#!/usr/bin/python

import time

from appium.webdriver.common.mobileby import MobileBy
from helper.basetest_no_voice import BaseTestNoVoice
from helper.test_helper import wait_for_element

GASSISTANT_PKG = 'com.google.android.googlequicksearchbox'
TARGET_MUSIC_PKG = 'com.miui.player'
TIMEOUT = 10


class TestGoogleAssistant(BaseTestNoVoice):

    def test_whats_the_weather(self):

        self._ID('logo_view').click()

        self._ID('keyboard_indicator').click()

        self._ID('input_text').send_keys("what's the weather tomorrow")

        self._ID('explore_icon_container').click()

        time.sleep(5)

    def _ID(self, id):
        return wait_for_element(
            self.driver,
            MobileBy.ID,
            '{}:id/{}'.format(GASSISTANT_PKG, id)
        )
