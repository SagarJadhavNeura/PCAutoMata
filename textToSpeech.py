# pip install pyttsx3
import pyttsx3


def speakTheText(textToBeSpoken): # to speak the text to be spoken
    conv = pyttsx3.init()
    conv.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0') # For female voice
    conv.setProperty('rate', 150) # voice speech rate (words per minute)
    conv.say(textToBeSpoken)
    conv.runAndWait()


speakTheText("Hello, world!")
