import itertools

nodes = {}
bounds = []
with open("day8") as file:
    for x, row in enumerate(file):
        row = row.strip("\n")
        for y, char in enumerate(row):
            if char != ".":
                if char in nodes.keys():
                    nodes[char].append((x,y))
                else:
                    nodes[char] = [(x,y)]
bounds = [x,y]
print(bounds)
antinodes1 = []
antinodes2 = []
for name in nodes.keys():
    if len(nodes[name]) > 1:
        for pair in itertools.combinations(nodes[name],2):
            delta = [pair[0][0]-pair[1][0], pair[0][1]-pair[1][1]]
            for x in [(pair[0][0]+delta[0],pair[0][1]+delta[1]), (pair[1][0]-delta[0],pair[1][1]-delta[1])]:
                if x not in antinodes1 and 0<=x[0]<=bounds[0] and 0<=x[1]<=bounds[1]:
                    antinodes1.append(x)
            for k in range(-max(bounds), max(bounds)):
                dn = [i*k for i in delta]
                for x in [(pair[0][0] + dn[0], pair[0][1] + dn[1]),(pair[1][0] - dn[0], pair[1][1] - dn[1])]:
                    if x not in antinodes2 and 0 <= x[0] <= bounds[0] and 0 <= x[1] <= bounds[1]:
                        antinodes2.append(x)
antinodes1.sort(key = lambda x: x[0])
print(antinodes1)
print(len(antinodes1))

print(antinodes2)
print(len(antinodes2))