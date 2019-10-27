#!/usr/bin/python

import os

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from ..voice.voice import Voice
from .desired_capabilities import PATH, get_disired_capabilities
from .test_helper import (GlobalVar, get_locale, wait_for_element,
                          wait_for_elements)


class BaseTest(object):
    GASSISTANT_PKG = 'com.google.android.googlequicksearchbox'

    def setup_method(self, method) -> None:
        self.caps = get_disired_capabilities()
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

    def _init_ok_google(self, response='Hi, how can I help?'):
        # ***Ok, Google
        self.voice.say_ok_google()

        el = wait_for_element(
            self.driver,
            MobileBy.ID,
            self.GASSISTANT_PKG + ':id/chatui_text')
        assert el.text == response

    def _say(self, word, lang='en', check_text=True):
        self.voice.say(word, lang)

        if check_text:
            el = wait_for_elements(
                self.driver,
                MobileBy.ID,
                self.GASSISTANT_PKG + ':id/chatui_streaming_text')[-1]
            assert el.text == word

    @staticmethod
    def make_log_dir(dir_name: str) -> None:
        GlobalVar().log_dir = os.path.join(GlobalVar().log_root_dir, dir_name)
        os.path.isdir(GlobalVar().log_dir) or os.makedirs(GlobalVar().log_dir)

    @staticmethod
    def pre_proc(target_locale):
        driver = webdriver.Remote(
            'http://localhost:4723/wd/hub',
            get_disired_capabilities())
        try:
            locale = get_locale(driver)
            if locale != target_locale:
                # TODO Change locale to 'locale'
                # data = {"command": "am",
                #         "args": "start -n net.sanapeli.adbchangelanguage/.AdbChangeLanguage -e language {}".format(
                #             locale).split()}
                # driver.execute_script('mobile:shell', data)
                raise SystemError(
                    "Device locale is {}, not {}.".format(locale, target_locale))

            data = {
                "command": "pm",
                "args": "grant net.sanapeli.adbchangelanguage android.permission.CHANGE_CONFIGURATION".split()}
            driver.execute_script('mobile:shell', data)
        finally:
            driver.quit()
