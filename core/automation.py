class Automaton:
    def __init__(self, grid, characters):
        self.grid = grid
        self.characters = characters
        self.place_characters()

    def place_characters(self):
        for char in self.characters:
            char.place_on_grid()

    def step(self):
        self.grid.update_grid()