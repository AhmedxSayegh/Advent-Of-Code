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
let packet = [];
let counter = 0;
let index = 0;
for (let letter of content.split("")) {
    index++;
    if (!packet.includes(letter)) {
        counter++;
    } else {
        counter = packet.length - packet.indexOf(letter);
        packet.splice(0, packet.indexOf(letter) + 1);
    }
    packet.push(letter);
    if (counter == 4) {
        answer = index;
        break;
    }
}
console.log("Part 1 Answer:", answer);

// part 2
let message = [];
counter = 0;
index = 0;
for (let letter of content.split("")) {
    index++;
    if (!message.includes(letter)) {
        counter++;
    } else {
        counter = message.length - message.indexOf(letter);
        message.splice(0, message.indexOf(letter) + 1);
    }
    message.push(letter);
    if (counter == 14) {
        answer = index;
        break;
    }
}
console.log("Part 2 Answer:", answer);
