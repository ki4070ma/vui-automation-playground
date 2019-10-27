#!/usr/bin/python

import time

from appium.webdriver.common.mobileby import MobileBy

from .helper.basetest import BaseTest
from .helper.test_helper import get_volume, wait_for_element, wait_for_elements

GASSISTANT_PKG = 'com.google.android.googlequicksearchbox'
TARGET_MUSIC_PKG = 'com.miui.player'
TIMEOUT = 10


class GoogleAssistantTestJp(BaseTest):

    @classmethod
    def setUpClass(cls, locale='en_US'):  # FIXME Would remove locale
        super(GoogleAssistantTestJp, cls).setUpClass('ja_JP')

    def test_asu_no_tenki(self):
        self._init_ok_google(response="はい、どんなご用でしょう？")
        self._say("明日の天気", lang='ja')

        time.sleep(5)
