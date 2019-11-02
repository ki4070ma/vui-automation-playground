# vui-automation-playground

# How to use script

## Set up appium server
* I'd recommend appium-desktop
   * https://github.com/appium/appium-desktop

## Resolve dependencies

### Linux

```bash
$pip install -r requirements.txt
$sudo apt install mpg321 espeak
```

### Mac

```bash
$pip install -r requirements_mac.txt
$brew install mpg321
```

## Execute script

```bash
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
