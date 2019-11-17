#!/usr/bin/python

import time

from helper.basetest_no_voice import BaseTestNoVoice

TARGET_MUSIC_PKG = ['com.miui.player', 'com.google.android.music']
TIMEOUT = 10


class TestGoogleAssistant(BaseTestNoVoice):

    def test_whats_the_weather(self):
        self.open_chat_mode()

        self.input_text("what's the weather tomorrow")

        time.sleep(5)

    def test_open_music(self):
        self.open_chat_mode()

        self.input_text("Launch music")

        for _ in range(TIMEOUT):  # TODO Make better
            time.sleep(1)
            if self.driver.current_package in TARGET_MUSIC_PKG:
                break
        assert self.driver.current_package in TARGET_MUSIC_PKG
