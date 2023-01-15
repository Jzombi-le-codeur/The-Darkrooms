import pygame
from game import Game
import sys

pygame.init()

screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("THE DARKROOMS")
infos = pygame.display.Info()
game = Game()

running = True
while running:
    background = pygame.image.load("Assets\Images\Scenes\Level 1\main.png")
    screen.blit(background, (0, 0))
    screen.blit(game.player.image, (game.player.rect.x, game.player.rect.y))
    game.all_guns.draw(screen)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()

    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_ESCAPE:
                running = False

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.flip()
