content = open('Input.txt').read().split('\n\n')


# Used By Both Parts
def table_checker(num, table, *arg):
    cycle = arg[0]
    table_id = arg[1]
    for x in range(len(table[0])):
        for y in range(len(table)):
            if table[y][x] == num:
                table[y][x] = 'x'
    for hor_line in table:
        if all(x == 'x' for x in hor_line):
            if cycle == 0:
                return [num, table]
            else:
                return [num, table, table_id]
    for x in range(len(table[0])):
        ver_line = []
        for y in range(len(table)):
            ver_line.append(table[y][x])
        if all(x == 'x' for x in ver_line):
            if cycle == 0:
                return [num, table]
            else:
                return [num, table, table_id]


bingo_tables = []
for table in content[1:]:
    table_list = []
    for line in table.split('\n'):
        table_list.append([int(x) for x in line.split()])
    bingo_tables.append(table_list)
bingo_tables_copy = [x for x in bingo_tables]

# Part 1
breaker = 0
for num in content[0].split(','):
    if breaker == 1:
        break
    for table in bingo_tables:
        answer = table_checker(int(num), table, 0, 0)
        if answer is not None:
            answer_list = []
            for row in answer[1]:
                answer_list.append(sum(list(filter(lambda x: str(x).isdigit(), row))))
            print('Part 1 Answer:', answer[0] * sum(answer_list))
            breaker += 1
            break

# Part 2
bingo_tables = [x for x in bingo_tables_copy]
breaker = 0
list_of_answers = []
for num in content[0].split(','):
    if breaker == 1:
        break
    for table_id, table in enumerate(bingo_tables):
        if all(x == [] for x in bingo_tables_copy):
            breaker += 1
            break
        answer = table_checker(int(num), table, 1, table_id)
        if answer is not None:
            answer_table = [x for x in bingo_tables_copy]
            answer_num = int(num)
            bingo_tables_copy[answer[-1]] = []
answer = 0
# noinspection PyUnboundLocalVariable
for table in answer_table:
    for line in table:
        answer += sum((list(filter(lambda x: str(x).isdigit(), line))))
# noinspection PyUnboundLocalVariable
print('Part 2 Answer:', answer * answer_num)
