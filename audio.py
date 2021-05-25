from gtts import gTTS
from playsound import playsound

import os

with open('output.txt','r') as file:
   mytext = file.read()

sceneDescription = mytext


language = 'en'


myobj = gTTS(text=sceneDescription, lang=language, slow=False)

myobj.save("AudioOutput.mp3")

playsound('AudioOutput.mp3')


from englisttohindi.englisttohindi import EngtoHindi

with open('output.txt','r') as file:
    sceneDesc = file.read()

res = EngtoHindi(sceneDesc)
print(res.convert)
hindi  = res.convert

myobj1 = gTTS(text=hindi, lang=language, slow=False)
myobj1.save('hindi.mp3')
playsound('hindi.mp3')




