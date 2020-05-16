#!/usr/bin/python

import os


def PATH(p):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )


def get_disired_capabilities():
    caps = {
        'platformName': "Android",
        'deviceName': "Android Emulator",
        'app': PATH('../files/ApiDemos-debug.apk.zip'),
        'automationName': "uiautomator2",
    }
    return caps


def get_disired_capabilities_no_voice():
    caps = {
        'platformName': "Android",
        'deviceName': "Android Emulator",
        'app': PATH('../files/ApiDemos-debug.apk.zip'),
        'appPackage': 'com.google.android.apps.googleassistant',
        'appActivity': '.AssistantActivity',
        'automationName': "uiautomator2",
    }
    return caps
