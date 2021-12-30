content = [int(x) for x in open('Input.txt').read().split(',')]
positions = {}

# Part 1
for position in content:
    positions[position] = sum(list(map(lambda x: abs(position - x), content)))
print('Part 1 Answer:', int(min(list(positions.values()))))

# Part 2
for position in content:
    positions[position] = sum(list(map(lambda x: abs(position - x) * (abs(position - x) + 1) / 2, content)))
print('Part 2 Answer:', int(min(list(positions.values()))))
