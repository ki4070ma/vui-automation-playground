#!/usr/bin/python

import time

from appium import webdriver

from .helper.basetest import BaseTest
from .helper.desired_capabilities import get_disired_capabilities
from .helper.test_helper import get_locale

GASSISTANT_PKG = 'com.google.android.googlequicksearchbox'
TARGET_MUSIC_PKG = 'com.miui.player'
TIMEOUT = 10


class TestGoogleAssistantJp(BaseTest):

    @classmethod
    def setup_class(cls):
        driver = webdriver.Remote(
            'http://localhost:4723/wd/hub',
            get_disired_capabilities())
        locale = get_locale(driver)
        driver.quit()
        if locale != 'ja_JP':
            # TODO Change locale to ja_JP
            raise SystemError("Device locale is {}, not ja_JP.".format(locale))

    def test_asu_no_tenki(self):
        self._init_ok_google(response="はい、どんなご用でしょう？")
        self._say("明日の天気", lang='ja')

        time.sleep(5)
