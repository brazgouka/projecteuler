points = {}

def calc_path(grid, x, y):
    if x > len(grid) - 1 and y > len(grid[0]) - 1:
        return 0
    if x > len(grid) - 1 or y > len(grid[0]) - 1:
        return 1
    if (x, y) not in points:
        points[(x, y)] = calc_path(grid, x + 1, y) + calc_path(grid, x, y + 1)
    return points[(x, y)]

def find_path_nums(grid_size):
    grid = [[0] * grid_size] * grid_size
    return calc_path(grid, 0, 0)

print(find_path_nums(20))
