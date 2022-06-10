import pygame

pygame.init()
screenWidth = 500
screenHeight = 500

class Player:
    def __init__(self):
        self.speed = 5
        self.sword_length = 48
        self.sword_width = 16
        self.health_points = 100
        self.attack_points = 100
        self.height = 32
        self.width = 32
        self.x_position = 50
        self.y_position = 50
        self.x_sword = -500
        self.y_sword = -500
        self.throwCount = 8
    def move(self):
        if keys[pygame.K_left] and self.x_position > self.speed:
            self.x_position -= self.speed
        if keys[pygame.K_right] and self.x_position < screenWidth-self.width-self.speed:
            self.x_position += self.speed
        if keys[pygame.K_up] and self.y_position > self.speed:
            self.y_position -= self.speed
        if keys[pygame.K_down] and self.y_position < screenHeight-self.height-self.speed:
            self.y_position += self.speed
            
    def attack(self):
       if keys[pygame.K_a]:
          self.x_sword = self.x_position - self.sword.length
          self.y_sword = self.y_position - 0.25*self.width
       if keys[pygame.K_d]:
          self.x_sword = self.x_position + self.width
          self.y_sword = self.y_position - 0.25*self.width
       if keys[pygame.K_w]:
          self.x_sword = self.x_position + 0.25*self.height
          self.y_sword = self.y_position - self.sword_lenght
       if keys[pygame.K_s]:
          self.x_sword = self.x_position + 0.25*self.height
          self.y_sword = self.y_position + self.width
            
    def defense(self, enemy):
        self.health_points -= enemy
        
    def throw_sword(self):
        if self.throwCount:  
            if keys[pygame.K_a]:
                self.x_sword -= (self.throwCount**2)*0.2
            if keys[pygame.K_d]:
                self.x_sword += (self.throwCount**2)*0.2
            if keys[pygame.K_w]:
                self.y_sword -= (self.throwCount**2)*0.2
            if keys[pygame.K_s]:
                self.y_sword += (self.throwCount**2)*0.2
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
