import itertools
from collections import defaultdict

chars = defaultdict(list)
grid = []

with open("day12") as file:
    for x,row in enumerate(file):
        row = row.strip("\n")
        grow = []
        for y,char in enumerate(row):
            grow.append(char)
            chars[char].append([int(x),int(y)])
        grid.append(grow)

regions = defaultdict(list)
repeats = defaultdict(int)

def region(b,adj):
    if tuple(b) in adj.keys():
        out = [b]
        for k in adj[tuple(b)]:
            out = out + region(k,adj)
        return out
    else:
        return [b]

borders = [[-1,0],[1,0],[0,-1],[0,1]]

def fill(legals, s, prev=[]):
    nexts = [[s[0]+b[0],s[1]+b[1]] for b in borders if [s[0]+b[0],s[1]+b[1]] in legals and [s[0]+b[0],s[1]+b[1]] not in prev]
    if len(nexts) == 0:
        return s
    else:
        return [fill(legals,sn,prev+[sn]) for sn in nexts] + s

regions = []
total1 = 0
for char in chars.keys():
    allfound = []
    points = chars[char]
    while len(points) > 0:
        edge = [points[0]]
        found = [points[0]]
        new = True
        while new:
            new = False
            nedge = []
            for e in edge:
                for b in borders:
                    if [e[0]+b[0],e[1]+b[1]] not in found and [e[0]+b[0],e[1]+b[1]] in points:
                        new = True
                        nedge.append([e[0]+b[0],e[1]+b[1]])
                        found.append([e[0]+b[0],e[1]+b[1]])
            edge = nedge
        allfound.append(found)
        points = [i for i in points if i not in found]
    regions.append(allfound)
    for plot in allfound:
        hidden = 0
        for square in plot:
            for b in borders:
                if [square[0]+b[0],square[1]+b[1]] in plot:
                    hidden += 1
        total1+=len(plot)*(len(plot)*4-hidden)

regions = [x for r in regions for x in r]
total2 = 0
for region in regions:
    mnm = [min(region,key=lambda x:x[0])[0],min(region,key=lambda x:x[1])[1]]
    mxm = [max(region,key=lambda x:x[0])[0],max(region,key=lambda x:x[1])[1]]
    region = [[x[0]-mnm[0],x[1]-mnm[1]] for x in region]
    region.sort()
    lines = [[] for i in range(4)]
    for i,b in enumerate(borders):
        for sq in region:
            if [sq[0]+b[0],sq[1]+b[1]] not in region:
                lines[i].append(sq)
    lines[2] = [[a[1],a[0]] for a in lines[2]]
    lines[3] = [[a[1],a[0]] for a in lines[3]]
    lines[1] = [[mxm[0]-a[0],a[1]] for a in lines[1]]
    lines[3] = [[a[0],mxm[1]-a[1]] for a in lines[3]]
    lines = [[sorted(d)]for d in lines]
    tlines = 0
    for dir in lines:
        rows = defaultdict(list)
        for x in dir[0]:
            rows[x[0]].append(x[1])
        rows = list(rows.values())
        for row in rows:
            tlines += 1
            prevval = row[0]-1
            for val in row:
                if val - prevval != 1:
                    tlines += 1
                prevval = val
    total2 += tlines*len(region)
print(total1)
print(total2)