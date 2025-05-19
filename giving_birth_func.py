import random
from classes import Creature
from config import all_creatures, alive_creatures

def give_birth(number = 10, fullness = 32, colors = [50, 120]):
    if type(number) != int:
        number = random.randint(number[0], number[1])
    if number == 0:
        number = random.randint(2, 24)

    if 0 in colors:
        for i in range(len(colors)):
            colors[i] = random.randint(2,24) * 10
    colors = list(set(colors))
    # создаю 10 Creatures в отдельных местах рождения. У них 64 клетки для рапределения Cells

    birth_rectangles = []

    for _ in range(number): # создаю 10 мест рождения

        random_x = random.randint(0, 127)
        random_y = random.randint(0, 95)
        one_rectangle = [random_x, random_y]

        sign = 0
        while sign == 0: # проверяем, чтобы у каждого Creature было свободное пространство
            sign = 1
            for each_rectangle in birth_rectangles:
                if min(abs(each_rectangle[0] - one_rectangle[0]), (128 - abs(each_rectangle[0] - one_rectangle[0]))) < 16:
                    if min(abs(each_rectangle[1] - one_rectangle[1]),  (96 - abs(each_rectangle[1] - one_rectangle[1]))) < 16:
                        random_x = random.randint(0, 127)
                        random_y = random.randint(0, 95)
                        one_rectangle = [random_x, random_y]
                        sign = 0
                        break
        birth_rectangles.append(one_rectangle)

    for place_of_birth in birth_rectangles: # "Рожаю" 10 Creatures
        creature = Creature(place_of_birth[0], place_of_birth[1])
        creature.add_rules(colors)
        creature.add_cells(fullness)
        all_creatures.append(creature)
        alive_creatures.append(creature)