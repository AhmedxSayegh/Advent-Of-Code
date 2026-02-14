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
answer = 0;
content.split("\r\n\r\n").forEach((elv) => {
    let sum = 0;
    elv.split("\r\n").forEach((cal) => {
        sum += parseInt(cal);
    });
    if (sum > answer) {
        answer = sum;
    }
});
console.log("Part 1 Answer:", answer);

// part 2
answer = [];
content.split("\r\n\r\n").forEach((elv) => {
    let sum = 0;
    elv.split("\r\n").forEach((cal) => {
        sum += parseInt(cal);
    });
    answer.push(sum);
});
answer.sort((a, b) => {
    return b - a;
});
console.log(
    "Part 2 Answer:",
    answer.slice(0, 3).reduce((sum, num) => sum + num)
);
