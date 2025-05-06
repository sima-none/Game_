import pygame
import random
import cv2
import numpy as np
from config import grid, all_rules, all_rules_without_zeros

class Cell:
    def __init__(self, owner, x, y, color=50):
        self.owner = owner
        self.x = x
        self.y = y
        self.color = color
        self.rule = self.owner.rules[self.color]
        grid[y][x] = self
    def draw(self, screen):
        hls_color = np.uint8([[[self.owner.own_color, self.color, self.color]]])
        bgr_color = cv2.cvtColor(hls_color, cv2.COLOR_HLS2BGR)[0][0]
        rgb_color = (int(bgr_color[2]), int(bgr_color[1]), int(bgr_color[0]))
        pygame.draw.rect(screen, rgb_color, (self.x * 8, self.y * 8, 8, 8))
'''(89, 2, 78)'''
class Creature:
    def __init__(self, x, y, own_color=None, cells=None):
        self.x = x
        self.y = y
        self.cells = cells if cells != None else []
        self.own_color = own_color if own_color != None else random.randint(0,179)
        self.rules = dict()
    def add_cells(self, number):
        if type(number) != int:
            number = random.randint(number[0],number[1])
        if number == 0:
            number = random.randint(1,64)
        lightness_chance = random.randint(1,64)
        for x in range(8):
            for y in range(8):
                if random.randint(1, 64) <= number:
                    if random.randint(1, 64) <= lightness_chance:
                        cell = Cell(self, (self.x + x) % 128, (self.y + y) % 96, 120)
                        self.cells.append(cell)
                    else:
                        cell = Cell(self, (self.x + x) % 128, (self.y + y) % 96, 50)
                        self.cells.append(cell)
    def add_rules(self, colors=[50, 120]):
        for color in colors:
            self.rules[color] = Rule()
    def draw(self, screen):
        for cell in self.cells:
            cell.draw(screen)
    def print_rules(self):
        for rule in self.rules:
            print("Lightness is", rule)
            rule = self.rules[rule]
            print('survives with', rule.exist_with)
            print('survives color', rule.exist_color)
            print('born with', rule.nonexist_with)
            print('born color', rule.nonexist_color)
            print()

class Rule:
    def __init__(self):
        self.exist_with = all_rules_without_zeros[random.randint(0, 35)]
        self.exist_color = all_rules[random.randint(0, 44)]
        self.nonexist_with = all_rules_without_zeros[random.randint(0, 35)]
        self.nonexist_color = all_rules[random.randint(0, 44)]