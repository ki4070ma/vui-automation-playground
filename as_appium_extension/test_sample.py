#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import unittest

from helper.test_helper import PATH, BaseTest, GlobalVar


class SampleAndroidTest(BaseTest):

    def test_test(self) -> None:

        print(self.driver.location)

        self.driver.back()

        self.driver.back()

        import time
        time.sleep(3)


if __name__ == '__main__':
    import datetime as dt
    GlobalVar().log_root_dir = os.path.join(
        PATH('.'), 'output', dt.datetime.now().strftime('%y%m%d-%H%M%S'))
    os.path.isdir(
        GlobalVar().log_root_dir) or os.makedirs(
        GlobalVar().log_root_dir)

    suite = unittest.TestLoader().loadTestsFromTestCase(SampleAndroidTest)  # For debug
    unittest.TextTestRunner(verbosity=2).run(suite)
