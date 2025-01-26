import functools
import itertools

passwords = []
with open("day21") as file:
    for line in file:
        passwords.append(line.strip("\n"))

numpad = [["7", "8", "9"],
          ["4", "5", "6"],
          ["1", "2", "3"],
          [None, "0", "A"]]

arrows = [[None, "^", "A"],
          ["<", "v", ">"]]

moves = {(-1, 0): "^", (1, 0): "v", (0, -1): "<", (0, 1): ">"}

def getmoves(str,map):
    posmap = {}
    for x, row in enumerate(map):
        for y, char in enumerate(row):
            if char is not None:
                posmap[char] = (x, y)
    out = []
    prev = "A"
    rmap = [[0 for _ in map] for _ in map[0]]
    for x, row in enumerate(map):
        for y, char in enumerate(row):
            rmap[y][x] = char
    for char in str:
        pv = posmap[prev]
        cr = posmap[char]
        move = [cr[0] - pv[0], cr[1] - pv[1]]
        if move == [0, 0]:
            out.append([""])
        elif move[0] == 0:
            out.append([moves[(0, int(move[1] / abs(move[1])))] * abs(move[1])])
        elif move[1] == 0:
            out.append([moves[(int(move[0] / abs(move[0]))), 0] * abs(move[0])])
        else:
            cut = []
            if None not in map[pv[0]][min(pv[1], cr[1]):max(pv[1], cr[1]) + 1]:
                cut.append(moves[(0, int(move[1] / abs(move[1])))] * abs(move[1]) +
                           moves[(int(move[0] / abs(move[0])), 0)] * abs(move[0]))
            if None not in rmap[pv[1]][min(pv[0], cr[0]):max(pv[0], cr[0]) + 1]:
                cut.append(moves[(int(move[0] / abs(move[0])), 0)] * abs(move[0]) +
                           moves[(0, int(move[1] / abs(move[1])))] * abs(move[1]))
            out.append(cut)
        prev = char
    return [[x + "A" for x in c] for c in out]

@functools.cache
def cost(mvs,depth):
    if depth == 0:
        return len(mvs)
    else:
        total = 0
        for x in getmoves(mvs,arrows):
            total += min(cost(y,depth-1) for y in x)
        return total

total1 = 0
total2 = 0
for p in passwords:
    a = ["".join(x) for x in itertools.product(*getmoves(p,numpad))]
    total1 += min([cost(x,2) for x in a])*int(p[:-1])
    total2 += min([cost(x,25) for x in a])*int(p[:-1])

print(total1)
print(total2)