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
const counter1 = (horLines, verLines) => {
    for (let direction = 0; direction < 2; direction++) {
        let grid = direction ? verLines : horLines;
        grid.forEach((mainLine, y) => {
            for (let [index, line] of [mainLine, mainLine.slice().reverse()].entries()) {
                let maxHeight = -1;
                line.forEach((tree, tempX) => {
                    let x = index ? Math.abs(tempX - mainLine.length + 1) : tempX;
                    if (tree > maxHeight) {
                        visible.push(direction ? `${x},${y}` : `${y},${x}`);
                        maxHeight = tree;
                    }
                });
            }
        });
    }
};

let visible = [];
let lines = content.split("\r\n");
let horLines = [];
let verLines = [];
lines.forEach((line) => horLines.push(line.split("")));
for (let y = 0; y < horLines[0].length; y++) {
    let invertedLine = [];
    for (let x = 0; x < horLines.length; x++) {
        invertedLine.push(horLines[x][y]);
    }
    verLines.push(invertedLine);
}
counter1(horLines, verLines);
visible = visible.filter((value, index) => visible.indexOf(value) == index);
answer = visible.length;
console.log("Part 1 Answer:", answer);

// part 2
const counter2 = (height, variable, constant, direction, result) => {
    let grid = direction ? verLines : horLines;
    for (let i = 0; i < 2; i++) {
        let index = variable;
        let visible = 0;
        for (i ? ++index : --index; i ? index < grid[0].length : index >= 0; i ? index++ : index--) {
            if (grid[constant][index] >= height) {
                visible++;
                break;
            }
            visible++;
        }
        result *= visible;
    }
    return result;
};

answer = 1;
visible.forEach((coordinates) => {
    let result = 1;
    let [y, x] = coordinates.split(",");
    for (let i = 0; i < 2; i++) {
        result = counter2(horLines[y][x], i ? y : x, i ? x : y, i, result);
    }
    answer = answer < result ? result : answer;
});
console.log("Part 2 Answer:", answer);
