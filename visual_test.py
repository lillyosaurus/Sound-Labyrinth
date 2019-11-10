import pygame
import view
import game_map
import game_object

pygame.init()
current_map = game_map.GameMap()
visual_view = view.View(current_map)

test_object = game_object.Wall(150, 200)
test_object.print_loaction()
test_object.print_size()

while(visual_view.on == True):
    visual_view.clear_screen()
    visual_view.draw_screen()
    # test_object.draw_offset(visual_view.screen, 100, 100)
    visual_view.close_screen()
    visual_view.refresh_screen()
    

