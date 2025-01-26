maze = []
location = []
costs = {}
totaldot = 0
with open("day16") as file:
    for x,line in enumerate(file):
        line = line.strip("\n")
        row = []
        for y,char in enumerate(line):
            row.append(char)
            if char == "S":
                location = [x,y]
            elif char == ".":
                costs[(x,y)] = 0
                totaldot += 1
        maze.append(row)

def score(path, b):
    return path[-1][2]+1+(not b == path[-1][1])*1000

borders = [[0,1],[0,-1],[1,0],[-1,0]]
change = True
paths = [[[location,[0,1],0]]]
visited = {(tuple(location),(0,1)):0}
minpath = 0
bestpaths = []
while change:
    print(len(paths), f"{len(visited)}/{totaldot*4}", minpath)
    change = False
    npaths = []
    visited_coords = [x[:2] for x in visited]
    for p in paths:
        for b in borders:
            if maze[p[-1][0][0]+b[0]][p[-1][0][1]+b[1]] == "." and [p[-1][0][0]+b[0],p[-1][0][1]+b[1]] not in [x[0] for x in p]:
                if ((p[-1][0][0]+b[0],p[-1][0][1]+b[1]),tuple(b)) in visited.keys():
                    if visited[((p[-1][0][0]+b[0],p[-1][0][1]+b[1]),tuple(b))] > score(p,b):
                        npaths.append(p+[[[p[-1][0][0]+b[0],p[-1][0][1]+b[1]],b,score(p,b)]])
                        visited[((p[-1][0][0]+b[0],p[-1][0][1]+b[1]),tuple(b))] = score(p,b)
                    elif visited[((p[-1][0][0]+b[0],p[-1][0][1]+b[1]),tuple(b))] == score(p,b):
                        npaths.append(p+[[[p[-1][0][0]+b[0],p[-1][0][1]+b[1]],b,score(p,b)]])
                else:
                    npaths.append(p + [[[p[-1][0][0] + b[0], p[-1][0][1] + b[1]], b, score(p,b)]])
                    visited[((p[-1][0][0] + b[0], p[-1][0][1] + b[1]), tuple(b))] = score(p,b)
                change = True
            elif maze[p[-1][0][0]+b[0]][p[-1][0][1]+b[1]] == "E" and (score(p,b) < minpath or minpath == 0):
                minpath = score(p,b)
                bestpaths = [p]
            elif maze[p[-1][0][0]+b[0]][p[-1][0][1]+b[1]] == "E" and (score(p,b) == minpath):
                bestpaths.append(p)
    paths = npaths

tiles = []
for p in bestpaths:
    for t in p:
        if t[0] not in tiles:
            tiles.append(t[0])

for x,r in enumerate(maze):
    for y,t in enumerate(r):
        if [x,y] in tiles:
            print("O",end="")
        else:
            print(t,end="")
    print()
print(len(tiles)+1)
print(minpath)