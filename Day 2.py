content = open('Text.txt').read().split('\n')

# Part 1
ver = 0
hor = 0
for instruction in content:
    direction, value = instruction.split()[0], int(instruction.split()[-1])
    if direction.startswith('f'):
        hor += value
    elif direction.startswith('d'):
        ver += value
    else:
        ver -= value
print('Part 1 Answer:', ver*hor)

# Part 2
ver = 0
hor = 0
aim = 0
for instruction in content:
    direction, value = instruction.split()[0], int(instruction.split()[-1])
    if direction.startswith('f'):
        hor += value
        ver += aim * value
    elif direction.startswith('d'):
        aim += value
    else:
        aim -= value
print('Part 2 Answer:', ver*hor)
