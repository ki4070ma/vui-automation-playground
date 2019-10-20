#!/usr/bin/env python

import os
import subprocess as sp

import pyttsx3
from gtts import gTTS


class Voice(object):

    def say(self, text='hello', lang='en'):
        '''Speech text from mic

        :param text: Text to speach
        :param lang: Language for text
        :return: None
        '''

        tmp_file = 'tmp.mp3'
        if os.path.exists(tmp_file):
            os.remove(tmp_file)

        tts = gTTS(text=text, lang=lang)
        tts.save(tmp_file)
        self._play_audio_file(tmp_file, delete_file=True)

    def text_to_speech_pyttsx3(self, text='hello'):
        '''

        :param text:
        :return:
        '''
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def say_ok_google(self):
        self._play_audio_file(
            file='files/ok_google_mori.mp3',
            delete_file=False)

    def _play_audio_file(self, file, delete_file=False):
        if not os.path.exists(file):
            raise FileExistsError("{} doesn't exist.".format(file))
        sp.run(['mpg321', file], stdout=sp.DEVNULL, stderr=sp.DEVNULL)

        if delete_file and os.path.exists(file):
            os.remove(file)


if __name__ == '__main__':

    voice = Voice()

    # voice.text_to_speech('OK Google, Good morning', 'en')
    # voice.text_to_speech('OK Google, こんにちは', 'ja')
    voice.say('OK Google', 'en')
    # voice.text_to_speech('オーケー  グーグル', 'ja')
    # voice.text_to_speech('明日の天気を教えて', 'ja')
    # voice.text_to_speech('OK Google, 明日の天気を教えて', 'ja')
