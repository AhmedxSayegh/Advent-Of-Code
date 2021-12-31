content = open('Input.txt').read().split('\n')

# Part 1
print('Part 1 Answer:', len(list(filter(lambda x: len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7,
                                        [output for i in range(len(content))
                                         for output in content[i].split('|')[1].split()]))))


# Part 2
def decoder(output):
    output_num = ''
    decoded = ''
    if len(output) == 2:
        return '1'
    elif len(output) == 3:
        return '7'
    elif len(output) == 4:
        return '4'
    elif len(output) == 7:
        return '8'
    else:
        for letter in output:
            output_num += str(list(encoder.keys())[list(encoder.values()).index(letter)])
        decoded = num_check(output_num)
    return decoded


def num_check(output_num):
    if all(str(x) in output_num for x in [1, 2, 4, 5, 6, 7]):
        return '0'
    elif all(str(x) in output_num for x in [1, 3, 4, 5, 6, 7]):
        return '6'
    elif all(str(x) in output_num for x in [1, 2, 3, 4, 5, 6]):
        return '9'
    elif all(str(x) in output_num for x in [1, 2, 3, 6, 7]):
        return '2'
    elif all(str(x) in output_num for x in [1, 2, 3, 5, 6]):
        return '3'
    elif all(str(x) in output_num for x in [1, 3, 4, 5, 6]):
        return '5'


inputs = {}
total = 0
for index, line in enumerate(content):
    inputs[index] = []
    encoder = {}
    for input in line.split('|')[0].split():
        inputs[index].append(input)
    zero_six_nine = [x for y in list(filter(lambda x: len(x) == 6, inputs[index])) for x in y]
    zero_six_nine = list(set(filter(lambda x: zero_six_nine.count(x) < 3, zero_six_nine)))
    two_three_five = [x for y in list(filter(lambda x: len(x) == 5, inputs[index])) for x in y]
    two_three_five = list(set(filter(lambda x: two_three_five.count(x) < 2, two_three_five)))
    one = list(filter(lambda x: len(x) == 2, inputs[index]))[0]
    four = list(filter(lambda x: len(x) == 4, inputs[index]))[0]
    seven = list(filter(lambda x: len(x) == 3, inputs[index]))[0]
    eight = list(filter(lambda x: len(x) == 7, inputs[index]))[0]
    encoder[1] = list(filter(lambda x: x not in one, seven))[0]
    encoder[2] = list(filter(lambda x: x in one, zero_six_nine))[0]
    encoder[5] = list(filter(lambda x: x not in encoder[2], one))[0]
    zero_six_nine.remove(encoder[2])
    encoder[3] = list(filter(lambda x: x in four, zero_six_nine))[0]
    zero_six_nine.remove(encoder[3])
    encoder[7] = zero_six_nine[0]
    two_three_five.remove(encoder[7])
    encoder[4] = two_three_five[0]
    encoder[6] = list(filter(lambda x: x not in list(encoder.values()), eight))[0]
    output_value = ''
    for output in line.split('|')[1].split():
        output_value += decoder(output)
    total += int(output_value)
print('Part 2 Answer:', total)
