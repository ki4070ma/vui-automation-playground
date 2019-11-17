#!/usr/bin/python

import time

from helper.basetest_no_voice import BaseTestNoVoice

TARGET_MUSIC_PKG = 'com.miui.player'
TIMEOUT = 10


class TestGoogleAssistant(BaseTestNoVoice):

    def test_whats_the_weather(self):
        self.open_chat_mode()

        self.input_text("what's the weather tomorrow")

        time.sleep(5)
