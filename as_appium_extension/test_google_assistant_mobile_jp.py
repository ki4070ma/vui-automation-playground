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
        try:
            locale = get_locale(driver)
            if locale != 'ja_JP':
                # TODO Change locale to ja_JP
                # data = {"command": "am",
                #         "args": "start -n net.sanapeli.adbchangelanguage/.AdbChangeLanguage -e language {}".format(
                #             locale).split()}
                # driver.execute_script('mobile:shell', data)
                raise SystemError(
                    "Device locale is {}, not ja_JP.".format(locale))

            data = {
                "command": "pm",
                "args": "grant net.sanapeli.adbchangelanguage android.permission.CHANGE_CONFIGURATION".split()}
            driver.execute_script('mobile:shell', data)
        finally:
            driver.quit()

    def test_asu_no_tenki(self):
        self._init_ok_google(response="はい、どんなご用でしょう？")
        self._say("明日の天気", lang='ja')

        time.sleep(5)
