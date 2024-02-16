# pip install pyttsx3
import pyttsx3

conv = pyttsx3.init()

voices = conv.getProperty('voices')

'''
# Loop through voices to find a female voice
for voice in voices:
    print(voice)
    if "Microsoft Zira Desktop - English (United States)" in voice.name:
        conv.setProperty('voice', voice.id)
        print(voice.id)
        break
'''
conv.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0') # For female voice

conv.setProperty('rate', 130) # voice speech rate (words per minute)

answer = input("Give any text.\n")

conv.say(answer)
conv.runAndWait()

# wait 
