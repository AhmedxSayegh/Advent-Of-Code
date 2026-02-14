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
let result = [];
answer = 0;
content.split("\r\n").forEach((sack) => {
    let [first, second] = [sack.slice(0, sack.length / 2), sack.slice(sack.length / 2)];
    for (let letter of first.split("")) {
        if (second.includes(letter)) {
            result.push(letter);
            break;
        }
    }
});
result.forEach((letter) => {
    if (letter.charCodeAt(0) > 96) {
        answer += letter.charCodeAt(0) - 96;
    } else {
        answer += letter.charCodeAt(0) - 38;
    }
});
console.log("Part 1 Answer:", answer);

// part 2
result = [];
answer = 0;
lines = content.split("\r\n");
for (let i = 0; i < lines.length; i += 3) {
    let group = lines.slice(i, i + 3);
    for (let letter of group[0].split("")) {
        if (group[1].includes(letter) && group[2].includes(letter)) {
            result.push(letter);
            break;
        }
    }
}
result.forEach((letter) => {
    if (letter.charCodeAt(0) > 96) {
        answer += letter.charCodeAt(0) - 96;
    } else {
        answer += letter.charCodeAt(0) - 38;
    }
});
console.log("Part 2 Answer:", answer);
