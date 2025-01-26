a = []
b = []

with open("day1") as file:
    for row in file:
        a.append(int(row.split()[0]))
        b.append(int(row.split()[1]))

#a = [3,4,2,1,3,3]
#b = [4,3,5,3,9,3]

#part 1
a.sort()
b.sort()

t = 0

for i,j in zip(a,b):
    t += abs(i-j)

print(t)

t = 0

# part 2
for i in a:
    t += i*b.count(i)

print(t)