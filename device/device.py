#!/usr/bin/python


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
