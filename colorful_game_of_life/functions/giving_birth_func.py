import random
from colorful_game_of_life.classes import Creature
from colorful_game_of_life.config import all_creatures, alive_creatures

def give_birth(number=10, fullness=32, colors=[50, 120]):
    number = normalize_number(number)
    colors = normalize_colors(colors)
    birth_rectangles = generate_birth_rectangles(number)
    create_creatures(birth_rectangles, fullness, colors)

def normalize_number(number):
    if not isinstance(number, int):
        number = random.randint(number[0], number[1])
    if number == 0:
        number = random.randint(2, 24)
    return number

def normalize_colors(colors):
    if 0 in colors:
        colors = [random.randint(2, 24) * 10 if c == 0 else c for c in colors]
    return list(set(colors))

def generate_birth_rectangles(number):
    birth_rectangles = []
    for _ in range(number):
        one_rectangle = generate_non_overlapping_rectangle(birth_rectangles)
        birth_rectangles.append(one_rectangle)
    return birth_rectangles

def generate_non_overlapping_rectangle(existing_rects):
    while True:
        x = random.randint(0, 127)
        y = random.randint(0, 95)
        if all(not is_too_close([x, y], other) for other in existing_rects):
            return [x, y]

def is_too_close(a, b, min_dist=16):
    dx = min(abs(a[0] - b[0]), 128 - abs(a[0] - b[0]))
    dy = min(abs(a[1] - b[1]), 96 - abs(a[1] - b[1]))
    return dx < min_dist and dy < min_dist

def create_creatures(birth_rectangles, fullness, colors):
    for x, y in birth_rectangles:
        creature = Creature(x, y)
        creature.add_rules(colors)
        creature.add_cells(fullness)
        all_creatures.append(creature)
        alive_creatures.append(creature)