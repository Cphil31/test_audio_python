from gtts import gTTS
import os

text = "hello world"

language = 'fr'


p = gTTS(text=text,lang=language,slow=False)

p.save("hello.mp3")

os.system("hello.mp3")