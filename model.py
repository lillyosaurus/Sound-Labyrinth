import view
import game_map as gm
import controller as c
import pygame
import visual
import game_map
import game_object

class Model:

    def __init__(self):
        self.current_map = gm.GameMap()
        self.visual_view = visual.VisualView(self.current_map)
        self.controller = c.Controller()

    def run_game(self):
        pygame.init()

        while(self.visual_view.on == True):
            self.controller.read_input()

            #process controller inputs for moving
            if self.controller.move_keys['north']:
                self.current_map.player.rect.move_ip(0,-1)
                if self.current_map.player_wall_collision() != None:
                        self.current_map.player.rect.move_ip(0,1)
            if self.controller.move_keys['south']:
                self.current_map.player.rect.move_ip(0,1)
                if self.current_map.player_wall_collision() != None:
                        self.current_map.player.rect.move_ip(0,-1)
            if self.controller.move_keys['west']:
                self.current_map.player.rect.move_ip(-1,0)
                if self.current_map.player_wall_collision() != None:
                        self.current_map.player.rect.move_ip(1,0)
            if self.controller.move_keys['east']:
                self.current_map.player.rect.move_ip(1,0)
                if self.current_map.player_wall_collision() != None:
                        self.current_map.player.rect.move_ip(-1,0)
            #process controller inputs for pings
            if self.controller.ping_keys['front']:
                print(self.current_map.ping_from_player('up',3))
            if self.controller.ping_keys['right']:
                print(self.current_map.ping_from_player('right',3))
            if self.controller.ping_keys['left']:
                print(self.current_map.ping_from_player('left',3))
            if self.controller.ping_keys['back']:
                print(self.current_map.ping_from_player('down',3))


            self.visual_view.clear_screen()
            self.visual_view.draw_screen()
            self.visual_view.close_screen()
            self.visual_view.refresh_screen()


if __name__ == "__main__":
    m = Model()
    m.run_game()
