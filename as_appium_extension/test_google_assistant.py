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
        word = "what's the weather tomorrow"
        self.voice.say(word, 'en')

        el = wait_for_element(
            self.driver,
            MobileBy.ID,
            GASSISTANT_PKG + ':id/chatui_streaming_text')
        assert el.text == word

        time.sleep(3)

    def test_open_music(self):
        self._ok_google()

        # ***Ask weather
        word = "Launch music"
        self.voice.say(word, 'en')

        time.sleep(3)

        assert self.driver.current_package == 'com.miui.player'

    def _ok_google(self):
        # ***Ok, Google
        self.voice.say_ok_google()

        el = wait_for_element(
            self.driver,
            MobileBy.ID,
            GASSISTANT_PKG + ':id/chatui_text')
        assert el.text == 'Hi, how can I help?'
