import pygame
pygame.init()

win_width = 1280
win_height = 780

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Zelda - projekt')

run_game = True
while run_game:
    pygame.time.delay(16)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    win.fill((40, 40, 65)) # to tylko kolorek tła
    pygame.display.update()

pygame.quit()
