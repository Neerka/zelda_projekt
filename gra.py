import pygame
pygame.init()

win_width = 1280
win_height = 768

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Zelda - projekt')

class Map_Tile:
    def __init__(self, texture: str):
        self.texture = pygame.image.load(texture).convert_alpha()


def build_walls(map):
    walls = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == W or map[i][j] == D:
                walls.append(pygame.Rect(j*64, i*64, 64, 64))
    return walls


def build_finish(map):
    finish = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == E:
                finish.append(pygame.Rect(j*64, i*64, 64, 64))
    return finish


def find_Destructible(map):
    destructible = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == D:
                destructible.append((i, j))
    return destructible


def load_level(level):
    global gracz, walls, finishes, destructible
    walls = build_walls(maps[level])
    gracz = Player()
    finishes = build_finish(maps[level])
    destructible = find_Destructible(maps[level])
   
  
def draw_map(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            win.blit(map[i][j].texture, (j*64, i*64))


currentLevel = 0

E = Map_Tile('grasstile.png')  # przejście do następnego poziomu
F = Map_Tile('grasstile.png')  # podłoga, po której można chodzić 
W = Map_Tile('rock.png')  # stałe ściany
D = Map_Tile('rockdestroyed.png')  # zniszczalne bombą

map1 = [
    [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, F, F, F, F, F, W, F, F, F, F, F, F, F, F, F, F, F, F, W],
    [W, F, F, F, F, F, W, F, F, F, F, F, F, F, F, F, F, F, F, E],
    [W, W, W, W, F, F, W, W, W, W, W, W, W, W, F, F, F, F, F, W],
    [W, F, F, F, F, F, F, F, F, F, W, F, F, W, F, F, F, F, F, W],
    [W, F, F, F, F, F, F, F, F, F, W, F, F, W, F, F, F, F, F, W],
    [W, F, F, F, F, F, F, F, F, F, D, F, F, W, F, F, F, F, F, W],
    [W, F, F, F, F, W, W, W, W, D, D, F, F, W, F, W, F, F, F, W],
    [W, D, F, F, F, W, F, F, F, F, F, F, F, W, F, W, F, F, F, W],
    [W, F, F, F, F, W, F, F, F, F, F, F, F, W, W, W, F, F, F, W],
    [W, F, F, F, F, W, F, F, F, F, F, F, F, F, F, F, F, F, F, W],
    [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
]

map2 = [
    [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, F, F, F, F, F, F, F, F, F, F, D, F, F, F, F, F, F, F, W],
    [F, F, F, F, F, F, F, F, F, F, F, D, F, F, F, F, F, F, F, W],
    [W, W, W, F, F, F, W, W, W, W, W, W, W, W, F, F, F, F, F, W],
    [W, F, F, F, F, F, W, F, F, F, W, F, F, W, F, F, F, F, F, W],
    [W, F, F, F, F, F, W, F, F, F, F, F, F, W, F, F, F, F, F, W],
    [W, F, F, F, F, F, W, F, F, F, F, F, F, W, F, F, F, F, F, W],
    [W, F, F, F, F, W, W, W, W, F, F, F, F, W, F, W, F, F, F, W],
    [W, W, W, F, W, W, F, F, F, F, F, F, F, W, F, W, F, F, F, W],
    [W, F, F, F, F, W, F, F, F, F, F, F, F, W, W, W, F, F, F, E],
    [W, F, F, F, F, W, F, F, F, F, F, F, F, F, D, F, F, F, F, W],
    [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
]

map3 = [
    [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, W],
    [W, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, W],
    [W, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, W],
    [W, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, W],
    [W, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, W],
    [W, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, W],
    [W, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, W],
    [W, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, W],
    [W, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, W],
    [W, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, F, W],
    [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
]

maps = [map1, map2, map3]
walls = build_walls(maps[currentLevel])

        
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
load_level(currentLevel)
while run_game:
    settings()

    exit()
