import sympy

games = []
row = 0
game = []

with open("day13") as file:
    for line in file:
        line = line.strip("\n")
        if row == 0:
            game = [[int(x[2:]) for x in line[10:].split(", ")]]
        elif row == 1:
            game.append([int(x[2:]) for x in line[10:].split(", ")])
        elif row == 2:
            game.append([int(x[2:]) for x in line[7:].split(", ")])
        else:
            games.append(game)
        row = (row+1)%4
games.append(game)
total = 0
isPartB = True

for game in games:
    if isPartB:
        game[2] = [i + 10000000000000 for i in game[2]]
    a,b = sympy.symbols("a,b")
    eq1 = sympy.Eq(game[0][0]*a + game[1][0]*b,game[2][0])
    eq2 = sympy.Eq(game[0][1] * a + game[1][1] * b, game[2][1])
    sol = sympy.solve([eq1,eq2],(a,b))
    if sol[a].is_integer and sol[b].is_integer and sol[a] > 0 and sol[b] > 0:
        total += sol[a]*3 + sol[b]
print(total)

