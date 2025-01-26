import copy

robots = []
robots2 = []
grid = [101,103]
quadrants = [[0,0],[0,0]]
with open("day14") as file:
    for line in file:
        robot = ([[int(j) for j in c]for c in [x[2:].split(",") for x in line.strip("\n").split(" ")]])
        robots2.append(copy.deepcopy((robot)))
        robot[0] = [(robot[1][0] * 3 + robot[0][0]) % grid[0], (robot[1][1] * 3 + robot[0][1]) % grid[1]]
        robots.append(robot)
        if not (robot[0][0] == (grid[0]-1)/2 or robot[0][1] == (grid[1]-1)/2):
            quadrants[int(robot[0][0] >= (grid[0]+1)/2)][int(robot[0][1] > (grid[1]+1)/2)] += 1
print(quadrants[0][0]*quadrants[0][1]*quadrants[1][0]*quadrants[1][1])

# square = [[0 for _ in range(grid[0])] for _ in range(grid[1])]
#
# for r in robots:
#     square[r[0][1]][r[0][0]] += 1
#
# for row in square:
#
#     row = ["." if i == 0 else "x"for i in row]
#     for cell in row:
#         print(cell,end="")
#     print()
# print()

ind = int(input())-1
for r in robots2:
    r[0] = [(r[1][0]*ind + r[0][0]) % grid[0], (r[1][1]*ind + r[0][1]) % grid[1]]
while True:
    ind += 1
    square = [[0 for i in range(grid[0])] for j in range(grid[1])]
    for r in robots2:
        r[0] = [(r[1][0]+r[0][0])%grid[0],(r[1][1]+r[0][1])%grid[1]]
        square[r[0][1]][r[0][0]] += 1
    for row in square:
        row = ["□" if i == 0 else "■" for i in row]
        for cell in row:
            print(cell,end="")
        print()
    print(ind)
    print()
    print()
    print("----------------------------------------------------\n\n")
    input()
