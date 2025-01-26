import math

inputs = []
total1 = 0
total2 = 0

def ternary(x):
    out = ""
    if x == 0: return "0"
    while x >= 1:
        x = x/3
        out = str(int(round((3*(x-math.floor(x)))))) + out
        x = math.floor(x)
    return out

with open("day7") as file:
    for b, row in enumerate(file):
        print(b)
        target, nums = row.split(":")
        target = int(target)
        nums = [int(x) for x in nums.split()]
        for i in range(2**(len(nums)-1)):
            calc = 0
            pattern = str(format(i,"b"))
            for _ in range(len(nums) - len(pattern)):
                pattern = "0" + pattern
            for j,space in enumerate(pattern):
                if space == "0":
                    calc = calc + nums[j]
                else:
                    calc = calc * nums[j]
            if calc == target:
                total1 += target
                break
        for i in range(3**(len(nums)-1)):
            calc = 0
            pattern = ternary(i)
            for _ in range(len(nums) - len(pattern)):
                pattern = "0" + pattern
            for j,space in enumerate(pattern):
                if space == "0":
                    calc = calc + nums[j]
                elif space == "1":
                    calc = calc * nums[j]
                else:
                    calc = int(str(calc)+str(nums[j]))
            if calc == target:
                total2 += target
                break

print(total1)
print(total2)