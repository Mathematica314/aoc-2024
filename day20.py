import networkx
from collections import defaultdict

map = []
with open("day20") as file:
    for x,row in enumerate(file):
        row = row.strip("\n")
        line = []
        for y,char in enumerate(row):
            line.append(char)
            if char == "S":
                start = (x,y)
            if char == "E":
                end = (x,y)
        map.append(line)

edge = [start]
found = [start]

borders = [[0, 1], [0, -1], [1, 0], [-1, 0]]

gr = networkx.Graph()
gr.add_node(start)

change = True
while change:
    change = False
    nedge = []
    for i in edge:
        for b in borders:
            n = (i[0]+b[0],i[1]+b[1])
            if map[n[0]][n[1]] != "#" and n not in found:
                found.append(n)
                nedge.append(n)
                change = True
                gr.add_node(n)
                gr.add_edge(i,n)
    edge = nedge

pa = networkx.shortest_path(gr,start,end)

scores = {}
for x in range(len(map)):
    for y in range(len(map[0])):
        if (x,y) in pa:
            scores[(x,y)] = len(pa)-pa.index((x,y))
        else:
            scores[(x,y)] = -1

maxcheat = 20

cheatable = []
for x in range(-maxcheat,maxcheat+1):
    for y in range(-maxcheat+abs(x),maxcheat-abs(x)+1):
        cheatable.append((x,y))
total = 0
for p in pa:
    for c in cheatable:
        k = (p[0]+c[0],p[1]+c[1])
        if 0 <= k[0] < len(map) and 0 <= k[1] < len(map[0]) and scores[k] - scores[p] - (abs(c[0])+abs(c[1])) >= 100:
            total += 1
print(total)