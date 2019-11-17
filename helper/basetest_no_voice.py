#!/usr/bin/python

import os

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from sentences.loader import SentenceLoader
from voice.voice import Voice

from .desired_capabilities import PATH, get_disired_capabilities_no_voice
from .test_helper import GlobalVar, wait_for_element

# TODO This class is almost same to basetest.py


class BaseTestNoVoice(object):
    GASSISTANT_PKG = 'com.google.android.googlequicksearchbox'

    def setup_method(self, method) -> None:
        self.caps = get_disired_capabilities_no_voice()
        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', self.caps)

        if not GlobalVar().log_root_dir:
            import datetime as dt
            GlobalVar().log_root_dir = os.path.join(
                PATH('..'), 'output', dt.datetime.now().strftime('%y%m%d-%H%M%S'))
            os.path.isdir(GlobalVar().log_root_dir) or \
                os.makedirs(GlobalVar().log_root_dir)

        # Start taking evidence
        self.make_log_dir(method.__name__)
        self.driver.start_recording_screen()

        self.s = SentenceLoader()

        self.voice = Voice()

    def teardown_method(self) -> None:
        # Stop taking evidence
        payload = self.driver.stop_recording_screen()
        with open(os.path.join(GlobalVar().log_dir, "cap.mp4"), "wb") as fd:
            import base64
            fd.write(base64.b64decode(payload))

        with open(os.path.join(GlobalVar().log_dir, "log.txt"), "w") as fd:
            logs = self.driver.get_log('logcat')
            for lines in logs:
                for line in lines['message'].split('¥n'):
                    fd.write(line + '\n')

        # Exit from google assistant
        for _ in range(5):
            self.driver.back()

        # end the session
        self.driver.quit()

    def open_chat_mode(self):
        self._ID('logo_view').click()
        self._ID('keyboard_indicator').click()

    def input_text(self, text):
        self._ID('input_text').send_keys(text)
        self._ID('explore_icon_container').click()

    def _ID(self, id):
        return wait_for_element(
            self.driver,
            MobileBy.ID,
            '{}:id/{}'.format(self.GASSISTANT_PKG, id)
        )

    @staticmethod
    def make_log_dir(dir_name: str) -> None:
        GlobalVar().log_dir = os.path.join(GlobalVar().log_root_dir, dir_name)
        os.path.isdir(GlobalVar().log_dir) or os.makedirs(GlobalVar().log_dir)
