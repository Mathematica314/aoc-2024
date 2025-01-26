import networkx

data = []
with open("day18") as file:
    for line in file:
        data.append([int(x) for x in line.split(",")])

def findpath(data):
    borders = [[0,1],[0,-1],[1,0],[-1,0]]

    gr = networkx.Graph()
    start = (0,0)
    end = (70,70)


    gr.add_node(start)
    visited = [start]

    edge = [start]
    change = True
    while change:
        change = False
        nedge = []
        for e in edge:
            for b in borders:
                if [e[0]+b[0],e[1]+b[1]] not in data and 0 <= e[0] + b[0] <= 70 and 0 <= e[1] + b[1] <= 70 and (e[0]+b[0],e[1]+b[1]) not in visited:
                    gr.add_node((e[0]+b[0],e[1]+b[1]))
                    gr.add_edge(e,(e[0]+b[0],e[1]+b[1]))
                    nedge.append((e[0]+b[0],e[1]+b[1]))
                    visited.append((e[0]+b[0],e[1]+b[1]))
                    change = True
        edge = nedge
    try:
        return networkx.shortest_path(gr,start,end)
    except:
        return -1

path = findpath(data[:1024])
print(len(path))
for i in range(1024,len(data)):
    if tuple(data[i]) in path:
        if findpath(data[:i]) == -1:
            print(f"{data[i-1][0]},{data[i-1][1]}")
            exit()