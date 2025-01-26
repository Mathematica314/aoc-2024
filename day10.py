grid = []
with open("day10") as file:
    for row in file:
        grid.append([int(x) for x in row.strip("\n")])

def score(grid, address):
    if grid[address[0]][address[1]] == 9:
        return [address]
    else:
        addresses = []
        for i in [[-1,0],[1,0],[0,-1],[0,1]]:
            try:
                if grid[address[0]+i[0]][address[1]+i[1]] == grid[address[0]][address[1]] + 1:
                    addresses = addresses + score(grid,[address[0]+i[0],address[1]+i[1]])
            except:
                pass
        if grid[address[0]][address[1]] == 0:
            na = []
            for i in addresses:
                if i not in na and i[0] >= 0 and i[1] >=0:
                    na.append(i)
            return len(na)
        return addresses

def scorenu(grid, address):
    if grid[address[0]][address[1]] == 9:
        return 1
    else:
        total = 0
        for i in [[-1,0],[1,0],[0,-1],[0,1]]:
            try:
                if grid[address[0]+i[0]][address[1]+i[1]] == grid[address[0]][address[1]] + 1 and address[0]+i[0] >= 0 and address[1]+i[1]>=0:
                    total += scorenu(grid,[address[0]+i[0],address[1]+i[1]])
            except:
                pass
        return total

total1 = 0
total2 = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] == 0:
            total1 += score(grid,[x,y])
            total2 += scorenu(grid,[x,y])
            if scorenu(grid,[x,y]) == 15:
                pass

print(total1)
print(total2)