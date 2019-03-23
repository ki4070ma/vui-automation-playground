#!/usr/bin/env python

import pyttsx3


def text_to_speech(sentence):
    engine = pyttsx3.init()
    engine.say(sentence)
    engine.runAndWait()

def speech_to_text():
    import speech_recognition as sr

    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source, timeout=5)

    try:
        print("You said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

if __name__ == '__main__':
    text_to_speech('Good morning')
    text_to_speech('How are you?')
    text_to_speech('OK Google 明日の天気を教えて')

