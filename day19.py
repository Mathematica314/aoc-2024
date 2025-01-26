import functools
from collections import defaultdict
import networkx

patterns = []
with open("day19") as file:
    firstline = True
    for line in file:
        if firstline:
            towels = line.strip("\n").split(", ")
            firstline = False
        else:
            patterns.append(line.strip("\n"))
patterns.pop(0)

@functools.cache
def ptrn(prev,full):
    next = full[len(prev):]
    if prev == full:
        return 1
    else:
        total = 0
        edge = []
        tw = towels.copy()
        i = 0
        while len(tw) > 0:
            nexttw = []
            for t in tw:
                if t == next[:i]:
                    edge.append(t)
                elif t[:i] == next[:i]:
                    nexttw.append(t)

            tw = nexttw
            i += 1
        for e in edge:
            total += ptrn(prev+e,full)
        return total

total = 0
total2 = 0
for pattern in patterns:
    x = ptrn("",pattern)
    if x > 0:
        total += 1
    total2 += x
print(total)
print(total2)






