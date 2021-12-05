content = open('Text.txt').read().split('\n\n')

# Part 1
bingo_table = []
for table in content[1:]:
    table_list = []
    for line in table.split('\n'):
        table_list.append([int(x) for x in line.split()])
    bingo_table.append(table_list)

def table_checker(table, num):
    for x in range(len(table[0])):
        for y in range(len(table)):
            if table[y][x] == num:
                table[y][x] = 'x'
    for hor_line in table:
        if all(x == 'x' for x in hor_line):
            return [num, table]
    for x in range(len(table[0])):
        ver_line = []
        for y in range(len(table)):
            ver_line.append(table[y][x])
        if all(x == 'x' for x in ver_line):
            return [num, table]

breaker = 0
for num in content[0].split(','):
    if breaker == 1:
        break
    for table in bingo_table:
        answer = table_checker(table, int(num))
        if answer != None:
            answer_list = []
            for row in answer[1]:
                for var in row:
                    if var != 'x':
                        answer_list.append(var)
            print('Part 1 Answer:', answer[0]*sum(answer_list))
            breaker += 1
            break

# Part 2
bingo_table = []
bingo_table_copy = []
for table in content[1:]:
    table_list = []
    for line in table.split('\n'):
        table_list.append([int(x) for x in line.split()])
    bingo_table.append(table_list)
    bingo_table_copy.append(table_list)

def table_checker(table, num, table_id):
    for x in range(len(table[0])):
        for y in range(len(table)):
            if table[y][x] == num:
                table[y][x] = 'x'
    for hor_line in table:
        if all(x == 'x' for x in hor_line):
            return [num, table, table_id]
    for x in range(len(table[0])):
        ver_line = []
        for y in range(len(table)):
            ver_line.append(table[y][x])
        if all(x == 'x' for x in ver_line):
            return [num, table, table_id]

breaker = 0
list_of_answers = []
for num in content[0].split(','):
    if breaker == 1:
        break
    for count, table in enumerate(bingo_table):
        if all(x == [] for x in bingo_table_copy):
            breaker += 1
            break
        answer = table_checker(table, int(num), count)
        if answer != None:
            answer_table = [x for x in bingo_table_copy]
            answer_num = int(num)
            bingo_table_copy[answer[-1]] = []

answer = 0
for table in answer_table:
    for line in table:
        answer += sum((list(filter(lambda x: str(x).isdigit(), line))))
print('Part 2 Answer:', answer*answer_num)