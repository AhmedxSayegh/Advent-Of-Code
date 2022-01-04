content = open('Input.txt').read().split('\n')


# Used By Both Parts
def brackets_checker(line, index):
    if line[index] in list(opposites.values()):
        brackets_status.append(line[index])
        if len(line) > index + 1:
            brackets_checker(line, index + 1)
        else:
            incomplete_brackets.append(brackets_status)
            return
    elif line[index] in list(opposites.keys()):
        if brackets_status[-1] == opposites[line[index]]:
            brackets_status.pop()
            if len(line) > index + 1:
                brackets_checker(line, index + 1)
            else:
                incomplete_brackets.append(brackets_status)
                return
        else:
            wrong_brackets.append(line[index])
            return


wrong_brackets = []
incomplete_brackets = []
opposites = {')': '(', '}': '{', '>': '<', ']': '['}
for line in content:
    brackets_status = []
    brackets_checker(line, 0)

# Part 1
print('Part 1 Answer:',
      (wrong_brackets.count(')') * 3) + (wrong_brackets.count(']') * 57) + (wrong_brackets.count('}') * 1197) +
      (wrong_brackets.count('>') * 25137))

# Part 2
scores = []
brackets_value = {'(': 1, '[': 2, '{': 3, '<': 4}
for incomplete_line in incomplete_brackets:
    total = 0
    for bracket in incomplete_line[::-1]:
        total = total * 5 + brackets_value[bracket]
    scores.append(total)
print('Part 2 Answer:', sorted(scores)[len(scores) // 2])
