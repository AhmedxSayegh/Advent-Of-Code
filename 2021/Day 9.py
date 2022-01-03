content = open('Input.txt').read().split('\n')
grid = [list(line) for line in content]
grid_size_xy = [len(grid[0]) - 1, len(grid) - 1]


# Used By Both Parts
def not_on_edge_checker(position, pos_id):
    if pos_id == 'x':
        if int(position) == 0 or int(position) == grid_size_xy[0]:
            return True
    else:
        if position == 0 or position == grid_size_xy[1]:
            return True


# Part 1
def nearby_checker(x, y):
    x_status = False
    y_status = False
    if not not_on_edge_checker(x, 'x'):
        x_status = True if grid[y][x - 1] > grid[y][x] < grid[y][x + 1] else False
    else:
        x_status = True if grid[y][abs(x - 1)] > grid[y][x] else False
    if not not_on_edge_checker(y, 'y'):
        y_status = True if grid[y - 1][x] > grid[y][x] < grid[y + 1][x] else False
    else:
        y_status = True if grid[abs(y - 1)][x] > grid[y][x] else False
    if all([x_status, y_status]):
        return True


low_points = []
total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if nearby_checker(x, y):
            total += int(grid[y][x]) + 1
            low_points.append([x, y])
print('Part 1 Answer:', total)


# Part 2
def basin_checker(x, y):
    global total
    total += 1
    xy_id[x, y] = False
    if not not_on_edge_checker(x, 'x'):
        if int(grid[y][x + 1]) < 9 and xy_id.get((x + 1, y), True):
            basin_checker(x + 1, y)
        if int(grid[y][x - 1]) < 9 and xy_id.get((x - 1, y), True):
            basin_checker(x - 1, y)
    if not not_on_edge_checker(y, 'y'):
        if int(grid[y + 1][x]) < 9 and xy_id.get((x, y + 1), True):
            basin_checker(x, y + 1)
        if int(grid[y - 1][x]) < 9 and xy_id.get((x, y - 1), True):
            basin_checker(x, y - 1)
    if int(grid[y][abs(x - 1)]) < 9 and xy_id.get((abs(x - 1), y), True):
        basin_checker(abs(x - 1), y)
    if int(grid[abs(y - 1)][x]) < 9 and xy_id.get((x, abs(y - 1)), True):
        basin_checker(x, abs(y - 1))


basins = []
total = 0
xy_id = {}
for low_point in low_points:
    xy_id.clear()
    total = 0
    basin_checker(low_point[0], low_point[1])
    basins.append(total)
basins.sort(reverse=True)
print('Part 2 Answer:', basins[0] * basins[1] * basins[2])
