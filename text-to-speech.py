from gtts import gTTs
import os

myText = 'Text to speech conversion using Python'

language = 'en'

output = gTTs(text=myText, lang=language, slow=False)

output.save("output.mp3")

os.system("start output.mp3")

