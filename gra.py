import pygame
import random
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
        self.texture = pygame.image.load('chara.png')
        self.texture = pygame.transform.scale(self.texture, (48, 48))
        self.sword_text = pygame.image.load('swordcharacter.png')
        self.sword_text = pygame.transform.scale(self.sword_text, (24, 72))
        self.sword_90 = pygame.transform.rotate(self.sword_text, 90)
        self.sword_180 = pygame.transform.rotate(self.sword_text, 180)
        self.sword_270 = pygame.transform.rotate(self.sword_text, 270)

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
   
    def draw_player(self):
        if self.health_points > 0:
            win.blit(self.texture, (self.rectangle.x, self.rectangle.y))

    def draw_sword(self):
        if self.sword_exists:
            if keys[pygame.K_w]:
                win.blit(self.sword_text,
                         (self.sword_rect.x, self.sword_rect.y))
            if keys[pygame.K_a]:
                win.blit(self.sword_90,
                         (self.sword_rect.x, self.sword_rect.y))
            if keys[pygame.K_s]:
                win.blit(self.sword_180,
                         (self.sword_rect.x, self.sword_rect.y))
            if keys[pygame.K_d]:
                win.blit(self.sword_270,
                         (self.sword_rect.x, self.sword_rect.y))
    
    
class Bomb:
    def __init__(self, x_bomb: int, y_bomb: int, boolv=False):
        self.timer = 3
        self.x_bomb = x_bomb
        self.y_bomb = y_bomb
        self.bomb_height = 16
        self.bomb_width = 16
        self.isSet = boolv
        self.collisional = 0
        self.bomb_rect = pygame.Rect(
            self.x_bomb, self.y_bomb, self.bomb_height, self.bomb_width)
        self.texture = pygame.image.load('bomb_no.png')
        self.texture.set_colorkey((255, 255, 255))

    def explode(self):
        global bomb_count, wybuch
        if bomb_count == 62: 
            self.timer -= 1
            bomb_count = 0
        if not self.timer:
            self.timer = 3
            self.isSet = False
            wybuch = Explosion(self.x_bomb-56, self.y_bomb-56, True)
    
    def draw_bomb(self):
        if self.isSet:
            win.blit(self.texture, (self.x_bomb, self.y_bomb))

            
class Explosion:
    def __init__(self, x: int, y: int, boolv=False):
        self.range = 64
        self.x = x  
        self.y = y 
        self.exists = boolv
        self.collisional = 1
        self.expl_rect = pygame.Rect(self.x, self.y, 128, 128)
        self.texture = pygame.image.load('explosionn.png')
        self.texture = pygame.transform.scale(self.texture, (128, 128))

    def vaporize(self):
        global expl_count
        if expl_count == 31:
            self.exists = False
            expl_count = 0
    
    def draw_expl(self):
        if self.exists:
            win.blit(self.texture, (self.x, self.y))
            
            
class Potwory():
    def __init__(self):
        self.kierunek = random.randint(1, 2)
        self.walk_count = 0

    def umrzyj(self):
        global lista_potworow
        if self.pkt_zycia == 0:
            lista_potworow.remove(self)

    def movement(self):
        if self.kierunek == 1:
            self.x += self.szybkosc
            self.walk_count += 1
            if self.walk_count == 31:
                self.szybkosc = self.szybkosc*(-1)
                self.walk_count = 0
        if self.kierunek == 2:
            self.y += self.szybkosc
            self.walk_count += 1
            if self.walk_count == 31:
                self.szybkosc = self.szybkosc*(-1)
                self.walk_count = 0
        self.op_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        
