class Node:
    def __init__(self,val):
        self.val = val
        self.st = 0
        self.visited = False
        self.et = 0



G = []
v = []

time  =0
def dfs(s):
    global time
    v[s].st = time
    time = time+1
    v[s].visited = True
    print(v[s].val)
    for u in G[s]:
        if v[u].visited == False:
            dfs(u)
        else:
            print("Cycle detected!!")
            exit()
    v[s].et = time
    time = time+1

def main():
    file=open('input.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for node in line.split(' '):
            if first:
                v.append(Node(int(node)))
                first=False
                continue
            adjacentVertices.append(int(node))
        G.append(adjacentVertices)

    file.close()
    print(G)
    l = len(G)
    for i in range(l):
        v.append(Node(i))
    dfs(0)
    print("No cycle")

if __name__ =='__main__':
    main()
