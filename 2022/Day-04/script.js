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
content.split("\r\n").forEach((pair) => {
    [first, second] = pair.split(",");
    first = first.split("-").map((num) => parseInt(num));
    second = second.split("-").map((num) => parseInt(num));
    if (first[1] - first[0] + 1 >= second[1] - second[0] + 1) {
        if (first[0] <= second[0] && first[1] >= second[1]) {
            answer += 1;
        }
    } else {
        if (second[0] <= first[0] && second[1] >= first[1]) {
            answer += 1;
        }
    }
});
console.log("Part 1 Answer:", answer);

// part 2
answer = 0;
content.split("\r\n").forEach((pair) => {
    [first, second] = pair.split(",");
    first = first.split("-").map((num) => parseInt(num));
    second = second.split("-").map((num) => parseInt(num));
    if (
        (first[0] <= second[1] && second[1] <= first[1]) ||
        (first[0] <= second[0] && second[0] <= first[1]) ||
        (second[0] <= first[1] && first[1] <= second[1]) ||
        (second[0] <= first[0] && first[0] <= second[1])
    ) {
        answer += 1;
    }
});
console.log("Part 2 Answer:", answer);
