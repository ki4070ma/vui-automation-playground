#!/usr/bin/python

import time

from appium.webdriver.common.mobileby import MobileBy

from .helper.basetest import BaseTest
from .helper.test_helper import get_volume, wait_for_element, wait_for_elements

GASSISTANT_PKG = 'com.google.android.googlequicksearchbox'
TARGET_MUSIC_PKG = 'com.miui.player'
TIMEOUT = 10


class GoogleAssistantTest(BaseTest):

    def test_whats_the_weather(self):
        self._init_ok_google()

        # ***Ask weather
        self._say("what's the weather tomorrow")

        time.sleep(5)

    def test_volume_change(self):
        self._init_ok_google()

        # ***Ask "volume zero"
        self._say("volume zero", check_text=False)

        for _ in range(TIMEOUT):
            time.sleep(1)
            if get_volume(self.driver) == 0:
                break
        volume = get_volume(self.driver)
        assert volume == 0

        # ***Exit google assistant
        self.driver.back()

        # ***Ask "ok google"
        self._init_ok_google()

        # ***Ask "volume up"
        self._say("volume up", check_text=False)

        for _ in range(TIMEOUT):
            time.sleep(1)
            if get_volume(self.driver) > volume:
                break
        assert get_volume(self.driver) > volume

    def test_open_music(self):
        self._init_ok_google()

        # ***Ask weather
        self.voice.say("Launch music", 'en')

        for _ in range(TIMEOUT):
            time.sleep(1)
            if self.driver.current_package == TARGET_MUSIC_PKG:
                break
        assert self.driver.current_package == TARGET_MUSIC_PKG

    def _init_ok_google(self):
        # ***Ok, Google
        self.voice.say_ok_google()

        el = wait_for_element(
            self.driver,
            MobileBy.ID,
            GASSISTANT_PKG + ':id/chatui_text')
        assert el.text == 'Hi, how can I help?'

    def _say(self, word, lang='en', check_text=True):
        self.voice.say(word, lang)

        if check_text:
            el = wait_for_elements(
                self.driver,
                MobileBy.ID,
                GASSISTANT_PKG + ':id/chatui_streaming_text')[-1]
            assert el.text == word
