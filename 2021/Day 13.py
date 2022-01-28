content = open('Input.txt').read().split('\n\n')
coordinates, folds = content[0].split('\n'), content[1].split('\n')


# Used By Both Parts
def folding(coordinates, axis, pos):
    result = []
    if axis == 'x':
        for coor in coordinates:
            x, y = coor.split(',')
            x, y = int(x), int(y)
            if x > pos:
                result.append(f'{pos - (int(x)-pos)}, {y}')
            else:
                result.append(f'{x}, {y}')
    else:
        for coor in coordinates:
            x, y = coor.split(',')
            x, y = int(x), int(y)
            if y > pos:
                result.append(f'{x}, {pos - (int(y)-pos)}')
            else:
                result.append(f'{x}, {y}')
    return list(set(result))


# Part 1
print_stopper = True
for fold in folds:
    axis, pos = fold.split()[2].split('=')
    coordinates = folding(coordinates, axis, int(pos))
    if print_stopper:
        print('Part 1 Answer:', len(coordinates))
        print_stopper = False

# Part 2
grid_size = max(int(y.split(',')[0]) for y in coordinates) + 1, max(int(x.split(',')[1]) for x in coordinates)+1
grid = [['.' for x in range(grid_size[0])] for y in range(grid_size[1])]
for coor in coordinates:
    grid[int(coor.split(',')[1])][int(coor.split(',')[0])] = '0'
print('Part 2 Answer:')
for line in grid:
    for i in line:
        if i == '0':
            print(i, end=' ')
        else:
            print(' ', end=' ')
    print()
