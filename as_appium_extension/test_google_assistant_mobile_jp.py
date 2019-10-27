#!/usr/bin/python

import time

from .helper.basetest import BaseTest

GASSISTANT_PKG = 'com.google.android.googlequicksearchbox'
TARGET_MUSIC_PKG = 'com.miui.player'
TIMEOUT = 10


class TestGoogleAssistantJp(BaseTest):

    def test_asu_no_tenki(self):
        self._init_ok_google(response="はい、どんなご用でしょう？")
        self._say("明日の天気", lang='ja')

        time.sleep(5)
