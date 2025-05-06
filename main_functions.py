from config import all_creatures, grid, alive_creatures
from giving_birth_func import give_birth


def new_simulation(screen, clock, current_creatures=None, quantity=0, frequency=0):
    for y in range(96):
            for x in range(128):
                grid[y][x] = 0
    if current_creatures:
        for creature in current_creatures:
            creature.cells.clear()
            creature.add_cells(frequency)
        print("\nNew variation:")
    else:
        give_birth(quantity, frequency)
        print("\nNew generation:")
        print(len(all_creatures), "creatures were born")

    for i in range(len(all_creatures)):
        creature = all_creatures[i]
        if len(creature.cells) == 0 and creature in alive_creatures:
            print("Creature №", all_creatures.index(creature) + 1, "died")
            print()
            alive_creatures.remove(creature)
        else:
            creature.draw(screen)
            creature.print_rules()
    clock.tick(10)