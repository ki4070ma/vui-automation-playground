#!/usr/bin/env python

from gtts import gTTS
import pyttsx3

import os

class Voice(object):

  def text_to_speech(self, text, lang):
    '''Speech text from mic

    :param text: Text to speach
    :param lang: Language for text
    :return: None
    '''

    tmp_file = 'tmp.mp3'
    tts = gTTS(text=text, lang=lang)
    tts.save(tmp_file)
    os.system("mpg321 {}".format(tmp_file))

    if os.path.exists(tmp_file):
      os.remove(tmp_file)

  def text_to_speech_pyttsx3(self, text):
    '''

    :param text:
    :return:
    '''
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

  def say_ok_google_mori(self, file='files/ok_google_mori.mp3'):
    '''

    :param file:
    :return:
    '''
    if not os.path.exists(file):
      raise FileExistsError("{} doesn't exist.".format(file))
    os.system("mpg321 {}".format(file))


if __name__ == '__main__':

  voice = Voice()

  # voice.text_to_speech('OK Google, Good morning', 'en')
  # voice.text_to_speech('OK Google, こんにちは', 'ja')
  voice.text_to_speech('OK Google', 'en')
  # voice.text_to_speech('オーケー  グーグル', 'ja')
  # voice.text_to_speech('明日の天気を教えて', 'ja')
  # voice.text_to_speech('OK Google, 明日の天気を教えて', 'ja')
