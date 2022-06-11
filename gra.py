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

    def set_bomb(self):
       
class Bomb:
    def __init__(self):
        self.timer = 3
        self.explosion_range = 30
        self.x_bomb = -500
        self.y_bomb = -500
        self.bomb_height = 10
        self.bomb_width = 10
        self.isSet = False

    def explode(self):
        if self.isSet = True:
            for i in range (self.timer):
                time.sleep(3)
