# обновление одной клетки
def update_cell(grid, length, i, j):
    neighbors = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if not (0 <= x < len(grid[0]) and 0 <= y < length):
                continue
            neighbors += grid[x][y]
    if grid[i][j] == 1:
        return 1 if neighbors in [2, 3] else 0
    else:
        return 1 if neighbors == 4 else 0
