import shutil
import os

print("""HOW TO USE :
put the hitsound you want to copy in the "input" folder and name it sound.wav (MUST BE .WAV - IF YOU NEED MP3 JUST CHANGE THE SOURCE CODE IM TOO LAZY)\n\n""")

input("press enter to continue")

filenameosu = ["drum-hitclap.wav","drum-hitfinish.wav", "drum-hitnormal.wav", "drum-hitwhistle.wav", "drum-sliderslide.wav", "drum-slidertick.wav", "drum-sliderwhistle.wav",
"normal-hitclap.wav","normal-hitfinish.wav", "normal-hitnormal.wav", "normal-hitwhistle.wav", "normal-sliderslide.wav", "normal-slidertick.wav", "normal-sliderwhistle.wav",
"soft-hitclap.wav","soft-hitfinish.wav", "soft-hitnormal.wav", "soft-hitwhistle.wav", "soft-sliderslide.wav", "soft-slidertick.wav", "soft-sliderwhistle.wav"]
base_hitsound = r'input/sound.wav'

os.mkdir("out")

for x in filenameosu:
    renamed_hitsound = r'out/' + x
    shutil.copyfile(base_hitsound, renamed_hitsound)

print("complete!")
