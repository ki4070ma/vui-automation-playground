#!/usr/bin/env python

import os
import subprocess as sp

import pyttsx3
from gtts import gTTS

DIR = 'files'
AUDIO_DIR = os.path.join(DIR, 'audio')

class Voice(object):

    def say(self, text='hello', lang='en'):
        '''Speech text from mic

        :param text: Text to speach
        :param lang: Language for text
        :return: None
        '''

        filename = os.path.join(AUDIO_DIR, '_'.join(text.split()).lower() + '.mp3')
        if not os.path.exists(filename):
            tts = gTTS(text=text, lang=lang)
            tts.save(filename)
        self._play_audio_file(filename)

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
            file=os.path.join(AUDIO_DIR, 'ok_google.mp3'))

    def _play_audio_file(self, file):
        if not os.path.exists(file):
            raise FileExistsError("{} doesn't exist.".format(file))
        sp.run(['mpg321', file], stdout=sp.DEVNULL, stderr=sp.DEVNULL)


if __name__ == '__main__':

    voice = Voice()

    # voice.say('OK Google', 'en')
    voice.say('明日の天気を教えて', 'ja')
