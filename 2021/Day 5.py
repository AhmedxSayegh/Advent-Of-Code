from math import fabs

content = open('Input.txt').read().split('\n')


# Used By Both Parts
def result(grid):
    counter = 0
    for row in grid:
        for column in row:
            if column > 1:
                counter += 1
    return counter


xy1 = []
xy2 = []
for instruction in content:
    xy1.append([int(instruction.split(',')[0]), int(instruction.split()[0].split(',')[-1])])
    xy2.append([int(instruction.split()[-1].split(',')[0]), int(instruction.split(',')[-1])])
grid_size = max(max(max(xy1[i]) for i in range(len(content))), max(max(xy2[i]) for i in range(len(content))))
grid = [[0 for i in range(grid_size + 1)] for i in range(grid_size + 1)]

# Part 1
for i in range(len(xy1)):
    if xy1[i][0] == xy2[i][0]:
        for o in range(min([xy1[i][1], xy2[i][1]]), max([xy1[i][1], xy2[i][1]]) + 1):
            grid[o][xy1[i][0]] += 1
    elif xy1[i][1] == xy2[i][1]:
        for o in range(min(xy1[i][0], xy2[i][0]), max(xy1[i][0], xy2[i][0]) + 1):
            grid[xy1[i][1]][o] += 1
print('Part 1 Answer:', result(grid))

# Part 2
for i in range(len(xy1)):
    if fabs(xy1[i][0] - xy2[i][0]) == fabs(xy1[i][1] - xy2[i][1]):
        for o in range(int(fabs(xy1[i][0] - xy2[i][0]) + 1)):
            if sum(xy1[i]) > sum(xy2[i]):
                grid[xy1[i][1] - o][xy1[i][0] - o] += 1
            elif sum(xy1[i]) < sum(xy2[i]):
                grid[xy1[i][1] + o][xy1[i][0] + o] += 1
            else:
                grid[max(xy1[i][1], xy2[i][1]) - o][min(xy1[i][0], xy2[i][0]) + o] += 1
print('Part 2 Answer:', result(grid))
