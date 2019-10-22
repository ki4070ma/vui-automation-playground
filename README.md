# vui-automation-playground

# How to use script

```bash
$pip install gTTS pyttsx3  # Linux
$sudo apt install mpg321 espeak  # Linux
# pip install gTTS pyttsx3 pyobjc  # Mac
# brew install mpg321  # Mac
$cd as_appium_extension
$pytest -s test_google_assistant_mobile.py
$pytest -s test_google_assistant_mobile.py::GoogleAssistantTest::test_asu_no_tenki
```

# Development

## Common

```bash
$pip install isort pre-commit
$pre-commit install
```

## Speech to text

* ```pip install SpeechRecognition```
* ```brew install portaudio```
* ```pip install pyaudio```

### Trial on terminal
* ```python -m speech_recognition```

# Reference
* Speech to text for Japanese
   * https://qiita.com/hamham/items/9b553d0759a2319ea211
