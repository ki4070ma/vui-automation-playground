#!/usr/bin/python

import os
import unittest

from appium.webdriver.common.mobileby import MobileBy

from .helper.basetest import BaseTest
from .helper.test_helper import PATH, GlobalVar, wait_for_element
from .voice.voice import Voice


class SampleAndroidTest(BaseTest):

    def test_test(self) -> None:

        v = Voice()

        self.driver.back()

        v.say_ok_google()

        id = 'com.google.android.googlequicksearchbox:id/chatui_text'
        el = wait_for_element(self.driver, MobileBy.ID, id)
        print('***start')
        print(el.text)
        print('***end')

        v.say('hello', 'en')


if __name__ == '__main__':
    import datetime as dt
    GlobalVar().log_root_dir = os.path.join(
        PATH('.'), 'output', dt.datetime.now().strftime('%y%m%d-%H%M%S'))
    os.path.isdir(GlobalVar().log_root_dir) or \
        os.makedirs(GlobalVar().log_root_dir)

    suite = unittest.TestLoader().loadTestsFromTestCase(SampleAndroidTest)  # For debug
    unittest.TextTestRunner(verbosity=2).run(suite)
