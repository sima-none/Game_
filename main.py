import pygame
import random
from config import all_creatures, grid, alive_creatures
from classes import Creature
from giving_birth_func import give_birth
from grid_func import update_the_grid
from main_functions import new_simulation

pygame.init()
screen = pygame.display.set_mode((1024, 768))  # создаём окно 1024 на 768. Поле состоит из 128 на 96 пустых клеток
clock = pygame.time.Clock()

quantity, frequency = (3,5), 0
give_birth(quantity, frequency) # Создаём 10 Creatures, 32 Cells. РАНДОМ В НУЛЯХ. Можно передавать списк

print(len(all_creatures), "creatures were born")
print()
print("The creatures have the folowing rules:")
print()

# рисую всех существ
for i in range(len(all_creatures)):
    creature = all_creatures[i]
    if len(creature.cells) == 0 and creature in alive_creatures:
        print("Creature №", all_creatures.index(creature) + 1, "died")
        print()
        alive_creatures.remove(creature)
    else:
        creature.draw(screen)
        creature.print_rules()
pygame.display.flip()  # обновляем экран
clock.tick(10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                all_creatures.clear()
                alive_creatures.clear()
                new_simulation(screen, clock, all_creatures, quantity, frequency)
            elif event.key == pygame.K_LEFT:
                alive_creatures.clear()
                alive_creatures.extend(all_creatures)
                new_simulation(screen, clock, all_creatures, quantity, frequency)
    print("Pr", grid[0][5], all_creatures, alive_creatures)
    update_the_grid()
    screen.fill((0, 0, 0))
    for i in range(len(all_creatures)):
        creature = all_creatures[i]
        if len(creature.cells) == 0 and creature in alive_creatures:
            print("Creature №", all_creatures.index(creature) + 1, "died")
            print()
            alive_creatures.remove(creature)
        else:
            creature.draw(screen)
    pygame.display.flip()
    clock.tick(10)
    
pygame.quit()