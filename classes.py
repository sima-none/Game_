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
        self.owner.alive_colors[self.color] += 1
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
        self.alive_colors = dict()
    def add_rules(self, colors=[50]):
        for color in colors:
            self.rules[color] = Rule()
            self.colors = colors
            self.alive_colors[color] = 0
    def add_cells(self, live_chance):
        if type(live_chance) != int:
            live_chance = random.randint(live_chance[0],live_chance[1])
        elif live_chance == 0:
            live_chance = random.randint(1,64)
        lightness_weights = []
        for _ in self.colors:
            lightness_weights.append(random.randint(1, 64))
        for x in range(8):
            for y in range(8):
                if random.randint(1,64) <= live_chance:
                    color = random.choices(self.colors, weights=lightness_weights, k=1)[0]
                    cell = Cell(self, (self.x + x) % 128, (self.y + y) % 96, color)
                    self.cells.append(cell)
                '''
                if random.randint(1, 64) <= lightness_chance:
                    cell = Cell(self, (self.x + x) % 128, (self.y + y) % 96, 120)
                    self.cells.append(cell)
                else:
                    cell = Cell(self, (self.x + x) % 128, (self.y + y) % 96, 50)
                    self.cells.append(cell)
                '''
    def draw(self, screen):
        for cell in self.cells:
            cell.draw(screen)
    def print_rules(self):
        rules_list = list(self.rules.items())
        for i in range(0, len(rules_list), 2):
            left_lightness, left_rule = rules_list[i]
            left_lines = [
                f"survives with {left_rule.exist_with}",
                f"survives color {left_rule.exist_color}",
                f"born with {left_rule.nonexist_with}",
                f"born color {left_rule.nonexist_color}"
            ]

            if i + 1 < len(rules_list):
                right_lightness, right_rule = rules_list[i + 1]
                right_lines = [
                    f"survives with {right_rule.exist_with}",
                    f"survives color {right_rule.exist_color}",
                    f"born with {right_rule.nonexist_with}",
                    f"born color {right_rule.nonexist_color}"
                ]
            else:
                right_lines = [""] * 4

            for left, right in zip(left_lines, right_lines):
                print(f"{left:<40} {right}")
            print()
    def draw_birth_rectangle(self, screen):
        for x in range(8):
            for y in range(8):
                color = self.colors[random.randint(0, len(self.colors)-1)]
                hls_color = np.uint8([[[self.own_color, color, 100]]])
                bgr_color = cv2.cvtColor(hls_color, cv2.COLOR_HLS2BGR)[0][0]
                rgb_color = (int(bgr_color[2]), int(bgr_color[1]), int(bgr_color[0]))
                pygame.draw.rect(screen, rgb_color, ((self.x + x) % 128 * 8, (self.y + y) % 96 * 8, 8, 8))



class Rule:
    def __init__(self):
        self.exist_with = all_rules_without_zeros[random.randint(0, 35)]
        self.exist_color = all_rules[random.randint(0, 44)]
        self.nonexist_with = all_rules_without_zeros[random.randint(0, 35)]
        self.nonexist_color = all_rules[random.randint(0, 44)]