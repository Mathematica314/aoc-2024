import copy

dirs = False
directions = {"<":[0,-1],">":[0,1],"^":[-1,0],"v":[1,0]}
moves = []
map = []
with open("day15") as file:
    for x,line in enumerate(file):
        line = line.strip("\n")
        if line == "":
            dirs = True
        elif dirs:
            for char in line:
                moves.append(directions[char])
        else:
            map.append([i for i in line])
            for y,i in enumerate(line):
                if i == "@":
                    robot = [x,y]

map2 = []
for row in map:
    row2 = []
    for char in row:
        if char == "O":
            row2 += ["[","]"]
        elif char == "@":
            row2 += ["@","."]
        else:
            row2 += [char,char]
    map2.append(row2)
robot2 = [robot[0],robot[1]*2]

for move in moves:
    wall = False
    scanned = [robot.copy()]
    while not wall:
        if map[scanned[-1][0]+move[0]][scanned[-1][1]+move[1]] == "#":
            wall = True
        elif map[scanned[-1][0]+move[0]][scanned[-1][1]+move[1]] == ".":
            map[robot[0]][robot[1]] = "."
            rbt = True
            for block in scanned:
                if rbt:
                    map[block[0]+move[0]][block[1]+move[1]] = "@"
                    robot = [block[0]+move[0],block[1]+move[1]]
                    rbt = False
                else:
                    map[block[0]+move[0]][block[1]+move[1]] = "O"
            break
        else:
            scanned.append([scanned[-1][0]+move[0],scanned[-1][1]+move[1]])
total1 = 0
for x,row in enumerate(map):
    for y,char in enumerate(row):
        if char == "O":
            total1+=x*100 + y
        print(char,end="")
    print()
print(total1)

for move in moves:
    if move[1] == 0:
        pushed = [[robot2.copy()+["@"]]]
        legal = True
        while legal:
            allclear = True
            pushed.append([])
            for block in pushed[-2]:
                nb = map2[block[0]+move[0]][block[1]+move[1]]
                if nb == "#":
                    legal = False
                    allclear = False
                    break
                elif nb == "[":
                    pushed[-1].append([block[0]+move[0],block[1]+move[1],"["])
                    if block[2] != "[":
                        pushed[-1].append([block[0]+move[0],block[1]+move[1]+1,"]"])
                    allclear = False
                elif nb == "]":
                    pushed[-1].append([block[0]+move[0],block[1]+move[1],"]"])
                    if block[2] != "]":
                        pushed[-1].append([block[0]+move[0],block[1]+move[1]-1,"["])
                    allclear = False
            if allclear:
                robot2 = [robot2[0] + move[0], robot2[1] + move[1]]
                for row in pushed:
                    for square in row:
                        map2[square[0]][square[1]] = "."
                for row in pushed:
                    for square in row:
                        map2[square[0] + move[0]][square[1] + move[1]] = square[2]
                legal = False

    else:
        wall = False
        scanned = [robot2.copy()]
        while not wall:
            if map2[scanned[-1][0] + move[0]][scanned[-1][1] + move[1]] == "#":
                wall = True
            elif map2[scanned[-1][0] + move[0]][scanned[-1][1] + move[1]] == ".":
                map2[robot2[0]][robot2[1]] = "."
                rbt = True
                rightbox = move == [0,-1]
                for block in scanned:
                    if rbt:
                        map2[block[0] + move[0]][block[1] + move[1]] = "@"
                        robot2 = [block[0] + move[0], block[1] + move[1]]
                        rbt = False
                    else:
                        if rightbox:
                            map2[block[0] + move[0]][block[1] + move[1]] = "]"
                        else:
                            map2[block[0] + move[0]][block[1] + move[1]] = "["
                        rightbox = not rightbox
                break
            else:
                scanned.append([scanned[-1][0] + move[0], scanned[-1][1] + move[1]])

total2 = 0
for x,row in enumerate(map2):
    for y,char in enumerate(row):
        print(char,end="")
        if char == "[":
            total2 += 100*x + y
    print()
print(total2)