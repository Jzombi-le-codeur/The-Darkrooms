import pygame

class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Assets\Images\Items\gun.png")
        self.attack = 10
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
