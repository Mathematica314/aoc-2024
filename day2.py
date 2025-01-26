total1 = 0
total2 = 0
def allowed(row):
    allowed = True
    prev = 0
    if list(sorted(row)) == row or list(sorted(row, reverse=True)) == row:
        for i, num in enumerate(row):
           if (abs(num - prev) > 3 or abs(num - prev) < 1) and i != 0:
                allowed = False
           prev = int(num)
        return allowed

with open("day2") as file:
    for line in file:
        allowed2 = False
        if allowed([int(i) for i in line.split()]):
            total1 += 1
            allowed2 = True
        for index in range(len(line.split())):
            l2 = [int(x) for x in line.split()[:index] + line.split()[(index+1):]]
            if allowed(l2):
                allowed2= True
        if allowed2:
            total2 += 1

print(total1)
print(total2)