class Boss(Potwory):
    def __init__(self):
        self.nazwa="Donogo"
        self.pkt_zycia=200
        self.pkt_ataku_ogniem=40
        self.szybkosc = 2
        self.x = 1000
        self.y = 383
        self.width, self.height = 72, 72
        self.op_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.wykrycie = 100000000
        self.shot_count = 1
        self.immune = False
        self.timer = 0
        self.odbicia = 0
        self.texture = pygame.image.load('bossvers2.png')
        self.texture = pygame.transform.scale(self.texture, (96, 96))

    def attack_movement(self):
        odleglosc_x = (self.x - gracz.x_position)
        odleglosc_y = (self.y - gracz.y_position)
        self.odleglosc = (odleglosc_x**2 + odleglosc_y**2)**(1/2)
        if self.odleglosc <= self.wykrycie and self.szybkosc < 0:
            self.szybkosc = self.szybkosc*(-1)
        if self.odleglosc <= self.wykrycie and self.odleglosc >= 100:
            if self.shot_count == 0:
                self.shoot()
                self.shot_count += 1
                if self.shot_count == 62:
                    self.shot_count = 0
        elif self.odleglosc < 100:
            if odleglosc_x > 0:
                self.x += self.szybkosc
                self.op_rect.x += self.szybkosc
            elif odleglosc_x < 0:
                self.x -= self.szybkosc
                self.op_rect.x -= self.szybkosc
            if odleglosc_y > 0:
                self.y += self.szybkosc
                self.op_rect.y += self.szybkosc
            elif odleglosc_y < 0:
                self.y -= self.szybkosc
                self.op_rect.y -= self.szybkosc

    def shoot(self):
      global lista_pociskow
      lista_pociskow.append(Projectile(self.x+32, self.y+32, 25, 32, 32))
    
    def draw(self):
        win.blit(self.texture, (self.x, self.y))
   
  
class Odolda(Potwory):
    def __init__(self,pozycja_x: int, pozycja_y: int):
        self.nazwa="Odolda"
        self.pkt_zycia=100
        self.atak=20
        self.szybkosc=2
        self.height, self.width = 32, 32
        self.odleglosc_od_gracza=0 
        self.promien_ataku=50
        self.x = pozycja_x
        self.y = pozycja_y
        self.kierunek = random.randint(1, 2)
        self.walk_count = 0
        self.op_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.immune = False
        self.timer = 0
        self.odbicia = 0
        self.odleglosc = 10000000
        self.texture = pygame.image.load('meleeenemy2.png')
        self.texture = pygame.transform.scale(self.texture, (48, 48))

    def attack_movement(self):
        odleglosc_x = (self.x - gracz.x_position)
        odleglosc_y = (self.y - gracz.y_position)
        self.odleglosc = (odleglosc_x**2 + odleglosc_y**2)**(1/2)
        if self.odleglosc <= self.wykrycie:
            if self.szybkosc < 0:
                self.szybkosc = self.szybkosc*(-1)
            if odleglosc_x > 0:
                self.x -= self.szybkosc
                self.op_rect.x -= self.szybkosc
            elif odleglosc_x < 0:
                self.x += self.szybkosc
                self.op_rect.x += self.szybkosc
            if odleglosc_y > 0:
                self.y -= self.szybkosc
                self.op_rect.y -= self.szybkosc
            elif odleglosc_y < 0:
                self.y += self.szybkosc
                self.op_rect.y += self.szybkosc 
    
    
