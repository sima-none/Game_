import pygame
import random
from config import all_creatures, grid, alive_creatures, create_grid
from classes import Creature
from giving_birth_func import give_birth
from grid_func import update_the_grid
from main_functions import new_simulation, save_creature, saved_creatures


pygame.init()
screen = pygame.display.set_mode((1024, 768))  # создаём окно 1024 на 768. Поле состоит из 128 на 96 пустых клеток
clock = pygame.time.Clock()

quantity, frequency, lightnesses = 3, 0, [30, 80, 130]
give_birth(quantity, frequency, lightnesses) # Создаём 10 Creatures, 32 Cells. РАНДОМ В НУЛЯХ. Можно передавать списки

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
selection_mode, run_new = "selection_mode", "run_new"
mode = run_new
while running:
    for event in pygame.event.get():
        if mode == run_new:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    all_creatures.clear()
                    alive_creatures.clear()
                    new_simulation(screen, clock, all_creatures, quantity, frequency, lightnesses)
                elif event.key == pygame.K_LEFT:
                    alive_creatures.clear()
                    alive_creatures.extend(all_creatures)
                    new_simulation(screen, clock, all_creatures, quantity, frequency, lightnesses)
                elif event.key == pygame.K_RETURN:
                    print("Rules:")
                    for creature in alive_creatures:
                        creature.print_rules()
                        save_creature(creature)
                    print()
                elif event.key == pygame.K_SPACE:
                    mode = selection_mode
                    screen.fill((0,0,0))
                    for creature in all_creatures:
                        creature.draw_birth_rectangle(screen)
        elif mode == selection_mode:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mode = run_new
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for creature in all_creatures:
                    rect = pygame.Rect(creature.x * 8, creature.y * 8, 64, 64)
                    if rect.collidepoint(mouse_x, mouse_y):
                        save_creature(creature)
                        print(f"Creature at ({creature.x}, {creature.y}) saved!")
                        print(" Their rules:")
                        creature.print_rules()
                        break
    if mode == run_new:
        update_the_grid()
        screen.fill((0,0,0))
        for i in range(len(all_creatures)):
            creature = all_creatures[i]
            if len(creature.cells) == 0 and creature in alive_creatures:
                print("Creature №", all_creatures.index(creature) + 1, "died")
                print()
                alive_creatures.remove(creature)
            else:
                creature.draw(screen)
    '''elif mode == selection_mode:
    '''
    pygame.display.flip()
    clock.tick(10)
pygame.quit()