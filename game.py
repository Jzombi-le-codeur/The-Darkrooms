import pygame
from player import Player
from gun import Gun

class Game:
    def __init__(self):
        self.player = Player()
        self.gun = Gun()
        self.all_guns = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_items()

    def spawn_items(self):
        self.gun.rect.x = 500
        self.gun.rect.y = 750
        self.all_guns.add()
