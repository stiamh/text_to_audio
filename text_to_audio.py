from gtts import gTTS
from playsound import playsound

print('Please enter the name of .mp3 you want to convert to speech.')
audio = input()
language = 'en'

file = open("test.docx", "r")
speech = gTTS(text = str(file),lang='en',slow = False)

speech.save(audio)
playsound(audio)