import pygame
import pyttsx3  # will need people to import this and libespeak1
                # pip install pyttsx3
                # sudo apt install libespeak1
from time import sleep

class Audio(object):
    """docstring for Audo."""
    def __init__(self):
        self.volume_to_distance = [1,.6,.1]
        self.time_delay_to_distance = [0,0,0]
        self.get_audio_files()
    def get_audio_files(self):
        self.ping_sound = pygame.mixer.Sound("Sounds/ping_2.wav")
        self.hollow_sound = pygame.mixer.Sound("Sounds/drop.wav")
        self.stone_step = []
        for i in range(1,7):
            self.stone_step.append(pygame.mixer.Sound("Sounds/stoneSteps/stone"+str(i)+".ogg"))

    def ping(self,sound):
        audio_length = pygame.mixer.Sound.get_length(sound)
        channel = sound.play()
        channel.set_volume(1,1)
        sleep(audio_length)

    def echo(self,distance,direction,sound):
        volume = self.volume_to_distance[distance - 1]
        time_delay = self.time_delay_to_distance[distance -1]
        audio_length = pygame.mixer.Sound.get_length(sound)

        if direction == 'front' or direction == 'back':
            sleep(time_delay)
            channel = sound.play()
            channel.set_volume(volume,volume)
        elif direction == 'right':
            sleep(time_delay)
            channel = sound.play()
            channel.set_volume(0,volume)
        elif direction == 'left':
            sleep(time_delay)
            channel = sound.play()
            channel.set_volume(volume,0)

    def string_to_speach(self,string,voice):
        pass



if __name__ == "__main__":
    import pyttsx3;
    engine = pyttsx3.init();
    engine.say("I will speak this text")
    engine.runAndWait()
## Walking Audio
"""
    pygame.mixer.init()
    ping_sound = pygame.mixer.Sound("Sounds/ping_2.wav")
    hollow_sound = pygame.mixer.Sound("Sounds/drop.wav")
    stone_step = []
    for i in range(1,7):
        stone_step.append(pygame.mixer.Sound("Sounds/stoneSteps/stone"+str(i)+".ogg"))

    ping(ping_sound)
    echo(3,'left',hollow_sound)
    ping(ping_sound)
    echo(2,'right',hollow_sound)
    ping(ping_sound)
    echo(1,'front',hollow_sound)
"""
    # i = 0
    # while i < 6:
    #     #step = random.choice(stone_step)
    #     step = stone_step[i]
    #     step.play()
    #     sleep(.2)
    #     i+=1
