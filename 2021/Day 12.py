content = open('Input.txt').read().split('\n')

# Used By Both Parts
caves = {}
for line in content:
    cave = line.split('-')
    if 'start' in cave:
        caves['start'] = [cave[cave.index('start') - 1]] + caves.get('start', [])
    elif 'end' in cave:
        caves[cave[cave.index('end') - 1]] = ['end'] + caves.get(cave[cave.index('end') - 1], [])
    else:
        caves[cave[0]] = [cave[1]] + caves.get(cave[0], [])
        caves[cave[1]] = [cave[0]] + caves.get(cave[1], [])


# Part 1
def path_finder(start):
    global total
    for cave in caves[start]:
        if cave == 'end':
            total += 1
        elif cave.isupper() or temp.count(cave) < 1:
            temp.append(cave)
            path_finder(cave)
            temp.pop()


total = 0
for start in caves['start']:
    temp = [start]
    path_finder(start)
print('Part 1 Answer:', total)


# Part 2
def path_finder2(start):
    global total
    for cave in caves[start]:
        if cave == 'end':
            total += 1
        elif cave.isupper() or temp.count(cave) < 1:
            temp.append(cave)
            path_finder2(cave)
            temp.pop()
        elif temp.count(cave) < 2:
            temp.append(cave)
            path_finder(cave)
            temp.pop()


total = 0
for start in caves['start']:
    temp = [start]
    path_finder2(start)
print('Part 2 Answer:', total)
