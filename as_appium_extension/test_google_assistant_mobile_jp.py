#!/usr/bin/python

import time

from .helper.basetest import BaseTest

GASSISTANT_PKG = 'com.google.android.googlequicksearchbox'
TARGET_MUSIC_PKG = 'com.miui.player'
TIMEOUT = 10


class TestGoogleAssistantJp(BaseTest):

    LANG = 'ja'
    LOCALE = 'ja_JP'

    @classmethod
    def setup_class(cls):
        BaseTest.pre_proc(cls.LOCALE)

    def test_asu_no_tenki(self):
        self._init_ok_google(
            response=self.s.get_sentence(
                "ok_google_res", self.LOCALE))
        self._say(self.s.get_sentence("weather", self.LOCALE), lang=self.LANG)

        time.sleep(5)
