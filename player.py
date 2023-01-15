import pygame

class Player:
    def __init__(self):
        self.image = pygame.image.load("Assets\Images\Player\player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 750
        self.velocity = 5

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
