from config import all_creatures, grid, alive_creatures
from classes import Cell

HEIGHT = 96
WIDTH = 128


def update_the_grid():
    old_grid = copy_grid(grid)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            cell = old_grid[y][x]
            if cell:
                process_existing_cell(x, y, cell, old_grid)
            else:
                process_empty_cell(x, y, old_grid)


def copy_grid(original_grid):
    return [row[:] for row in original_grid]


def process_existing_cell(x, y, cell, old_grid):
    my_color, my_neighbours = 0, 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            neighbor = old_grid[(y + dy) % HEIGHT][(x + dx) % WIDTH]
            if neighbor and neighbor != cell:
                if neighbor.owner == cell.owner:
                    my_neighbours += 1
                else:
                    my_neighbours -= 1
                if neighbor.color == cell.color:
                    my_color += 1

    if not (my_neighbours in cell.rule.exist_with and my_color in cell.rule.exist_color):
        grid[y][x] = 0
        cell.owner.cells.remove(cell)


def process_empty_cell(x, y, old_grid):
    neighbouring_cells = [0 for _ in alive_creatures]
    neighbouring_colors = {}

    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            neighbor = old_grid[(y + dy) % HEIGHT][(x + dx) % WIDTH]
            if neighbor:
                index = alive_creatures.index(neighbor.owner)
                neighbouring_cells[index] += 1
                if neighbor.color in neighbouring_colors:
                    neighbouring_colors[neighbor.color] += 1
                else:
                    neighbouring_colors[neighbor.color] = 1

    potential_parents = find_potential_parents(neighbouring_cells, neighbouring_colors)

    if len(potential_parents) == 1:
        creature, color = potential_parents[0]
        creature.cells.append(Cell(creature, x, y, color))


def find_potential_parents(neighbouring_cells, neighbouring_colors):
    potential_parents = []
    for color, color_count in neighbouring_colors.items():
        for i, creature in enumerate(alive_creatures):
            rule = creature.rules[color]
            if neighbouring_cells[i] in rule.nonexist_with and color_count in rule.nonexist_color:
                potential_parents.append([creature, color])
    return potential_parents
