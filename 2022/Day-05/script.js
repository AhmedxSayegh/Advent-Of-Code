const file = require("fs");
const textFile = file.readFileSync("./content.txt", "utf-8");
let test = textFile.split("\r\ninput:")[0].split("test:\r\n")[1];
let input = textFile.split("\r\ninput:\r\n")[1];
let answer;
// set the condition to 0 to get the test answer, and to 1 to get the input answer
let condition = 1;
if (condition) {
    content = input;
} else {
    content = test;
}

// part 1
answer = "";
let crates = [];
let stacks = {};
let [tempCrates, instructions] = content.split("\r\n\r\n");
tempCrates
    .split("\r\n")
    .slice(0, -1)
    .forEach((line) => {
        crates.push(
            line.split(/(\[[A-Z]\])/).filter((i) => {
                if (i && i != " ") {
                    return true;
                }
            })
        );
    });
crates.reverse();
crates.forEach((layer) => {
    let index = 1;
    layer.forEach((crate) => {
        if (crate.includes(" ")) {
            index += Math.floor(crate.length / 4);
        } else {
            stacks[index] = stacks[index] ? [...stacks[index], crate.split("")[1]] : [crate.split("")[1]];
            index++;
        }
    });
});
instructions.split("\r\n").forEach((singleInstruction) => {
    let [, quantity, , from, , to] = singleInstruction.split(" ");
    moved = stacks[from].splice(stacks[from].length - quantity);
    stacks[to] = [...stacks[to], ...moved.reverse()];
});
Object.keys(stacks).forEach((key) => {
    answer += stacks[key].at(-1);
});
console.log("Part 1 Answer:", answer);

// part 2
answer = "";
stacks = {};
crates.forEach((layer) => {
    let index = 1;
    layer.forEach((crate) => {
        if (crate.includes(" ")) {
            index += Math.floor(crate.length / 4);
        } else {
            stacks[index] = stacks[index] ? [...stacks[index], crate.split("")[1]] : [crate.split("")[1]];
            index++;
        }
    });
});
instructions.split("\r\n").forEach((singleInstruction) => {
    let [, quantity, , from, , to] = singleInstruction.split(" ");
    moved = stacks[from].splice(stacks[from].length - quantity);
    stacks[to] = [...stacks[to], ...moved];
});
Object.keys(stacks).forEach((key) => {
    answer += stacks[key].at(-1);
});
console.log("Part 2 Answer:", answer);