class Black_Bow_Guard(Potwory): 
    def __init__(self,pozycja_x: int, pozycja_y: int):
        self.nazwa="Czarny łuk"
        self.pkt_zycia=50
        self.atak=15
        self.szybkosc=1
        self.wykrycie=400 
        self.height, self.width = 32, 32
        self.odleglosc_od_gracza=0
        self.x = pozycja_x
        self.y = pozycja_y
        self.kierunek = random.randint(1, 2)
        self.walk_count = 0
        self.op_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.immune = False
        self.timer = 0
        self.odbicia = 0
        self.odleglosc = 10000000
        self.shot_count = 1
        self.texture = pygame.image.load('arrowenemy.png')
        self.texture = pygame.transform.scale(self.texture, (48, 48))

    def attack_movement(self):
        odleglosc_x = (self.x - gracz.x_position)
        odleglosc_y = (self.y - gracz.y_position)
        self.odleglosc = (odleglosc_x**2 + odleglosc_y**2)**(1/2)
        if self.odleglosc <= self.wykrycie and self.szybkosc < 0:
            self.szybkosc = self.szybkosc*(-1)
        if self.odleglosc <= self.wykrycie and self.odleglosc >= 100:
            if self.shot_count == 0:
                self.shoot()
                self.shot_count += 1
            if self.shot_count == 62:
                self.shot_count = 0
        elif self.odleglosc < 100:
            if odleglosc_x > 0:
                self.x += self.szybkosc
                self.op_rect.x += self.szybkosc
            elif odleglosc_x < 0:
                self.x -= self.szybkosc
                self.op_rect.x -= self.szybkosc
            if odleglosc_y > 0:
                self.y += self.szybkosc
                self.op_rect.y += self.szybkosc
            elif odleglosc_y < 0:
                self.y -= self.szybkosc
                self.op_rect.y -= self.szybkosc

    def shoot(self):
        global lista_pociskow
        lista_pociskow.append(Projectile(self.x+16, self.y+16, 10, 16, 16))
  
  
class Projectile:
    def __init__(self, x: int, y: int, damage: int, length: int, height: int):
        self.x = x
        self.y = y
        self.damage = damage
        self.length = length
        self.height = height
        self.x_speed = 5
        self.y_speed = 4
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)
        self.los = random.choice([1, 2, 3, 4])
        if self.length == 16:
            self.texture = pygame.image.load('projectil.png')
            self.texture = pygame.transform.scale(self.texture, (24, 24))
        if self.length == 32:
            self.texture = pygame.image.load('fireball.png')
            self.texture = pygame.transform.scale(self.texture, (48, 48))

    def projectile_movement(self):
        if self.los == 1:
            self.x += self.x_speed
            self.rect.x += self.x_speed
        if self.los == 2:
            self.x -= self.x_speed
            self.rect.x -= self.x_speed
        if self.los == 3:
            self.y += self.y_speed
            self.rect.y += self.y_speed
        if self.los == 4:
            self.y -= self.y_speed
            self.rect.y -= self.y_speed
    
    def draw_projectile(self):
        win.blit(self.texture, (self.rect.x, self.rect.y))

      
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
            

def oponent_spawn():
    global lista_potworow 
    for i in range(1, 3):
        pozycja_x, pozycja_y = 0, 0
        check_rect = pygame.Rect(pozycja_x, pozycja_y, 32, 32)
        for k in range(len(walls)):
            for m in range(k+1):
            while check_rect.colliderect(walls[m]):
                pozycja_x = random.randint(i*320, i*640-96)
                pozycja_y = random.randint(i*180, i*360-96)
                check_rect = pygame.Rect(pozycja_x, pozycja_y, 32, 32)
        typ = random.choice([1, 2])
        if typ == 1:
            lista_potworow.append(Odolda(pozycja_x, pozycja_y))
        else:
            lista_potworow.append(Black_Bow_Guard(pozycja_x, pozycja_y))
    for j in range(1, 3):
        pozycja_x, pozycja_y = 0, 0
        check_rect = pygame.Rect(pozycja_x, pozycja_y, 32, 32)
        for k in range(len(walls)):
            for m in range(k+1):
                while check_rect.colliderect(walls[m]):
                    if j == 1:
                        pozycja_x = random.randint(0, 640)
                        pozycja_y = random.randint(360, 720-96)
                        check_rect = pygame.Rect(pozycja_x, pozycja_y, 32, 32)
                    else:
                        pozycja_x = random.randint(640, 1280-96)
                        pozycja_y = random.randint(0, 360)
                        check_rect = pygame.Rect(pozycja_x, pozycja_y, 32, 32)
        typ = random.choice([1, 2])
        if typ == 1:
            lista_potworow.append(Odolda(pozycja_x, pozycja_y))
        else:
            lista_potworow.append(Black_Bow_Guard(pozycja_x, pozycja_y))
    return True


