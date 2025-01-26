import numpy as np

total1 = 0

crossword = []
with open("day4") as file:
    for row in file:
        line = []
        for char in row.strip("\n"):
            line.append(char)
        crossword.append(line)

arr = np.array(crossword)

def check(row):
    total = 0
    for index in range(len(row)):
        if "".join(row[index:index+4]) == "XMAS":
            total += 1
        if "".join(row[index:index+4]) == "SAMX":
            total += 1
    return total

for row in arr:
    total1 += check(row)

for column in np.rot90(arr):
    total1 += check(column)

for i in range(-len(arr[0]),len(arr[0])):
    total1 += check(arr.diagonal(i))

for i in range(-len(arr),len(arr)):
    total1 += check(np.rot90(arr).diagonal(i))

total2 = 0
corners = [[-1,-1],[1,-1],[-1,1],[1,1]]
for i,row in enumerate(arr[1:-1]):
    for j,letter in enumerate(row[1:-1]):
        if letter == "A":
            ltrs = []
            for corner in corners:
                try:
                    ltrs.append(arr[i+corner[0]+1][j+corner[1]+1])
                except:
                    pass
            if ltrs.count("M") == 2 and ltrs.count("S") == 2 and ltrs[0]!=ltrs[3]:
                total2 += 1
                for row in arr[i:i+3]:
                    for char in row[j:j+3]:
                        print(char,end=" ")
                    print()
                print([str(x) for x in ltrs])


print(total2)
