import pygame

pygame.init()
screenWidth = 500
screenHeight = 500

class Player:
    def __init__(self):
       self.speed = 3
        self.sword_length = 0  # 48
        self.sword_width = 0  # 16
        self.health_points = 100
        self.attack_points = 25
        self.height = 32
        self.width = 32
        self.x_position = 50
        self.y_position = 50
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
           self.sword_width = 16
           self.sword_length = 48
           self.x_sword = self.x_position - self.sword_length
           self.y_sword = self.y_position + 0.25*self.height
           self.sword_rect = pygame.Rect(self.x_sword,
                                         self.y_sword,
                                         self.sword_length, self.sword_width)
           self.sword_exists = 1
           return True
           
       elif keys[pygame.K_d]:
           self.sword_width = 16
           self.sword_length = 48
           self.x_sword = self.x_position + self.width
           self.y_sword = self.y_position + 0.25*self.width
           self.sword_rect = pygame.Rect(self.x_sword,
                                         self.y_sword,
                                         self.sword_length, self.sword_width)
           self.sword_exists = 1
           return True
           
       elif keys[pygame.K_w]:
           self.sword_width = 48
           self.sword_length = 16
           self.x_sword = self.x_position + 0.25*self.height
           self.y_sword = self.y_position - self.sword_width
           self.sword_rect = pygame.Rect(self.x_sword,
                                         self.y_sword,
                                         self.sword_length, self.sword_width)
           self.sword_exists = 1
           return True
           
       elif keys[pygame.K_s]:
           self.sword_width = 48
           self.sword_length = 16
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
        if self.health_points <= 0:
            print('GAME OVER')
       
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
        if bomb_count == 62:  # to wychodzi 992 ms, więc prawie jak sekunda
            self.timer -= 1
            bomb_count = 0
        if not self.timer:
            self.timer = 3
            self.isSet = False
            wybuch = Explosion(self.x_bomb-56, self.y_bomb-56, True)

class Explosion:
    def __init__(self, x: int, y: int, boolv=False):
        self.range = 64
        self.x = x  # tutaj trzeba policzyć tak żeby to jakoś miało sens
        self.y = y  # tutaj też
        self.exists = boolv
        self.collisional = 1
        self.expl_rect = pygame.Rect(self.x, self.y, 128, 128)

    def vaporize(self):
        global expl_count
        if expl_count == 31:
            self.exists = False
            expl_count = 0
