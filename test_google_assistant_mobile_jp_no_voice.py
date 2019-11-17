#!/usr/bin/python

import time

from helper.basetest_no_voice import BaseTestNoVoice

TARGET_MUSIC_PKG = ['com.miui.player', 'com.google.android.music']
TIMEOUT = 10


class TestGoogleAssistant(BaseTestNoVoice):

    # Format comes from http://appium.io/docs/en/writing-running-appium/caps/
    LANG = 'ja'
    LOCALE = 'JP'

    @classmethod
    def setup_class(cls):
        BaseTestNoVoice.pre_proc(cls.LANG, cls.LOCALE)

    def test_whats_the_weather(self):
        self.open_chat_mode()

        self.input_text(self._text('weather'))

        time.sleep(5)

        # TODO Add assertion

    def test_open_music(self):
        self.open_chat_mode()

        self.input_text(self._text('open_music'))

        time.sleep(5)

        # TODO Add assertion

    def _text(self, str_id):
        return self.s.get_sentence(
            str_id,
            "{}_{}".format(
                self.LANG,
                self.LOCALE))
