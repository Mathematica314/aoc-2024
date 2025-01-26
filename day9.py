memory1 = []
memory2 = []
gaps = []

with open("day9") as file:
    for line in file:
        gap = False
        index = 0
        for char in line:
            if gap:
                for i in range(int(char)):
                    memory1.append(None)
                if int(char) > 0:
                    memory2.append((-1,int(char)))
            else:
                for i in range(int(char)):
                    memory1.append(index)
                memory2.append((index, int(char)))
                index += 1
            gap = not gap

mi = index

def removenones(mem):
    b = None
    while b is None:
        b = mem.pop(-1)
    mem.append(b)
    return mem

for i,block in enumerate(memory1):
    if block is None:
        memory1.pop(i)
        memory1 = removenones(memory1)
        memory1.insert(i, memory1.pop(-1))

for l in range(mi-1,0,-1):
    if l%100 == 0:
        print(f"{mi-l}/{mi}")
    for i,block in enumerate(memory2):
        if block[0] == l:
            index = i
    end = -1
    for i,block in enumerate(memory2[:index]):
        if block[0] == -1 and block[1] >= memory2[index][1]:
            val = memory2.pop(index)
            memory2[i] = (-1,block[1]-val[1])
            memory2.insert(i,val)
            memory2.insert(index+1,(-1,val[1]))
            break

print(memory2)




total1 = 0
for i,m in enumerate(memory1):
    total1 += i*m

total2 = 0
i = 0
m2p = []
for b in memory2:
    for _ in range(b[1]):
        if b[0] == -1:
            m2p.append(None)
        else:
            m2p.append(b[0])

for i,b in enumerate(m2p):
    if b is not None:
        total2 += i*b


print(total1)
print(total2)