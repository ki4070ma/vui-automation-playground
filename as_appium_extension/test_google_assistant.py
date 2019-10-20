#!/usr/bin/python

import os
import time
import unittest

from appium.webdriver.common.mobileby import MobileBy

from .helper.basetest import BaseTest
from .helper.test_helper import PATH, GlobalVar, wait_for_element

GASSISTANT_PKG = 'com.google.android.googlequicksearchbox'


class GoogleAssistantTest(BaseTest):

    def test_whats_the_weather(self) -> None:

        # ***Ok, Google
        self.voice.say_ok_google()

        el = wait_for_element(
            self.driver,
            MobileBy.ID,
            GASSISTANT_PKG + ':id/chatui_text')
        assert el.text == 'Hi, how can I help?'

        # ***Ask weather
        word = "what's the weather tomorrow"
        self.voice.say(word, 'en')

        el = wait_for_element(
            self.driver,
            MobileBy.ID,
            GASSISTANT_PKG + ':id/chatui_streaming_text')
        assert el.text == word

        time.sleep(3)


if __name__ == '__main__':
    import datetime as dt
    GlobalVar().log_root_dir = os.path.join(
        PATH('.'), 'output', dt.datetime.now().strftime('%y%m%d-%H%M%S'))
    os.path.isdir(GlobalVar().log_root_dir) or \
        os.makedirs(GlobalVar().log_root_dir)

    suite = unittest.TestLoader().loadTestsFromTestCase(
        GoogleAssistantTest)  # For debug
    unittest.TextTestRunner(verbosity=2).run(suite)
