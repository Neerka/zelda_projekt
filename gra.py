import pygame

pygame.init()
screenWidth = 500
screenHeight = 500

class Player:
    def __init__(self):
        self.speed = 5
        self.health_points = 100
        self.attack_points = 100
        self.height
        self.width
        self.x_position = 50
        self.y_position = 50
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x_position > self.speed:
            self.x_position -= self.speed
        if keys[pygame.K_RIGHT] and self.x_position < screenWidth-self.width-self.speed:
            self.x_position += self.speed
        if keys[pygame.K_UP] and self.y_position > self.speed:
            self.y_position -= self.speed
        if keys[pygame.K_DOWN] and self.y_position < screenHeight-self.height-self.speed:
            self.y_position += self.speed
    def attack(self):

    def defense(self):

    def throw_sword(self):

    def set_bomb(self):
