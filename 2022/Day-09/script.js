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

// part 1 & part 2
const move = (coordinates, destination, count) => {
    if (count == ropeLength) {
        return;
    }
    let distance = { x: destination.x - coordinates.x, y: destination.y - coordinates.y };
    if (Math.abs(distance.x * distance.y) > 1) {
        for (let axis of Object.keys(coordinates)) {
            coordinates[axis] += distance[axis] / Math.abs(distance[axis]);
        }
    } else {
        let [axis, value] = distance.x ? ["x", distance.x] : ["y", distance.y];
        if (Math.abs(value) > 1) {
            coordinates[axis] += value / Math.abs(value);
        }
    }
    if (count == 1 || count == 9) {
        visited[count].push([coordinates.x, coordinates.y].join(","));
    }
    move(heads[count + 1], coordinates, count + 1);
};

let ropeLength = 10;
let heads = {};
let visited = {};
for (let i = 0; i < ropeLength; i++) {
    heads[i] = { x: 0, y: 0 };
    visited[i + 1] = ["0,0"];
}
let instructions = content.split("\r\n");
instructions.forEach((instruction) => {
    [direction, steps] = instruction.split(" ");
    let axis = ["R", "L"].includes(direction) ? "x" : "y";
    let value = ["R", "U"].includes(direction) ? 1 : -1;
    for (let step = 0; step < parseInt(steps); step++) {
        heads[0][axis] += value;
        move(heads[1], heads[0], 1);
    }
});
for (let i of [1, 9]) {
    visited[i] = new Set(visited[i]);
}
answer = visited[1].size;
console.log("Part 1 Answer:", answer);
answer = visited[9].size;
console.log("Part 2 Answer:", answer);
