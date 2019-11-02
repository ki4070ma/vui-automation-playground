#!/usr/bin/python

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
