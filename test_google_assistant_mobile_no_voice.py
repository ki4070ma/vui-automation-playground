#!/usr/bin/python

import time

from helper.basetest_no_voice import BaseTestNoVoice

GASSISTANT_PKG = 'com.google.android.googlequicksearchbox'
TARGET_MUSIC_PKG = 'com.miui.player'
TIMEOUT = 10


class TestGoogleAssistant(BaseTestNoVoice):

    def test_whats_the_weather(self):

        # ***Ask weather
        self._say("what's the weather tomorrow")

        time.sleep(5)
