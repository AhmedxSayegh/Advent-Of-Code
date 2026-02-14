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
const step = ({ y, x }) => {
    if (x > 0 && grid[[y, x]] + 1 >= grid[[y, x - 1]] && !visited[[y, x - 1]]) {
        possibilities.push({ y, x: x - 1 });
        visited[[y, x - 1]] = true;
    }
    if (x < width && grid[[y, x]] + 1 >= grid[[y, x + 1]] && !visited[[y, x + 1]]) {
        possibilities.push({ y, x: x + 1 });
        visited[[y, x + 1]] = true;
    }
    if (y > 0 && grid[[y, x]] + 1 >= grid[[y - 1, x]] && !visited[[y - 1, x]]) {
        possibilities.push({ y: y - 1, x });
        visited[[y - 1, x]] = true;
    }
    if (y < height && grid[[y, x]] + 1 >= grid[[y + 1, x]] && !visited[[y + 1, x]]) {
        possibilities.push({ y: y + 1, x });
        visited[[y + 1, x]] = true;
    }
};

answer = 0;
let i = true;
let grid = {};
let visited = {};
let possibilities = [];
let current;
let end;
let lines = content.split("\r\n");
lines.forEach((line, y) => {
    line.split("").forEach((value, x) => {
        if (value == "S") {
            grid[[y, x]] = "a".charCodeAt();
            visited[[y, x]] = true;
            current = { y, x };
        } else if (value == "E") {
            grid[[y, x]] = "z".charCodeAt();
            visited[[y, x]] = false;
            end = { y, x };
        } else {
            grid[[y, x]] = value.charCodeAt();
            visited[[y, x]] = false;
        }
    });
});
let height = lines.length - 1;
let width = lines[0].split("").length - 1;
step(current);
while (i) {
    for (let possibility of [...possibilities]) {
        if (possibility.y == end.y && possibility.x == end.x) {
            i = false;
            break;
        }
        step(possibility);
        possibilities.shift();
    }
    answer++;
}
console.log("Part 1 Answer:", answer);

// part 2
const step2 = ({ y, x }) => {
    if (x > 0 && grid[[y, x]] - 1 <= grid[[y, x - 1]] && !visited[[y, x - 1]]) {
        possibilities.push({ y, x: x - 1 });
        visited[[y, x - 1]] = true;
    }
    if (x < width && grid[[y, x]] - 1 <= grid[[y, x + 1]] && !visited[[y, x + 1]]) {
        possibilities.push({ y, x: x + 1 });
        visited[[y, x + 1]] = true;
    }
    if (y > 0 && grid[[y, x]] - 1 <= grid[[y - 1, x]] && !visited[[y - 1, x]]) {
        possibilities.push({ y: y - 1, x });
        visited[[y - 1, x]] = true;
    }
    if (y < height && grid[[y, x]] - 1 <= grid[[y + 1, x]] && !visited[[y + 1, x]]) {
        possibilities.push({ y: y + 1, x });
        visited[[y + 1, x]] = true;
    }
};

i = true;
answer = 0;
Object.keys(visited).forEach(key=>visited[key]=false)
visited[[end.y,end.x]] = true
possibilities = [];
step2(end);
while (i) {
    for (let possibility of [...possibilities]) {
        if (grid[[possibility.y,possibility.x]] == 97) {
            i = false;
            break;
        }
        step2(possibility);
        possibilities.shift();
    }
    answer++;
}
console.log("Part 2 Answer:", answer);
