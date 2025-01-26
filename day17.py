with open("day17") as file:
    for row in file:
        row = row.strip("\n")
        if "A" in row:
            a = int(row.split()[-1])
        elif "B" in row:
            b = int(row.split()[-1])
        elif "C" in row:
            c = int(row.split()[-1])
        elif "P" in row:
            program = [int(x) for x in row.split(" ")[-1].split(",")]

def combo(a,b,c,o):
    if o < 4:
        return o
    else:
        return {4:a,5:b,6:c}[o]

def jnz(a,b,c,o,p):
    if a == 0:
        return [a,b,c,p]
    else:
        return [a,b,c,o-2]

def xor(x,y):
    x = str(x).zfill(len(str(y)))
    y = str(y).zfill(len(x))
    out = ""
    table = {
        ("0","0"):"0",
        ("0","1"):"1",
        ("1","0"):"1",
        ("1","1"):"0"
    }
    for a,b in zip(x,y):
        out = out + table[(a,b)]
    return out


opcodes = {
    0: lambda a,b,c,o,p: [int(a/(2**combo(a,b,c,o))),b,c,p,None],
    1: lambda a,b,c,o,p: [a,int(xor(int(bin(b)[2:]),int(bin(o)[2:])),2),c,p,None],
    2: lambda a,b,c,o,p: [a,combo(a,b,c,o)%8,c,p,None],
    3: lambda a,b,c,o,p: jnz(a,b,c,o,p) + [None],
    4: lambda a,b,c,o,p: [a,int(xor(int(bin(b)[2:]),int(bin(c)[2:])),2),c,p,None],
    5: lambda a,b,c,o,p: [a,b,c,p,combo(a,b,c,o)%8],
    6: lambda a,b,c,o,p: [a,int(a/(2**combo(a,b,c,o))),c,p,None],
    7: lambda a,b,c,o,p: [a,b,int(a/(2**combo(a,b,c,o))),p,None]
}

def prog(a,b,c,program):
    p = 0
    output = []
    while p<len(program):
        a,b,c,p,out = opcodes[program[p]](a,b,c,program[p+1],p)
        if out is not None:
            output.append(out)
        p += 2
    return output

output = prog(a,b,c,program)
for i,j in enumerate(output):
    if i < len(output)-1:
        print(j,end=",")
    else:
        print(j)

def trysol(tried,desired):
    a = 0
    for i,_ in enumerate(desired):
        for j in range(tried[i],8):
            na = a*8 + j
            x = prog(na,0,0,desired)
            if x == desired[-(i+1):]:
                a = na
                tried[i] = j
                if i == len(tried)-1:
                    print(int("".join([str(x) for x in tried]),8))
                    exit()
                break
            if j == 7:
                tried[i] = 0
                tried[i-1] += 1
                trysol(tried,desired)

trysol([0 for i in program],program)