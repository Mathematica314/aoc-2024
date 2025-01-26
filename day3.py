doing = True

def mul(a,b):
    return a*b
def do():
    return True
def dont():
    return False

total1 = 0
total2 = 0

with open("day3") as file:
    for line in file:
        for char in range(len(line)):
            for length in range(4,13):
                try:
                    string = line[char:char+length]
                    for c in string:
                        if c not in "1234567890mul(),don't":
                            raise Exception
                    string = string.replace("don't","dont")
                    if "d" in string and "(" in string and "," not in string:
                        exec(f"doing = {string}")
                    elif doing:
                        exec(f"total2 += {string}")
                    if "d" not in string:
                        exec(f"total1+={string}")

                except:
                    pass

print(total1)
print(total2)