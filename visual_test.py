import pygame
import view
import game_map
import game_object

pygame.init()
current_map = game_map.GameMap()
visual_view = view.View(current_map)

while(visual_view.on == True):

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
            current_map.player.rect.move_ip(0,-1)
    if keys[pygame.K_DOWN]:
            current_map.player.rect.move_ip(0,1)
    if keys[pygame.K_LEFT]:
            current_map.player.rect.move_ip(-1,0)
    if keys[pygame.K_RIGHT]:
            current_map.player.rect.move_ip(1,0)

    visual_view.clear_screen()
    visual_view.draw_screen()
    visual_view.close_screen()
    visual_view.refresh_screen()
    

