#!/usr/bin/env python



if __name__ == '__main__':
    import pyttsx3
    engine = pyttsx3.init()
    # engine.say('Good morning.')
    # engine.say('How are you?')
    # engine.say('こんにちは')
    engine.say('OK Google 明日の天気を教えて')
    engine.runAndWait()