def spawn_boss():
    global lista_potworow
    boss = Boss()
    lista_potworow.append(boss)
  
  
def oponent_walka():
    global gracz_im_timer, map
    for oponent in lista_potworow:
        if gracz.rectangle.colliderect(oponent.op_rect) and not gracz.immune:
            gracz.health_points -= oponent.atak
            gracz.death()
            gracz.immune = True
        if gracz.immune:
            gracz_im_timer += 1
            if gracz_im_timer == len(lista_potworow)*62:
                gracz_im_timer = 0
                gracz.immune = False
        if (oponent.op_rect.colliderect(gracz.sword_rect) and not oponent.immune and gracz.sword_exists):
            oponent.pkt_zycia -= gracz.attack_points
            oponent.umrzyj()
            oponent.immune = True
        if oponent.immune:
            oponent.timer += 1
            if oponent.timer == 31:
                oponent.timer = 0
                oponent.immune = False
        if oponent.op_rect.colliderect(wybuch.expl_rect) and wybuch.exists:
            oponent.pkt_zycia = 0
            oponent.umrzyj()
  
  
def ruchy_niezalezne():
    global bomb_count, expl_count
    if bomba.isSet:
        bomb_count += 1
        bomba.explode()
    if wybuch.exists:
        expl_count += 1
        wybuch.vaporize()
    for oponent in lista_potworow:
        odleglosc_x = (oponent.x - gracz.x_position)
        odleglosc_y = (oponent.y - gracz.y_position)
        oponent.odleglosc = (odleglosc_x**2 + odleglosc_y**2)**(1/2)
        if oponent.odleglosc > oponent.wykrycie:
            oponent.movement()
        elif oponent.odleglosc <= oponent.wykrycie:
            oponent.attack_movement()
    for projectile in lista_pociskow:
        projectile.projectile_movement()
    
    
def oponent_wall_collision(oponent: Potwory):
    for wall in walls:
        if oponent.op_rect.colliderect(wall):
            if oponent.odleglosc > oponent.wykrycie:
                if oponent.kierunek == 1:
                    if oponent.szybkosc > 0:
                        oponent.op_rect.x -= oponent.szybkosc
                        oponent.x -= oponent.szybkosc
                    else:
                        oponent.op_rect.x += oponent.szybkosc
                        oponent.x += oponent.szybkosc
                else:
                    if oponent.szybkosc > 0:
                        oponent.op_rect.y -= oponent.szybkosc
                        oponent.y -= oponent.szybkosc
                    else:
                        oponent.op_rect.y += oponent.szybkosc
                        oponent.y += oponent.szybkosc
            else:
                if oponent.op_rect.x > wall.x:
                    oponent.op_rect.x += oponent.szybkosc
                    oponent.x += oponent.szybkosc
                if oponent.op_rect.x < wall.x:
                    oponent.op_rect.x -= oponent.szybkosc
                    oponent.x -= oponent.szybkosc
                if oponent.op_rect.y > wall.y:
                    oponent.op_rect.y += oponent.szybkosc
                    oponent.y += oponent.szybkosc
                if oponent.op_rect.y < wall.y:
                    oponent.op_rect.y -= oponent.szybkosc
                    oponent.y -= oponent.szybkosc   

          
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


def refresh_display():
    draw_map(maps[currentLevel])
    gracz.draw_player()
    gracz.draw_sword()
    bomba.draw_bomb()
    wybuch.draw_expl()
    for oponent in lista_potworow:
        win.blit(oponent.texture, (oponent.op_rect.x, oponent.op_rect.y))
    for projectile in lista_pociskow:
        projectile.draw_projectile()
    pygame.display.update()
    
    
lista_potworow = []
oponent_spawn()

lista_pociskow = []

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
    
    ruchy_gracz()
    player_wall_collision()

    ruchy_niezalezne()
    for oponent in lista_potworow:
        oponent_wall_collision(oponent)

    walka()

    refresh_display()
    exit()
