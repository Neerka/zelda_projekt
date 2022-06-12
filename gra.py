import pygame
pygame.init()

win_width = 1280
win_height = 768

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Zelda - projekt')

class Map_Tile:
    def __init__(self, texture: str):
        self.texture = pygame.image.load(texture).convert_alpha()

        
class Player:
    def __init__(self):
       self.speed = 3
        self.sword_length = 0  # 48
        self.sword_width = 0  # 16
        self.health_points = 100
        self.attack_points = 25
        self.height = 32
        self.width = 32
        self.x_position = 100
        self.y_position = 100
        self.x_sword = 0
        self.y_sword = 0
        self.throwCount = 8
        self.x_con = self.width + self.speed
        self.y_con = self.height + self.speed
        self.collisional = 1
        self.sword_exists = 0
        self.immune = False
        self.rectangle = pygame.Rect(self.x_position, self.y_position, self.width, self.height)
        self.sword_rect = pygame.Rect(self.x_sword, self.y_sword, self.sword_length, self.sword_width)

    def move(self):
        if keys[pygame.K_LEFT] and self.x_position > self.speed:
            self.x_position -= self.speed
            self.rectangle.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x_position < map_width-self.x_con:
            self.x_position += self.speed
            self.rectangle.x += self.speed
        if keys[pygame.K_UP] and self.y_position > self.speed:
            self.y_position -= self.speed
            self.rectangle.y -= self.speed
        if keys[pygame.K_DOWN] and self.y_position < win_height-self.y_con:
            self.y_position += self.speed
            self.rectangle.y += self.speed
            
    def attack(self):
       if keys[pygame.K_a]:
           self.sword_width = 24
           self.sword_length = 72
           self.x_sword = self.x_position - self.sword_length
           self.y_sword = self.y_position + 0.25*self.height
           self.sword_rect = pygame.Rect(self.x_sword,
                                         self.y_sword,
                                         self.sword_length, self.sword_width)
           self.sword_exists = 1
           return True
           
       elif keys[pygame.K_d]:
           self.sword_width = 24
           self.sword_length = 72
           self.x_sword = self.x_position + self.width
           self.y_sword = self.y_position + 0.25*self.width
           self.sword_rect = pygame.Rect(self.x_sword,
                                         self.y_sword,
                                         self.sword_length, self.sword_width)
           self.sword_exists = 1
           return True
           
       elif keys[pygame.K_w]:
           self.sword_width = 72
           self.sword_length = 24
           self.x_sword = self.x_position + 0.25*self.height
           self.y_sword = self.y_position - self.sword_width
           self.sword_rect = pygame.Rect(self.x_sword,
                                         self.y_sword,
                                         self.sword_length, self.sword_width)
           self.sword_exists = 1
           return True
           
       elif keys[pygame.K_s]:
           self.sword_width = 72
           self.sword_length = 24
           self.x_sword = self.x_position + 0.25*self.height
           self.y_sword = self.y_position + self.width
           self.sword_rect = pygame.Rect(self.x_sword,
                                         self.y_sword,
                                         self.sword_length, self.sword_width)
           self.sword_exists = 1
           return True
           
       else:
           self.sword_exists = 0
        
   def throw_sword(self):
        if self.throwCount:
            if keys[pygame.K_a]:
                self.sword_rect.x -= (self.throwCount**2)*0.5
            if keys[pygame.K_d]:
                self.sword_rect.x += (self.throwCount**2)*0.5
            if keys[pygame.K_w]:
                self.sword_rect.y -= (self.throwCount**2)*0.5
            if keys[pygame.K_s]:
                self.sword_rect.y += (self.throwCount**2)*0.5
        else:
            self.throwCount = 8

    def place_bomb(self):
        global bomba
        if keys[pygame.K_q] and not bomba.isSet:
            bomba = Bomb(self.x_position+8, self.y_position+8, True)

   def death(self):
        global run_game
        if self.health_points <= 0:
            self.speed = 0
            print('GAME OVER')
            run_game = False
       
class Bomb:
    def __init__(self, x_bomb: int, y_bomb: int, boolv=False):
        self.timer = 3
        # self.explosion_range = 64
        self.x_bomb = x_bomb
        self.y_bomb = y_bomb
        self.bomb_height = 16
        self.bomb_width = 16
        self.isSet = boolv
        self.collisional = 0
        self.bomb_rect = pygame.Rect(
            self.x_bomb, self.y_bomb, self.bomb_height, self.bomb_width)

    def explode(self):
        global bomb_count, wybuch
        if bomb_count == 62: 
            self.timer -= 1
            bomb_count = 0
        if not self.timer:
            self.timer = 3
            self.isSet = False
            wybuch = Explosion(self.x_bomb-56, self.y_bomb-56, True)

class Explosion:
    def __init__(self, x: int, y: int, boolv=False):
        self.range = 64
        self.x = x  
        self.y = y 
        self.exists = boolv
        self.collisional = 1
        self.expl_rect = pygame.Rect(self.x, self.y, 128, 128)

    def vaporize(self):
        global expl_count
        if expl_count == 31:
            self.exists = False
            expl_count = 0


def ruchy_gracz():
    gracz.move()
    gracz.attack()
    if gracz.attack() and keys[pygame.K_LSHIFT]:
        gracz.throw_sword()
    gracz.place_bomb()

    
def player_wall_collision():
    global currentLevel
    for wall in walls:
        if gracz.rectangle.colliderect(wall):
            if keys[pygame.K_UP]:
                gracz.y_position += gracz.speed
                gracz.rectangle.y += gracz.speed
            if keys[pygame.K_LEFT]:
                gracz.x_position += gracz.speed
                gracz.rectangle.x += gracz.speed
            if keys[pygame.K_DOWN]:
                gracz.rectangle.y -= gracz.speed
                gracz.y_position -= gracz.speed
            if keys[pygame.K_RIGHT]:
                gracz.rectangle.x -= gracz.speed
                gracz.x_position -= gracz.speed
    if currentLevel < 2:
        if gracz.rectangle.colliderect(finishes[0]):
            currentLevel += 1
            for wall in walls:
                walls.remove(wall)
            for oponent in lista_potworow:
                lista_potworow.remove(oponent)
            for pocisk in lista_pociskow:
                lista_pociskow.remove(pocisk)
            load_level(currentLevel)
            if currentLevel < 2:
                oponent_spawn()
            else:
                spawn_boss()
            
            
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


bomba = Bomb(-100, -100)
wybuch = Explosion(-100, -100)

gracz_im_timer = 0
licznik = 0
bomb_count = 0
expl_count = 0

run_game = True
load_level(currentLevel)
while run_game:
    settings()

    exit()

