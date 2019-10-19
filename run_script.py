#!/usr/bin/env python

from vui_automation.voice import Voice
from vui_automation.logcat import Logcat


if __name__ ==  '__main__':
    # Usage: $ python run_script.py "hello" 'en' 'Displayed com.google.android.googlequicksearchbox'

    import argparse

    parser = argparse.ArgumentParser(description='Automation for vui')

    parser.add_argument('sentence', help='Sentence to say. e.g. "Ok google, hello."')
    parser.add_argument('lang', help='Language. e.g. "ja", "en"')
    parser.add_argument('word_to_wait', help='Word to wait. e.g. "Displayed com.google.android.googlequicksearchbox"')

    args = parser.parse_args()

    logcat = Logcat()
    voice = Voice()

    logcat.log_clear()
    voice.say_ok_google()
    voice.say(args.sentence, args.lang)
    logcat.wait_for_word_in_log(args.word_to_wait, log_clear=False)
