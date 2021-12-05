content = open('Text.txt').read().split('\n')
measurements = [int(i) for i in content]
total = 0
window = 0
windows = {}

# Part 1
for count, measurement in enumerate(measurements[1::]):
    if measurement > measurements[count]:
        total += 1
print('Part 1 Answer:', total)

total = 0

# Part 2
for count in range(len(measurements)):
    if count + 3 > len(measurements):
        break
    windows[window] = sum(measurements[count:count+3])
    window += 1

for i in range(1,len(windows)):
    if windows[i] > windows[i-1]:
        total += 1
print('Part 2 Answer:', total)
