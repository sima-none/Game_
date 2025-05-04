import pygame
import random
from config import all_creatures, grid
from classes import Creature
from giving_birth_func import give_birth
from grid_func import update_the_grid

pygame.init()
screen = pygame.display.set_mode((1024, 768))  # создаём окно 1024 на 768. Поле состоит из 128 на 96 пустых клеток
clock = pygame.time.Clock()

give_birth(0, 0) # Создаём 10 Creatures, 32 Cells. РАНДОМ В НУЛЯХ. Можно передавать списки

# рисую всех существ
for creature in all_creatures:
    creature.draw(screen)
pygame.display.flip()  # обновляем экран


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(50)

    grid = update_the_grid(grid)
    screen.fill((0, 0, 0))
    for creature in all_creatures:
        creature.draw(screen)
    pygame.display.flip()
    
pygame.quit()