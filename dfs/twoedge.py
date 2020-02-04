class Node:
    def __init__(self,val):
        self.val = val
        self.st = 0
        self.et = 0
        self.parent = -1
        self.visited = False
time = 0
v = []
def min(i,j) :
    if(i>j) :
        return j
    else :
        return i

def twEdge(G,s):
    global time
    v[s].visited = True
    v[s].st = time
    sst = v[s].st
    time = time+1
    for u in G[s]:
        print(s,u)
        if v[u].visited == False:
            v[u].parent = s
            sst = min(twEdge(G,u),sst)
        elif v[s].parent != u:
            sst = min(v[u].st,sst)
    v[s].ft =  time
    time = time +1
    print(sst)
    if sst == v[s].st and v[s].st!=0:
        print("Not 2 edge connected")
        exit()
    return sst


def main():
    G = []
    file=open('input.txt','r')
    for line in file:
        line = line.strip()
        first = True
        adjV = []
        for nd in line.split():
            if first:
                first = False
                continue
            adjV.append(int(nd))
        G.append(adjV)
    file.close()
    l = len(G)
    print(G)
    for i in range(l):
        v.append(Node(i))
    w = twEdge(G,0)
    print("2  edge connected!")
if __name__ == '__main__':
    main()
