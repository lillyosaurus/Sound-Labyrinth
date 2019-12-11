import audio
import visual

class View:
    """
    The class used to relate the visual and audio components before passing
    into the game model.

    Attributes:
    visual -> Visual class with functions to display objects on the screen
    audio -> Audio class with functions to play audio files
    show_home_screen -> boolean for displaying the home screen
    show_instructions -> boolean for displaying the instructions
    show_credits -> boolean for displaying the credits
    game_on -> boolean to determine whether to display the game
    """
    def __init__(self,map):
        """Initalize the View class with default variable values"""
        self.visual = visual.VisualView(map)
        self.audio = audio.Audio()
        self.show_home_screen = True
        self.show_instructions = False
        self.show_credits = False
        self.game_on = False

    def update_screen(self,screen):
        """Updates screen that is displayed in game window

        This function takes in a screen name as a string, refreshes the game
        window and calls a function to displays the correct screen.

        Keyword arguments:
            screen -> a string of text that indicates a screen to display
                ('home_screen','instructions','credits','game')
        Return values: None
        """
        self.visual.clear_screen()
        self.display_correct_screen(screen)
        self.visual.close_screen()
        self.visual.refresh_screen()

    def display_correct_screen(self,screen):
        """Calls function to display screen

        This function takes in a screen name as a string and draws the
        appropriate screen

        Keyword arguments:
            screen -> a string of text that indicates a screen to display
                ('home_screen','instructions','credits','game')
        Return values: None
        """
        if screen == 'home_screen':
            self.visual.draw_home_screen()
        elif screen == 'instructions':
            self.visual.draw_instructions()
        elif screen == 'credits':
            self.visual.draw_credits()
        elif screen == 'game':
            self.visual.draw_screen()

    def play_echo(self,distance,direction,sound):
        """Calls function to play echo

        Keyword arguments:
            distance -> integer value for distance to wall
            direction -> string with direction being pinged
            sound -> sound file to play
        Return values: None
        """
        self.audio.echo(distance,direction,sound)



    def play_footsteps(self,current_time,previous_time,delay,count):
        """Plays footstep audio

        Keyword arguments:
            current_time -> integer with current time in milliseconds
            previous_time -> integer with previous time that footstep audio was
                played in milliseconds
            delay -> integer indicating milliseconds to wait between playing
                footstep audio
            count -> integer referencing which footstep audio file to play
        Return values: None
        """
        if current_time - previous_time >= delay:
            previous_time = current_time
            if count < 5:
                count += 1
                self.audio.footstep_audio(count)
            else:
                count = 0

    def say_and_display(self,string,audio_engine):
        """Displays string at the top of the page and reads the text aloud

        Keyword arguments:
            string -> string to say and displays
            audio_engine -> engine to speak text that can have variables like rate,
            volume and volume_to_distance
        Return values: None
        """
        self.audio.string_to_speach(string,audio_engine)
        self.draw_paragraph(string,32,pygame.Rect((self.margin, self.margin, self.width - self.margin*2, 300)))

if __name__ == "__main__":
    pass
