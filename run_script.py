#!/usr/bin/env python

from text_to_speech_gtts import text_to_speech
from logcat import wait_for_word_in_log

if __name__ ==  '__main__':
    # Usage: $ python test.py input.txt output.txt --arg3 11111 -a 22222

    import argparse

    parser = argparse.ArgumentParser(description='Automation for vui')

    parser.add_argument('sentence', help='Sentence to say. e.g. "Ok google, hello."')
    parser.add_argument('lang', help='Language. e.g. "ja", "en"')
    parser.add_argument('word_to_wait', help='Word to wait. e.g. "Displayed com.google.android.googlequicksearchbox"')

    args = parser.parse_args()

    text_to_speech(args.sentence, args.lang)
    wait_for_word_in_log(args.word_to_wait)
