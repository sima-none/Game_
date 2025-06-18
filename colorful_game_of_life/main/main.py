import pygame
from colorful_game_of_life.config import all_creatures, alive_creatures
from colorful_game_of_life.main.main_facade import GameManager

pygame.init()
screen = pygame.display.set_mode((1024, 768))  # окно 1024x768 (128x96 клеток по 8 пикселей)
clock = pygame.time.Clock()

# Параметры, которые можно менять здесь
quantity, frequency, lightnesses = 0, 0, [40, 80, 120]

# Создаём менеджер игры, передаем параметры
game_manager = GameManager(screen, clock, quantity, frequency, lightnesses)

# Инициализация — создание существ, отрисовка стартового экрана
game_manager.setup()

running = True
while running:
    
    running = game_manager.handle_events()
    game_manager.update()
    game_manager.draw()
    pygame.display.flip()
    clock.tick(10)

pygame.quit()