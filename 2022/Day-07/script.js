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
current = [];
let fileSys = {};
for (let line of content.split("\r\n")) {
    let instruction = line.split(" ");
    if (instruction.length == 3) {
        if (instruction[2] != "..") {
            current.push(instruction[2]);
            fileSys[current.join(",")] = 0;
        } else {
            current.pop();
        }
    } else {
        if (instruction[0] != "$" && instruction[0] != "dir") {
            for (let index in current) {
                fileSys[current.slice(0, parseInt(index) + 1).join(",")] += parseInt(instruction[0]);
            }
        }
    }
}
for (let value of Object.values(fileSys)) {
    value < 100000 ? (answer += value) : null;
}
console.log("Part 1 Answer:", answer);

// part 2
let requiredSpace = 30000000-70000000+fileSys['/']
for (let value of Object.values(fileSys).sort((a,b)=>a-b)) {
    if (value>=requiredSpace) {
        answer = value
        break
    }
}
console.log("Part 2 Answer:", answer);
