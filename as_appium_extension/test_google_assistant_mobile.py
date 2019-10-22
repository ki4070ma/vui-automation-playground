#!/usr/bin/python

import time

from appium.webdriver.common.mobileby import MobileBy

from .helper.basetest import BaseTest
from .helper.test_helper import wait_for_element

GASSISTANT_PKG = 'com.google.android.googlequicksearchbox'


class GoogleAssistantTest(BaseTest):

    def test_whats_the_weather(self):
        self._ok_google()

        # ***Ask weather
        self._say("what's the weather tomorrow")

        time.sleep(5)

    def test_asu_no_tenki(self):
        self._ok_google()
        self._say("明日の天気", lang='ja')

        time.sleep(5)

    def test_open_music(self):
        self._ok_google()

        # ***Ask weather
        word = "Launch music"
        self.voice.say(word, 'en')

        TIMEOUT = 10
        TARGET_PKG = 'com.miui.player'
        for _ in range(TIMEOUT):
            time.sleep(1)
            if self.driver.current_package == TARGET_PKG:
                break
        assert self.driver.current_package == TARGET_PKG

    def _ok_google(self):
        # ***Ok, Google
        self.voice.say_ok_google()

        el = wait_for_element(
            self.driver,
            MobileBy.ID,
            GASSISTANT_PKG + ':id/chatui_text')
        assert el.text == 'Hi, how can I help?'

    def _say(self, word, lang='en'):
        self.voice.say(word, lang)

        el = wait_for_element(
            self.driver,
            MobileBy.ID,
            GASSISTANT_PKG + ':id/chatui_streaming_text')
        assert el.text == word
