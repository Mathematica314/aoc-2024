import copy
import random

SWAPS = [["gws","nnt"],["z13","npf"],["z33","hgj"],["z19","cph"]]

invals = True
values = {}

rels = {}

xs = []
ys = []
zs = []

names = {"OR":lambda x,y:x or y, "AND": lambda x,y:x and y, "XOR": lambda x,y:x^y}

lns = []
with open("day24") as file:
    for line in file:
        lns.append(line)
        line = line.strip("\n")
        if line == "":
            invals = False
        elif invals:
            line = line.split(": ")
            values[line[0]] = int(line[1])
            if line[0][0] == "x":
                xs.append(line[0])
            if line[0][0] == "y":
                ys.append(line[0])
        else:
            line = [x for x in line.split(" ") if x != "->"]
            rels[line[3]] = [line[0], line[2], names[line[1]]]
            if line[3][0] == "z":
                zs.append(line[3])

lns = [x.strip("\n") for x in lns]
lns = lns[90:]
lns = lns[1:]
lns.sort()
ins = [l.split() for l in lns]
insn = [l[:3] + [l[-1]] for l in ins]
nins = []
for l in insn:
    if l[0][0] == "y":
        nins.append([l[2], l[1], l[0], l[3]])
    else:
        nins.append(l)

nins.sort()

del file
del lns
del line
del l
del ins
del insn

rins = copy.deepcopy(nins)

for s in SWAPS:
    for l in nins:
        if l[3] == s[0]:
            l[3] = s[1]
        elif l[3] == s[1]:
            l[3] = s[0]


inl = nins[132:]
not_inl = nins[:132]

not_inl.sort(key=lambda x: x[-1])
xydict = {}
for l in inl:
    xydict[l[-1]] = l[0][1:] + l[1][0]

xydict.__delitem__("z00")

not_inl_n = []
for l in not_inl:
    row = []
    for r in l:
        if r in xydict.keys():
            row.append(xydict[r])
        else:
            row.append(r)
    not_inl_n.append(row)

not_inl_n.sort()
not_inl = not_inl_n
del not_inl_n
del r
del row
del l
not_inl_n = []
nums = "0123456789"
for r in not_inl:
    if r[0][0] in nums and r[2][0] not in nums:
        not_inl_n.append(r)
    elif r[0][0] not in nums and r[2][0] not in nums:
        not_inl_n.append(r)
    elif r[0][0] not in nums and r[2][0] in nums:
        not_inl_n.append([r[2], r[1], r[0], r[3]])
    else:
        if r[0][2] == "A":
            not_inl_n.append(r)
        else:
            not_inl_n.append([r[2], r[1], r[0], r[3]])

not_inl_n.sort()
not_inl = not_inl_n
del not_inl_n
del r
del nums
l0 = inl
l1 = not_inl
del inl
del not_inl
a = [[l1[0][2], l1[0][1], l1[0][0], l1[0][3]], [l1[1][2], l1[1][1], l1[1][0], l1[1][3]]]
l1[0] = a[0]
l1[1] = a[1]
l1.sort()
l1.sort(key=lambda x: x[-1])
l2 = l1[87:]
l1 = l1[:87]
del a

l1.sort()
l1dict = {}
for l in l1:
    l1dict[l[3]] = l[0] + l[1][0]

nl1 = []
for l in l1:
    row = []
    for a in l:
        if a in l1dict.keys():
            row.append(l1dict[a])
        else:
            row.append(a)
    nl1.append(row)

nl1.sort()
del row
del a
del l

nl2 = []
for l in l2:
    row = []
    for r in l:
        if r in l1dict.keys():
            row.append(l1dict[r])
        else:
            row.append(r)
    nl2.append(row)

nl0 = []
for l in l0:
    row = []
    for r in l:
        if r in xydict.keys():
            row.append(xydict[r])
        else:
            row.append(r)
    nl0.append(row)
ins = nins
del nins
del l
del r

#HAVE A MANUAL LOOK - very important step

zs.sort()

def calc(rels,values,zmax):
    zs = {f"z{str(k).zfill(2)}":v for k,v in enumerate([False for _ in range(zmax)])}
    while not min([z in values.keys() for z in zs]):
        changed = []
        for r in rels.keys():
            if rels[r][0] in values and rels[r][1] in values:
                values[r] = rels[r][2](values[rels[r][0]],values[rels[r][1]])
                changed.append(r)
        rels = {k:v for k,v in zip(rels.keys(),rels.values()) if k not in changed}
        if not changed:
            return [2 for _ in zs]
    return [values[z] for z in zs]

def verify(rels,xmax,ymax,zmax,cond,verifynum):
    for _ in range(verifynum):
        x = random.randrange(0,2**xmax)
        y = random.randrange(0,2**ymax)
        xb = bin(x)[2:].zfill(xmax)
        yb = bin(y)[2:].zfill(ymax)
        vals = {f"x{str(k).zfill(2)}":int(v) for k,v in enumerate(xb[::-1])} | {f"y{str(k).zfill(2)}":int(v) for k,v in enumerate(yb[::-1])}
        if "".join([str(x) for x in calc(rels,vals,zmax)])[::-1] != bin(cond(x,y))[2:].zfill(zmax):
            return False
    return True

xmax = len(xs)
ymax = len(ys)
zmax = len(zs)

nrels = {x[3]:[x[0],x[2],names[x[1]]] for x in ins}

print(int("".join([str(x) for x in calc(rels,values,zmax)[::-1]]),2))

if verify(nrels,xmax,ymax,zmax,lambda a,b:a+b,50000):
    out = []
    for x in SWAPS:
        out.append(x[0])
        out.append(x[1])
    print(sorted(out).__repr__()[1:-1].replace("\'","").replace(" ",""))
else:
    print("Wrong")