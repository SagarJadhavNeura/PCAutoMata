import pyttsx3

conv = pyttsx3.init()

voices = conv.getProperty('voices')

# Loop through voices to find a female voice
for voice in voices:
    print(voice)
    if "Microsoft Zira Desktop - English (United States)" in voice.name:
        conv.setProperty('voice', voice.id)
        break

conv.setProperty('rate', 150)

answer = input("Give any text.\n")

conv.say(answer)
conv.runAndWait()