const file = require("fs");
const textFile = file.readFileSync("./content.txt", "utf-8");
let test = textFile.split("\r\ninput:")[0].split("test:\r\n")[1];
let input = textFile.split("\r\ninput:\r\n")[1];
let answer;
// set the condition to 0 to get the test answer, and to 1 to get the input answer
let condition = 0;
if (condition) {
    content = input;
} else {
    content = test;
}

// part 1
class Monkey {
    constructor({ name, items, operation, test }) {
        this.name = name;
        this.items = items;
        this.operation = function (value) {
            if (operation.value == "old") {
                return operation.operator == "+" ? value + value : value * value;
            } else {
                return operation.operator == "+"
                    ? value + parseInt(operation.value)
                    : value * parseInt(operation.value);
            }
        };
        this.test = test;
        this.inspectedTimes = 0;
    }

    inspect(divide) {
        this.items.map((item) => {
            this.inspectedTimes++;
            if (divide) {
                item = Math.floor(this.operation(item) / 3);
            } else {
                item = this.operation(item);
            }
            let throwTo = item % this.test.condition == 0 ? this.test.True : this.test.False;
            monkeys[throwTo].items.push(item);
        });
        this.items = [];
    }
}

let monkeys = {};
let inspectionCounts = [];
content = content.split("\r\n\r\n");
content.forEach((monkey, index) => {
    monkeys[index] = {
        name: index,
        items: monkey
            .split("\r\n")[1]
            .split(": ")[1]
            .split(", ")
            .map((item) => parseInt(item)),
        operation: {
            operator: monkey.split("\r\n")[2].split("old ")[1][0],
            value: monkey.split("\r\n")[2].split("old ")[1].split(" ")[1],
        },
        test: {
            condition: +monkey.split("\r\n")[3].split("by ")[1],
            True: +monkey.split("\r\n")[4].split("monkey ")[1],
            False: +monkey.split("\r\n")[5].split("monkey ")[1],
        },
    };
    monkeys[index] = new Monkey(monkeys[index]);
});
for (let round = 0; round < 20; round++) {
    for (let monkey of Object.keys(monkeys)) {
        monkeys[monkey].inspect(true);
    }
}
for (let monkey of Object.keys(monkeys)) {
    inspectionCounts.push(monkeys[monkey].inspectedTimes);
}
inspectionCounts.sort((a, b) => b - a);
answer = inspectionCounts.slice(0, 2).reduce((prev, curr) => prev * curr);
console.log("Part 1 Answer:", answer);

// part 2

console.log("Part 2 Answer:", answer);
