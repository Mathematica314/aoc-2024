legal = {}
books = []
with open("day5") as file:
    for line in file:
        line = line.strip("\n")
        if "|" in line:
            if int(line.split("|")[0]) in legal.keys():
                legal[int(line.split("|")[0])] = legal[int(line.split("|")[0])] + [int(line.split("|")[1])]
            else:
                legal[int(line.split("|")[0])] = [int(line.split("|")[1])]
        else:
            if line != "":
                books.append([int(x) for x in line.split(",")])

def verifybook(book):
    l = True
    vals = []
    for key in legal.keys():
        if key in book:
            for value in legal[key]:
                if value in book:
                    if book.index(value) < book.index(key):
                        l = False
                        vals.append(value)
    return l, vals

illegals = []
total1 = 0
for book in books:
    if verifybook(book)[0]:
        total1 += book[int((len(book)-1)/2)]
    else:
        illegals.append(book)

total2 = 0
for book in illegals:
    while not verifybook(book)[0]:
        for i in verifybook(book)[1]:
            book.pop(book.index(i))
            book.append(i)
    total2 += book[int((len(book) - 1) / 2)]

print(total1)
print(total2)