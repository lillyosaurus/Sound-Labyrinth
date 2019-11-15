import audio
import visual

class View:

    def __init__(self,map):
        self.visual = visual.VisualView(map)
        self.on = True

    def update_screen(self):
        self.visual.clear_screen()
        self.visual.draw_screen()
        self.visual.close_screen()
        self.visual.refresh_screen()
        self.on = self.visual.on

if __name__ == "__main__":
    pass
