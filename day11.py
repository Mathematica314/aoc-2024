with open("day11") as file:
    stones = {int(x):1 for x in file.readlines()[0].split()}

for i in range(75):
    nstones = {}
    for i,s in enumerate(stones.keys()):
        if s == 0:
            if 1 not in nstones.keys():
                nstones[1] = stones[s]
            else:
                nstones[1] = nstones[1] + stones[s]
        elif len(str(s))%2 == 0:
            if int(str(s)[int(len(str(s))/2):]) not in nstones.keys():
                nstones[int(str(s)[int(len(str(s)) / 2):])] = stones[s]
            else:
                nstones[(int(str(s)[int(len(str(s))/2):]))] = nstones[(int(str(s)[int(len(str(s))/2):]))] + stones[s]
            if int(str(s)[:int(len(str(s)) / 2)]) not in nstones.keys():
                nstones[int(str(s)[:int(len(str(s)) / 2)])] = stones[s]
            else:
                nstones[(int(str(s)[:int(len(str(s)) / 2)]))] = nstones[(int(str(s)[:int(len(str(s)) / 2)]))] + stones[s]
        else:
            if 2024*s not in nstones.keys():
                nstones[2024*s] = stones[s]
            else:
                nstones[2024 * s] = nstones[2024*s] + stones[s]
    stones = nstones

total = 0
for x in stones.keys():
    total+=stones[x]
print(total)