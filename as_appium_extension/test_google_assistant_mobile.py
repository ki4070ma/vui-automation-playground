#!/usr/bin/python

import time

from appium import webdriver

from .helper.basetest import BaseTest
from .helper.desired_capabilities import get_disired_capabilities
from .helper.test_helper import get_locale, get_volume

GASSISTANT_PKG = 'com.google.android.googlequicksearchbox'
TARGET_MUSIC_PKG = 'com.miui.player'
TIMEOUT = 10


class TestGoogleAssistant(BaseTest):

    @classmethod
    def setup_class(cls):
        driver = webdriver.Remote(
            'http://localhost:4723/wd/hub',
            get_disired_capabilities())
        locale = get_locale(driver)
        driver.quit()
        if locale != 'en_US':
            # TODO Change locale to en_US
            raise SystemError("Device locale is {}, not en_US.".format(locale))

    def test_whats_the_weather(self):
        self._init_ok_google()

        # ***Ask weather
        self._say("what's the weather tomorrow")

        time.sleep(5)

    def test_volume_change(self):
        self._init_ok_google()

        # ***Ask "volume zero"
        self._say("volume zero", check_text=False)

        for _ in range(TIMEOUT):
            time.sleep(1)
            if get_volume(self.driver) == 0:
                break
        volume = get_volume(self.driver)
        assert volume == 0

        # ***Exit google assistant
        self.driver.back()

        # ***Ask "ok google"
        self._init_ok_google()

        # ***Ask "volume up"
        self._say("volume up", check_text=False)

        for _ in range(TIMEOUT):
            time.sleep(1)
            if get_volume(self.driver) > volume:
                break
        assert get_volume(self.driver) > volume

    def test_open_music(self):
        self._init_ok_google()

        # ***Ask weather
        self.voice.say("Launch music", 'en')

        for _ in range(TIMEOUT):
            time.sleep(1)
            if self.driver.current_package == TARGET_MUSIC_PKG:
                break
        assert self.driver.current_package == TARGET_MUSIC_PKG
