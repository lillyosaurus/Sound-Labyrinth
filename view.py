import audio
import visual

class View:

    def __init__(self,map):
        self.visual = visual.VisualView(map)
        self.audio = audio.Audio()
        self.show_home_screen = True
        self.show_instructions = False
        self.show_credits = False
        self.game_on = False

    def update_screen(self,screen):
        self.visual.clear_screen()
        self.display_correct_screen(screen)
        self.visual.close_screen()
        self.visual.refresh_screen()
        self.game_on = self.visual.game_on

    def display_correct_screen(self,screen):
        if screen == 'home_screen':
            self.visual.draw_home_screen()
        elif screen == 'instructions':
            self.visual.draw_instructions()
        elif screen == 'credits':
            self.visual.draw_credits()
        elif screen == 'game':
            self.visual.draw_screen()

    def play_echo(self,distance,direction,sound):
        self.audio.echo(distance,direction,sound)

if __name__ == "__main__":
    pass
