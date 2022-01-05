content = open('Input.txt').read().split('\n')


# Used By Both Parts
class Octopus:
    def __init__(self, x_pos, y_pos, energy):
        self.x, self.y, self.energy, self.around, self.flash_id, = x_pos, y_pos, energy, [], True
        for func in around:
            self.around.append(func(self.x, self.y))

    def step(self):
        global flashes, flashes_total
        if self.energy == 9:
            flashes_total += 1
            flashes.append([self.x, self.y])
            self.energy = 0
            self.flash_id = False
        else:
            self.energy += 1
            self.flash_id = True

    def flash_step(self):
        global flashes_total
        if self.flash_id is not False:
            if self.energy == 9:
                flashes_total += 1
                self.energy = 0
                self.flash_id = False
                flash_around(self.x, self.y)
            else:
                self.energy += 1


def flash_around(x, y):
    for position in octopuses[y][x].around:
        if position is not False:
            octopuses[position[1]][position[0]].flash_step()


around = [lambda x, y: [x + 1, y] if x + 1 <= len(content[0]) - 1 else False,
          lambda x, y: [x + 1, y + 1] if x + 1 <= len(content[0]) - 1 and y + 1 <= len(content) - 1 else False,
          lambda x, y: [x, y + 1] if y + 1 <= len(content) - 1 else False,
          lambda x, y: [x - 1, y + 1] if x - 1 >= 0 and y + 1 <= len(content) - 1 else False,
          lambda x, y: [x - 1, y] if x - 1 >= 0 else False,
          lambda x, y: [x - 1, y - 1] if x - 1 >= 0 and y - 1 >= 0 else False,
          lambda x, y: [x, y - 1] if y - 1 >= 0 else False,
          lambda x, y: [x + 1, y - 1] if x + 1 <= len(content[0]) - 1 and y - 1 >= 0 else False]

octopuses = [list(line) for line in content]
flashes = []
flashes_total = 0
step = 0
for y in range(len(octopuses)):
    for x in range(len(octopuses[0])):
        octopuses[y][x] = Octopus(x, y, int(octopuses[y][x]))
while True:
    step += 1
    [octopuses[y][x].step() for y in range(len(octopuses)) for x in range(len(octopuses[0]))]
    for flash in flashes:
        flash_around(flash[0], flash[1])
    flashes = []
    if step == 100:
        print('Part 1 Answer:', flashes_total)
    if len(list(filter(lambda x: x == 0, [octopuses[y][x].energy for y in range(len(octopuses)) for x in
                                          range(len(octopuses[0]))]))) == len(octopuses) * len(octopuses[0]):
        break
print('Part 2 Answer:', step)
