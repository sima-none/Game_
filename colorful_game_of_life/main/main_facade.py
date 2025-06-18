import pygame
from colorful_game_of_life.config import all_creatures, alive_creatures
from colorful_game_of_life.functions.giving_birth_func import give_birth
from colorful_game_of_life.functions.grid_func import update_the_grid
from colorful_game_of_life.main.main_functions import new_simulation, save_creature

class GameManager:
    def __init__(self, screen, clock, quantity, frequency, lightnesses):
        self.screen = screen
        self.clock = clock
        self.quantity = quantity
        self.frequency = frequency
        self.lightnesses = lightnesses
        
        self.selection_mode = "selection_mode"
        self.run_new = "run_new"
        self.mode = self.run_new

    def setup(self):
        # Создаём существ
        give_birth(self.quantity, self.frequency, self.lightnesses)
        print(len(all_creatures), "creatures were born\n")
        print("The creatures have the following rules:\n")
        self.draw_creatures_initial()

    def draw_creatures_initial(self):
        for creature in list(all_creatures):
            if len(creature.cells) == 0 and creature in alive_creatures:
                print(f"Creature №{all_creatures.index(creature) + 1} died\n")
                alive_creatures.remove(creature)
            else:
                creature.draw(self.screen)
                creature.print_rules()

    def handle_events(self):
        for event in pygame.event.get():
            if self.mode == self.run_new:
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        all_creatures.clear()
                        alive_creatures.clear()
                        new_simulation(self.screen, self.clock, all_creatures, self.quantity, self.frequency, self.lightnesses)
                    elif event.key == pygame.K_LEFT:
                        alive_creatures.clear()
                        alive_creatures.extend(all_creatures)
                        new_simulation(self.screen, self.clock, all_creatures, self.quantity, self.frequency, self.lightnesses)
                    elif event.key == pygame.K_RETURN:
                        print("Rules:")
                        for creature in alive_creatures:
                            creature.print_rules()
                            save_creature(creature)
                        print()
                    elif event.key == pygame.K_SPACE:
                        self.mode = self.selection_mode
                        self.screen.fill((0,0,0))
                        for creature in all_creatures:
                            creature.draw_birth_rectangle(self.screen)
            elif self.mode == self.selection_mode:
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.mode = self.run_new
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    for creature in all_creatures:
                        rect = pygame.Rect(creature.x * 8, creature.y * 8, 64, 64)
                        if rect.collidepoint(mouse_x, mouse_y):
                            save_creature(creature)
                            print(f"Creature at ({creature.x}, {creature.y}) saved!")
                            print(" Their rules:")
                            creature.print_rules()
                            break
        return True

    def update(self):
        if self.mode == self.run_new:
            update_the_grid()

    def draw(self):
        if self.mode == self.run_new:
            self.screen.fill((0,0,0))
            for creature in list(all_creatures):
                if len(creature.cells) == 0 and creature in alive_creatures:
                    print(f"Creature №{all_creatures.index(creature) + 1} died\n")
                    alive_creatures.remove(creature)
                else:
                    creature.draw(self.screen)
