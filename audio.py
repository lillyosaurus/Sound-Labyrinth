import pygame
import pyttsx3  # will need people to import this and libespeak1
                # pip install pyttsx3
                # sudo apt install libespeak1
from time import sleep

class Audio(object):
    """
    The class used to process and play audio files in the game.

    Attributes:
    volume_to_distance -> list object with floats from 0 to 1 indicating volume
        to play a sound at
    """
    def __init__(self):
        """Initalize the Audio class with default variable values"""
        self.volume_to_distance = [1,.6,.1]
        self.get_audio_files()

    def get_audio_files(self):
        """Gathers audio files

        Attributes:
            ping_sound -> ping audio file
            hollow_sound -> hollow sound audio file
            stone_step -> list containing a series of six audio files that
                form the sound of footsteps
        Return values: None
        """
        self.ping_sound = pygame.mixer.Sound("Sounds/ping_2.wav")
        self.hollow_sound = pygame.mixer.Sound("Sounds/drop.wav")
        self.stone_step = []
        for i in range(1,7):
            self.stone_step.append(pygame.mixer.Sound("Sounds/stoneSteps/stone"+str(i)+".ogg"))

    def ping(self,sound):
        """Plays audio file

        Keyword arguments:
            sound -> audio file to play
        Return values: None
        """
        audio_length = pygame.mixer.Sound.get_length(sound)
        channel = sound.play()
        channel.set_volume(1,1)
        sleep(audio_length)

    def echo(self,distance,direction,sound):
        """Plays audio file with respect to distance and direction of sound

        This function takes an audio file and implements stereo sound to give
        the player a more imersive experience and communicate information
        auditoraly

        Keyword arguments:
            distance -> integer between 1 and 3 indicating distance of sound
            direction -> string containing the direction that the sound is
                coming from ('front','back','left','right')
            sound -> audio file to play
        Return values: None
        """
        volume = self.volume_to_distance[distance - 1]
        audio_length = pygame.mixer.Sound.get_length(sound)

        if direction == 'front' or direction == 'back':
            channel = sound.play()
            channel.set_volume(volume,volume)
        elif direction == 'right':
            channel = sound.play()
            channel.set_volume(0,volume)
        elif direction == 'left':
            channel = sound.play()
            channel.set_volume(volume,0)

    def string_to_speach(self,string,engine):
        """Converts a string into spoken word and speaks

        The function takes a string and audio engine and speaks the string with
        the voice of the audio engine.

        Keyword arguments:
            string -> a string of text
            engine -> engine to speak text that can have variables like rate,
            volume and volume_to_distance
        Return values: None
        """
        engine.say(string)
        engine.runAndWait()

    def footstep_audio(self,count):
        """Plays a single footstep audio file

        The function will take in a count variable and play the respective
        footstep audio file

        Keyword arguments:
            count -> A variable that indicates which audio file to play
        Return values: None
        """
        step = self.stone_step[count]
        step.play()




if __name__ == "__main__":
    #engine = pyttsx3.init();
    #engine.say("I will speak this text")
    #engine.runAndWait()
## Walking Audio
    footstep_count = 0
    pygame.init()
    pygame.mixer.init()
    audio = Audio()
    if footstep_count < 6:
        footstep_count += 1
        audio.footstep_audio(footstep_count)
    else:
        footstep_count = 0


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
