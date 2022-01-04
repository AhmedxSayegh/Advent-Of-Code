content = [int(x) for x in open('Input.txt').read().split(',')]


# Used By Both Parts
def fish_calculator(initial_day, num_of_days):
    days = {}
    for i in range(9):
        days[i] = initial_day.count(i)
    for i in range(num_of_days):
        temp = []
        for y in range(9):
            if not y == 6 and not y == 8:
                temp.append(days[y + 1])
            elif y == 6:
                temp.append(days[y + 1] + days[0])
            else:
                temp.append(days[0])
        for index, count in enumerate(temp):
            days[index] = count
    return sum(days.values())


# Part 1
print('Part 1 Answer:', fish_calculator(content, 80))

# Part 2
print('Part 2 Answer:', fish_calculator(content, 256))
