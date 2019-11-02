#!/usr/bin/python

import os


def PATH(p):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )


def get_disired_capabilities():
    caps = {
        'platformName': "Android",
        'platformVersion': "8.0",
        # 'platformVersion': "9",
        'deviceName': "Android Emulator",
        'app': PATH('../files/ApiDemos-debug.apk'),
        'otherApps': PATH('../files/apk/net.sanapeli.adbchangelanguage_0.80.apk'),
        'automationName': "uiautomator2",
    }
    return caps
