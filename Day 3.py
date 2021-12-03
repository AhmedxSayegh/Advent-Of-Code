content = open('Text.txt').read().split('\n')

def binary_to_dicimal(num):
    dicimal = 0
    for count, digit in enumerate(num):
        dicimal += int(digit)*2**(len(num)-count-1)
    return dicimal

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
epsilon_rate = ''.join(list(map(lambda x: '1' if x is '0' else '0', gamma_rate)))
print('Part 1 Answer:', binary_to_dicimal(gamma_rate)*binary_to_dicimal(epsilon_rate))

# Part 2
def ox_rating(report, index):
    global ox
    if len(report) == 1:
        ox = report[0]
        return
    else:
        zero_counter = 0
        one_counter = 0
        for y in range(len(report)):
            if report[y][index] == '1':
                one_counter += 1
            else:
                zero_counter += 1
        if one_counter >= zero_counter:
            ox_counter = list(filter(lambda xreport: xreport[index] == '1', report))
        else:
            ox_counter = list(filter(lambda xreport: xreport[index] == '0', report))
        index += 1
        ox_rating(ox_counter, index)
def co2_rating(report, index):
    global co2
    if len(report) == 1:
        co2 = report[0]
        return
    else:
        zero_counter = 0
        one_counter = 0
        for y in range(len(report)):
            if report[y][index] == '1':
                one_counter += 1
            else:
                zero_counter += 1
        if one_counter < zero_counter:
            co2_counter = list(filter(lambda xreport: xreport[index] == '1', report))
        else:
            co2_counter = list(filter(lambda xreport: xreport[index] == '0', report))
        index += 1
        co2_rating(co2_counter, index)
ox_rating(content, 0)
co2_rating(content, 0)
print('Part 2 Answer:', binary_to_dicimal(ox)*binary_to_dicimal(co2))
