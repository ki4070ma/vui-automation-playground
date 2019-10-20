#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from typing import Any

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class GlobalVar(object):

    log_root_dir = ''
    log_dir = ''

    _instance = None

    def __new__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

# Returns abs path relative to this file and not cwd


def PATH(p):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )


# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 10


def wait_for_element(driver, locator, value, timeout=SLEEPY_TIME):
    """Wait until the element located
    Args:
        driver (`appium.webdriver.webdriver.WebDriver`): WebDriver instance
        locator (str): Locator like WebDriver, Mobile JSON Wire Protocol
            (e.g. `appium.webdriver.common.mobileby.MobileBy.ACCESSIBILITY_ID`)
        value (str): Query value to locator
        timeout (int): Maximum time to wait the element. If time is over, `TimeoutException` is thrown
    Raises:
        `selenium.common.exceptions.TimeoutException`
    Returns:
        `appium.webdriver.webelement.WebElement`: Found WebElement
    """
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((locator, value))
    )
