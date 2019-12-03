# pip install pyttsx3 pypiwin32
import pyttsx3
# One time initialization
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Set properties _before_ you add things to say
engine.setProperty('rate', 120)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1
#
# Queue up things to say.
# There will be a short break between each one
# when spoken, like a pause between sentences.
engine.say("You've got mail!")
engine.say("You can queue up multiple items")

# Flush the say() queue and play the audio
engine.runAndWait()

# Program will not continue execution until
# all speech is done talking

# afrikaans
# aragonese
# bulgarian
# bosnian
# catalan
# czech
# welsh
# danish
# german
# greek
# default
# english
# en-scottish
# english-north
# english_rp
# english_wmids
# english-us
# en-westindies
# esperanto
# spanish
# spanish-latin-am
# estonian
# persian
# persian-pinglish
# finnish
# french-Belgium
# french
# irish-gaeilge
# greek-ancient
# hindi
# croatian
# hungarian
# armenian
# armenian-west
# indonesian
# icelandic
# italian
# lojban
# georgian
# kannada
# kurdish
# latin
# lingua_franca_nova
# lithuanian
# latvian
# macedonian
# malayalam
# malay
# nepali
# dutch
# norwegian
# punjabi
# polish
# brazil
# portugal
# romanian
# russian
# slovak
# albanian
# serbian
# swedish
# swahili-test
# tamil
# turkish
# vietnam
# vietnam_hue
# vietnam_sgn
# Mandarin
# cantonese
'''

# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks!'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
#os.system("mpg321 welcome.mp3")
'''
