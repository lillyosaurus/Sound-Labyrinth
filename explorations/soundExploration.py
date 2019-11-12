"""
import pygame
from time import sleep
import random
#import sndlib

# intialise mixer
pygame.mixer.init()

# Load the sound file
ping = pygame.mixer.Sound("Sounds/ping_2.wav")
foot = pygame.mixer.Sound("Sounds/footstep_cement.wav")
hollow = pygame.mixer.Sound("Sounds/drop.wav")

stone_step = []
for i in range(1,7):
    stone_step.append(pygame.mixer.Sound("Sounds/stoneSteps/stone"+str(i)+".ogg"))
"""
"""
i = 0
while i < 6:
    #step = random.choice(stone_step)
    step = stone_step[i]
    step.play()
    sleep(.2)
    i+=1
"""
'''
# Play the file and put it into a channel object
channel = ping.play()
#channel = foot.play()

# Mute right speaker
channel.set_volume(1,0)
sleep(1.5)
channel.stop()
channel = ping.play()
channel.set_volume(1,0)
sleep(3)

# Mute left speaker
channel = ping.play()
channel.set_volume(0,1)
sleep(4)
channel = ping.play()
channel.set_volume(0,.05)
sleep(3)

# Dual Feedback
channel = ping.play()
channel.set_volume(1,1)
sleep(3)
channel = ping.play()
channel.set_volume(.8,0)
sleep(.1)
channel = ping.play()
channel.set_volume(0,.4)
sleep(3)
'''



from gtts import gTTS
import os
tts = gTTS(text='Hi my name is Kyle Bertram', lang='en-uk')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
