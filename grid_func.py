from config import all_creatures, grid
import random
from classes import Cell

def update_the_grid():
    old_grid = grid[:]
    for y in range(96):
        for x in range(128):
            me = old_grid[y][x] 
            if me:
                my_color, my_neighbours = 0, 0
                for local_y in [-1, 0, 1]:
                    for local_x in [-1, 0, 1]:
                        local = old_grid[(y + local_y) % 96][(x + local_x) % 128]
                        if local:
                            if local.owner == me.owner:
                                my_neighbours += 1
                            else:
                                my_neighbours -= 1
                            if local.color == me.color:
                                my_color += 1
                if not(my_neighbours in me.rule.exist_with and my_color in me.rule.exist_color):
                    grid[y][x] = None
                    me.owner.cells.remove(me)
            else:
                counter_of_cells = [] # Считает сколько каких клеток вокруг
                existing_colors = dict() # Словарь с цвеами и количесвом клеток
                for _ in range(len(all_creatures)):
                    counter_of_cells.append(0)
                for local_y in [-1, 0, 1]:
                    for local_x in [-1, 0, 1]:
                        local = old_grid[(y + local_y) % 96][(x + local_x) % 128]
                        if local:
                            counter_of_cells[all_creatures.index(local.owner)] += 1
                            if local.color in existing_colors:
                                existing_colors[local.color] += 1
                            else:
                                existing_colors[local.color] = 0
                like = [] # Подходящие Creaturs и colors
                for color in existing_colors: # Проходимся по цветам
                    for i in range(len(all_creatures)): # Проходимся по Creatures
                        rules = all_creatures[i].rules[color] # Правила данного цвета данного существа
                        if counter_of_cells[i] in rules.nonexist_with and existing_colors[color] in rules.nonexist_color:
                            like.append([all_creatures[i], color]) # Добавляем подходящие существа и цвета
                if len(like) > 1:
                    like = [like[random.randint(1,len(like) - 1)]]
                if len(like) != 0:
                    happy_creature = like[0][0]
                    happy_creature.cells.append(Cell(happy_creature, x, y, like[0][1]))