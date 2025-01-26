import itertools

import networkx

gr = networkx.Graph()

with open("day23") as file:
    for line in file:
        line = line.strip("\n").split("-")
        gr.add_node(line[0])
        gr.add_node(line[1])
        gr.add_edge(line[0],line[1])

total = 0
for c in networkx.simple_cycles(gr,3):
    for node in c:
        if node[0] == "t":
            total += 1
            break
print(total)

tval = max([len(list(gr.neighbors(n))) for n in gr.nodes]) + 1
while True:
    check = []
    for n in gr.nodes:
        nbrs = list(gr.neighbors(n))
        nbrs.append(n)
        if len(nbrs) == tval:
            check.append(nbrs.copy())
        elif len(list(nbrs)) > tval:
            for c in itertools.combinations(nbrs,len(nbrs) - tval):
                n_nbrs = [i for i in nbrs if i not in c]
                check.append(n_nbrs.copy())
    for ch in check:
        for s in ch:
            for e in ch:
                if e != s and not gr.has_edge(e,s):
                    break
            else:
                continue
            break
        else:
            print(sorted(ch).__repr__()[1:-1].replace("\'","").replace(" ",""))
            exit()
    tval -= 1