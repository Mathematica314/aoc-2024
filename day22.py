import math

buyers = []
with open("day22") as file:
    for line in file:
        buyers.append(int(line))


def mix(x,y):
    x = bin(int(x))[2:]
    y = bin(int(y))[2:]
    x = str(x).zfill(len(str(y)))
    y = str(y).zfill(len(x))
    out = ""
    table = {
        ("0", "0"): "0",
        ("0", "1"): "1",
        ("1", "0"): "1",
        ("1", "1"): "0"
    }
    for a, b in zip(x, y):
        out = out + table[(a, b)]
    return int(out,2)

def prune(x):
    return x%16777216

def next(x):
    x = prune(mix(x*64, x))
    x = prune(mix(math.floor(x / 32), x))
    x = prune(mix(x * 2048, x))
    return x

def score(seq):
    score = 0
    for pr,cr in zip(prices,changes):
        for i in range(len(cr)):
            if cr[i:i+4] == seq:
                score+=pr[i+4]
                break
    return score


prices = []
changes = []
total = 0
for b in buyers:
    print(total)
    prev = 0
    changerow = []
    pricerow = []
    for i in range(2000):
        x = int(str(b)[-1])
        changerow.append(x - prev)
        pricerow.append(x)
        prev = x
        b = next(b)
    changes.append(changerow)
    prices.append(pricerow)
    changerow.pop(0)
    total += b
print(total)

max = 0
for a in range(-9,10):
    for b in range(-9, 10):
        for c in range(-9, 10):
            for d in range(-9, 10):
                res = score([a,b,c,d])
                if res > max:
                    max = res
print(max)