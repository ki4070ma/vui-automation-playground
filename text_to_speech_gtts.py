#!/usr/bin/env python

from gtts import gTTS
import os

def text_to_speech(text, lang):
  tmp_file = 'tmp.mp3'
  tts = gTTS(text=text, lang=lang)
  tts.save(tmp_file)
  os.system("mpg321 {}".format(tmp_file))

  if os.path.exists(tmp_file):
    os.remove(tmp_file)

if __name__ == '__main__':
  # text_to_speech('OK Google, Good morning', 'en')
  # text_to_speech('OK Google, こんにちは', 'ja')
  # text_to_speech('OK Google', 'ja')
  # text_to_speech('オーケー  グーグル', 'ja')
  text_to_speech('明日の天気を教えて', 'ja')
  # text_to_speech('OK Google, 明日の天気を教えて', 'ja')
