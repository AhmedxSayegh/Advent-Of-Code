import heapq

content = open("Input.txt").read().split("\n")

# Used By Both Parts
def run(prev_cost, y, x):
    if grid[(y,x)]['cost'] != -1 and grid[(y,x)]['cost'] < prev_cost:
        return
    cost = prev_cost + grid[(y,x)]['value']
    if grid[(y,x)]['cost'] == -1 or grid[(y,x)]['cost'] > cost:
        grid[(y,x)]['cost'] = cost
        for yOffset, xOffset in [(0,1), (0,-1), (1,0), (-1,0)]:
            newY = y + yOffset
            newX = x + xOffset
            if -1 < newY < maxWidth and -1 < newX < maxHeight:
                heapq.heappush(next_, (cost, newY, newX))

# Part 1
grid = {}
next_ = [(0, 0, 0)]
for y, row in enumerate(content):
    for x, value in enumerate(row):
        grid[(y,x)] = {'value': int(value), 'cost': -1}
maxWidth, maxHeight = max(grid.keys())
maxWidth += 1
maxHeight += 1
while next_:
    run(*heapq.heappop(next_))
print("Part 1 Answer:", grid[max(grid.keys())]["cost"] - grid[(0, 0)]["cost"])

# Part 2
for key in grid.keys():
    grid[key]['cost'] = -1
for ver in range(4):
    for y, row in enumerate(content):
        for x, value in enumerate(row):
            v = grid[(y + ver * maxHeight, x)]["value"]
            grid[(y + (ver + 1) * maxHeight, x)] = {
                "value": v + 1 if v < 9 else 1,
                "cost": -1,
            }
for ver in range(5):
    for hor in range(4):
        for y, row in enumerate(content):
            for x, value in enumerate(row):
                v = grid[(y + ver * maxHeight, x + hor * maxWidth)]['value']
                grid[(y + ver * maxHeight, x + (hor + 1) * maxWidth)] = {
                    "value": v + 1 if v < 9 else 1,
                    "cost": -1,
                }
maxWidth, maxHeight = max(grid.keys())
maxWidth += 1
maxHeight += 1
next_ = [(0, 0, 0)]
while next_:
    run(*heapq.heappop(next_))
print("Part 2 Answer:", grid[max(grid.keys())]["cost"] - grid[(0, 0)]["cost"])
