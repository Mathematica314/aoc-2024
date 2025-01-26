obstacles = []
direction = (-1, 0)
turns = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
bounds = []
with open("day6") as file:
    l = file.readlines()
    for x, row in enumerate(l):
        row = row.strip("\n")
        if x == 0:
            bounds = [len(row), len(l)]
        for y, char in enumerate(row):
            if char == "#":
                obstacles.append([x, y])
            if char == "^":
                pos = [x, y]
initpos = pos
visited = [pos]
while bounds[0] > pos[0] >= 0 and bounds[1] > pos[1] >= 0:
    n = [pos[0] + direction[0], pos[1] + direction[1]]
    if n in obstacles:
        direction = turns[direction]
    else:
        pos = n
        if n not in visited:
            visited.append(n)

visited.pop(-1)
print(len(visited))

total = 0
for i, j in visited:
    print(f"{visited.index([i, j])}/{len(visited)}")
    if [i, j] == [7, 8]:
        pass
    if [i, j] != initpos:
        vst = []
        pos = initpos
        direction = (-1, 0)
        obst = obstacles + [[i, j]]
        noloop = True
        while bounds[0] > pos[0] >= 0 and bounds[1] > pos[1] >= 0 and noloop:
            n = [pos[0] + direction[0], pos[1] + direction[1]]
            if n in obst:
                direction = turns[direction]
            else:
                pos = n
                if n + list(direction) in vst:
                    total += 1
                    noloop = False
                else:
                    vst.append(n + list(direction))
print(total)
