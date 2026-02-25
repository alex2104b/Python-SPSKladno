import pygame
from settings import *
pygame.init()
screen = pygame.display.set_mode((500,800))
pygame.display.set_caption("uhybani")
running = True
clock = pygame.time.Clock()

from Player import Player
player = Player(250,750)
player_group = pygame.sprite.Group()
player_group.add(player)

while running:
    screen.fill((255,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_group.update()
    player_group.draw(screen)

    clock.tick(60)
    pygame.display.update()