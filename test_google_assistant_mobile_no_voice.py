#!/usr/bin/python

import time

from helper.basetest_no_voice import BaseTestNoVoice

GASSISTANT_PKG = 'com.google.android.googlequicksearchbox'
TARGET_MUSIC_PKG = 'com.miui.player'
TIMEOUT = 10


class TestGoogleAssistant(BaseTestNoVoice):

    def test_whats_the_weather(self):

        self.driver.find_element_by_id(
            'com.google.android.googlequicksearchbox:id/logo_view').click()

        import time
        time.sleep(5)

        self.driver.find_element_by_id(
            'com.google.android.googlequicksearchbox:id/keyboard_indicator').click()
        time.sleep(5)

        el = self.driver.find_element_by_id(
            'com.google.android.googlequicksearchbox:id/input_text')
        el.send_keys("what's the weather tomorrow")

        self.driver.find_element_by_id(
            'com.google.android.googlequicksearchbox:id/explore_icon_container').click()

        time.sleep(5)
