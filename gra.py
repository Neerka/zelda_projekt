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
        self.throwCount = 
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

    def set_bomb(self):
