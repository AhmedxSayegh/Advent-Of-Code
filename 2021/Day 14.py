content = open("Input.txt").read().split("\n")


# Used By Both Parts
def evalStep(pair, step):
    if not step in pairSteps[pair]:
        result = rules[pair]
        if step == 1:
            pairSteps[pair].setdefault(step, lettersCount.copy())
            pairSteps[pair][1][result] = 1
        else:
            if not step - 1 in pairSteps[pair]:
                evalStep(pair, step - 1)
            pairSteps[pair].setdefault(step, lettersCount.copy())
            pairSteps[pair][step][result] = 1
            leftChild = pair[0] + result
            rightChild = result + pair[1]
            evalStep(leftChild, step - 1)
            evalStep(rightChild, step - 1)
            for letter in pairSteps[pair][step]:
                pairSteps[pair][step][letter] += (
                    pairSteps[leftChild][step - 1][letter]
                    + pairSteps[rightChild][step - 1][letter]
                )


template = content[0]
rules = {}
pairSteps = {}
for line in content[2:]:
    pair, result = line.split(" -> ")
    rules[pair] = result
for pair in rules:
    pairSteps[pair] = {}

# Part 1
lettersCount = {i: 0 for i in rules.values()}
for index in range(len(template) - 1):
    evalStep(template[index : index + 2], 40)
for letter in template:
    lettersCount[letter] += 1
for letter in set(rules.values()):
    for index in range(len(template) - 1):
        lettersCount[letter] += pairSteps[template[index : index + 2]][10][letter]
print("Part 1 Answer:", max(lettersCount.values()) - min(lettersCount.values()))

# Part 2
lettersCount = {i: 0 for i in rules.values()}
for letter in template:
    lettersCount[letter] += 1
for letter in set(rules.values()):
    for index in range(len(template) - 1):
        lettersCount[letter] += pairSteps[template[index : index + 2]][40][letter]
print("Part 2 Answer:", max(lettersCount.values()) - min(lettersCount.values()))
