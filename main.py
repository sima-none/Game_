import pygame
import random
from classes import Creature

pygame.init()
screen = pygame.display.set_mode((1024, 768))  # создаём окно 1280×720


creature1 = Creature()
creature1.add_cells(3)

pygame.draw.rect(screen, (89, 27, 78), (686, 80, 8, 8))  # квадрат
creature1.draw(screen)
pygame.display.flip()  # обновляем экран


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()