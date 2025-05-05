import pygame
import random
from config import grid, all_rules

class Cell:
    def __init__(self, owner, x, y, color="Purple"):
        self.owner = owner
        self.x = x
        self.y = y
        self.color = color
        self.rule = self.owner.rules[self.color]
        grid[y][x] = self
    def draw(self, screen):
        pygame.draw.rect(screen, (89, 2, 78), (self.x * 8, self.y * 8, 8, 8))

class Creature:
    def __init__(self, x, y, cells=None):
        self.x = x
        self.y = y
        self.cells = cells if cells != None else []
        self.rules = dict()
    def add_cells(self, number):
        if type(number) != int:
            number = random.randint(number[0],number[1])
            print(number)
        if number == 0:
            number = random.randint(1,64)
        for x in range(8):
            for y in range(8):
                if random.randint(1, 64) <= number:
                    cell = Cell(self, (self.x + x) % 128, (self.y + y) % 96)
                    self.cells.append(cell)
    def add_rules(self, colors=["Purple"]):
        for color in colors:
            self.rules[color] = Rule()
    def draw(self, screen):
        for cell in self.cells:
            cell.draw(screen)

class Rule:
    def __init__(self):
        self.exist_with = all_rules[random.randint(0, 44)]
        self.exist_color = all_rules[random.randint(0, 44)]
        self.nonexist_with = all_rules[random.randint(0, 44)]
        self.nonexist_color = all_rules[random.randint(0, 44)]