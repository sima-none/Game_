import pygame
import random

class Cell:
    def __init__(self, belong, x, y, color=(89, 2, 78)):
        self.color = color
        self.belong = belong
        self.x = x
        self.y = y
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * 8, self.y * 8, 8, 8))
class Creature:
    def __init__(self, cells=None):
        self.cells = cells if cells != None else []
    def add_cells(self, number):
        for _ in range(number):
            x = random.randint(0, 256 // 2) #
            y = random.randint(0, 192 // 2) #
            cell = Cell(self, x, y)
            self.cells.append(cell)
    def draw(self, screen):
        for cell in self.cells:
            cell.draw(screen)