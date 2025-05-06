from config import all_creatures, grid, alive_creatures
from classes import Cell

def update_the_grid():
    print("Before Update", alive_creatures, all_creatures)
    old_grid = []
    for i in grid:
        old_grid.append(i[:])
    for y in range(96):
        for x in range(128):
            me = old_grid[y][x]
            if me:
                my_color, my_neighbours = 0, 0
                for local_y in [-1, 0, 1]:
                    for local_x in [-1, 0, 1]:
                        local = old_grid[(y + local_y) % 96][(x + local_x) % 128]
                        if local:
                            if local.owner == me.owner and local != me:
                                my_neighbours += 1
                            else:
                                my_neighbours -= 1
                            if local.color == me.color:
                                my_color += 1
                if not(my_neighbours in me.rule.exist_with and my_color in me.rule.exist_color):
                    grid[y][x] = 0
                    me.owner.cells.remove(me)
            else:
                neighbouring_cells = [] # Список из нулей, считает сколько клеток из живых вокруг
                neighbouring_colors = dict() # Словарь с цветами и количесвом клеток
                for _ in range(len(alive_creatures)):
                    neighbouring_cells.append(0)
                for local_y in [-1, 0, 1]:
                    for local_x in [-1, 0, 1]:
                        local = old_grid[(y + local_y) % 96][(x + local_x) % 128]
                        if local:
                            if local.owner not in alive_creatures:
                                print("Problem", local, local.owner, alive_creatures, all_creatures)
                            neighbouring_cells[alive_creatures.index(local.owner)] += 1
                            if local.color in neighbouring_colors:
                                neighbouring_colors[local.color] += 1
                            else:
                                neighbouring_colors[local.color] = 1
                potential_parents = [] # Подходящие Creaturs и colors
                for color in neighbouring_colors: # Проходимся по цветам
                    for i in range(len(neighbouring_cells)): # Проходимся по Creatures
                        current_rules = alive_creatures[i].rules[color] # Правила данного цвета данного существа
                        if neighbouring_cells[i] in current_rules.nonexist_with and neighbouring_colors[color] in current_rules.nonexist_color:
                            potential_parents.append([alive_creatures[i], color]) # Добавляем подходящие существа и цвета
                if len(potential_parents) == 1:
                    happy_creature = potential_parents[0][0]
                    if y == 0 and x in [0,1,2]:
                        happy_creature.cells.append(Cell(happy_creature, x, y, potential_parents[0][1]))
                    else:
                        happy_creature.cells.append(Cell(happy_creature, x, y, potential_parents[0][1]))