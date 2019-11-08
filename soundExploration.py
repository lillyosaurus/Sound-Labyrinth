import pygame
from time import sleep

# intialise mixer
pygame.mixer.init()

# Load the sound file
ping = pygame.mixer.Sound("Sounds/ping_2.wav")
foot = pygame.mixer.Sound("Sounds/footstep_cement.wav")
hollow = pygame.mixer.Sound("Sounds/drop.wav")

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
channel.set_volume(.8,.05)
sleep(3)
