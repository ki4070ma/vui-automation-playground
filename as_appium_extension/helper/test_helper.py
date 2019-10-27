#!/usr/bin/python

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


def wait_for_elements(driver, locator, value, timeout=SLEEPY_TIME):
    """Wait until all elements located
    Args:
        driver (`appium.webdriver.webdriver.WebDriver`): WebDriver instance
        locator (str): Locator like WebDriver, Mobile JSON Wire Protocol
            (e.g. `appium.webdriver.common.mobileby.MobileBy.ACCESSIBILITY_ID`)
        value (str): Query value to locator
        timeout (int): Maximum time to wait the element. If time is over, `TimeoutException` is thrown
    Raises:
        `selenium.common.exceptions.TimeoutException`
    Returns:
        :obj:`list` of :obj:`appium.webdriver.webelement.WebElement`: Found WebElements
    """
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_all_elements_located((locator, value))
    )


def get_volume(driver):
    KEY = "STREAM_MUSIC"
    data = {"command": "dumpsys", "args": ['audio']}
    text = driver.execute_script('mobile:shell', data)
    flg_STREAM_MUSIC = False
    import re
    for line in text.split('\n'):
        if flg_STREAM_MUSIC:
            tmp = re.search(r'\(speaker\): [0-9]+', line)
            if tmp:
                return int(tmp.group().split()[-1])
        elif KEY in line:
            flg_STREAM_MUSIC = True
    raise SystemError("Can't get volume from the device.")


def get_locale(driver):
    data = {"command": "getprop", "args": ["persist.sys.locale"]}
    return driver.execute_script(
        'mobile:shell', data).strip().replace('-', '_')
