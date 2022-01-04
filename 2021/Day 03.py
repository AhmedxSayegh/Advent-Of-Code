content = open('Input.txt').read().split('\n')

# Part 1
gamma_rate = ''
for x in range(len(content[0])):
    rate = ''
    for y in range(len(content)):
        rate += content[y][x]
    if rate.count('1') > rate.count('0'):
        gamma_rate += '1'
    else:
        gamma_rate += '0'
epsilon_rate = ''.join(list(map(lambda q: '1' if q is '0' else '0', gamma_rate)))
print('Part 1 Answer:', int(gamma_rate, 2) * int(epsilon_rate, 2))


# Part 2
def ox_rating(report, index):
    if len(report) < 2:
        return report[0]
    else:
        zero_counter = 0
        one_counter = 0
        for w in range(len(report)):
            if report[w][index] == '1':
                one_counter += 1
            else:
                zero_counter += 1
        if one_counter >= zero_counter:
            ox_counter = list(filter(lambda q: q[index] == '1', report))
        else:
            ox_counter = list(filter(lambda q: q[index] == '0', report))
        index += 1
        return ox_rating(ox_counter, index)


def co2_rating(report, index):
    if len(report) < 2:
        return report[0]
    else:
        zero_counter = 0
        one_counter = 0
        for i in range(len(report)):
            if report[i][index] == '1':
                one_counter += 1
            else:
                zero_counter += 1
        if one_counter < zero_counter:
            co2_counter = list(filter(lambda q: q[index] == '1', report))
        else:
            co2_counter = list(filter(lambda q: q[index] == '0', report))
        index += 1
        return co2_rating(co2_counter, index)


print('Part 2 Answer:', int(ox_rating(content, 0), 2) * int(co2_rating(content, 0), 2))
