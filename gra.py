class Map_Tile:


    def __init__(self, texture: str):
        self.texture = pygame.image.load(texture).convert_alpha()


def draw_map(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            win.blit(map[i][j].texture, (j*64, i*64))


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
load_level(currentLevel)
