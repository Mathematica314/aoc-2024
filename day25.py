import numpy
import itertools

locks = []
keys = []

with open("day25") as file:
    current = []
    for line in file:
        line = line.strip("\n")
        if line == "":
            cr90 = [len("".join(x).replace(".",""))-1 for x in numpy.rot90([[y for y in x] for x in current])[::-1]]
            if current[0][0] == ".":
                keys.append(cr90)
            else:
                locks.append(cr90)
            current = []
        else:
            current.append(line)
cr90 = [len("".join(x).replace(".",""))-1 for x in numpy.rot90([[y for y in x] for x in current])[::-1]]
if current[0][0] == ".":
    keys.append(cr90)
else:
    locks.append(cr90)

maxlen = len(current)

total = 0
for pair in itertools.product(keys,locks):
    if max([a+b for a,b in zip(pair[0],pair[1])]) < maxlen-1:
        total += 1
print(total)

