import pygame
pygame.init()

win_width = 1280
win_height = 768

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Zelda - projekt')


def exit():
    global run_game
    if keys[pygame.K_ESCAPE]:
        run_game = False
 

def settings():
    global run_game, keys
    pygame.time.delay(16)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
    keys = pygame.key.get_pressed()


run_game = True
while run_game:
    settings()

    keys = pygame.key.get_pressed()
    exit()

    win.fill((40, 40, 65)) # to tylko kolorek tła
    pygame.display.update()

pygame.quit()
