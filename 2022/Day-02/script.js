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
const guide = { A: 1, B: 2, C: 3, X: 1, Y: 2, Z: 3 };
answer = 0;
content.split("\r\n").forEach((round) => {
    let [opponent, me] = round.split(" ");
    answer += guide[me];
    if (guide[me] == 1 && guide[opponent] == 3) {
        answer += 6;
    } else if (guide[me] == 3 && guide[opponent] == 1) {
    } else {
        answer += guide[me] > guide[opponent] ? 6 : guide[me] == guide[opponent] ? 3 : 0;
    }
});
console.log("Part 1 Answer:", answer);

// part 2
answer = 0;
content.split("\r\n").forEach((round) => {
    let [opponent, result] = round.split(" ");
    if (guide[result] == 1) {
        answer += guide[opponent] == 1 ? 3 : guide[opponent] - 1;
    } else if (guide[result] == 2) {
        answer += guide[opponent] + 3;
    } else {
        answer += (guide[opponent] == 3 ? 1 : guide[opponent] + 1) + 6;
    }
});
console.log("Part 2 Answer:", answer);
