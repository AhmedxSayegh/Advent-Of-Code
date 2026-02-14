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
const cycleIncrement = (cycle) => {
    cycle += 1;
    if (cycle == 20 || (cycle - 20) % 40 == 0) {
        return [cycle, answer + cycle * x];
    }
    return [cycle, answer];
};

// part 2
const draw = () => {
    let row = cycle % 40 ? Math.floor(cycle / 40) : cycle / 40 - 1;
    if ((cycle - 1) % 40 == 0) {
        crt.push("");
    }
    if ([x - 1, x, x + 1].includes(crt[row].length)) {
        crt[row] += "#";
    } else {
        crt[row] += ".";
    }
};

const instructions = content.split("\r\n");
let x = 1;
let cycle = 0;
let crt = [];
answer = 0;
instructions.forEach((instruction) => {
    [cycle, answer] = cycleIncrement(cycle, answer);
    draw();
    if (instruction != "noop") {
        [cycle, answer] = cycleIncrement(cycle, answer);
        draw();
        x += parseInt(instruction.split(" ")[1]);
    }
});
console.log("Part 1 Answer:", answer);
console.log("Part 2 Answer:");
crt.forEach((line) => console.log(line));
