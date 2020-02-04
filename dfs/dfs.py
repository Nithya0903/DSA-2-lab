class Node:
    def __init__(self,val):
        self.st = 0
        self.ft = 0
        self.no = val
        self.visited = False
        self.parent = -1
    def __str__(self):
        return 'index: {}, start time:{}, end time:{}'.format(self.no,self.st,self.ft)
time = 0 #to maintain timestamp
v= [] #a list of class node instances
tEdge =[]
bEdge =[]
def dfs(G,s):
    global time
    v[s].visited = True
    v[s].st = time
    time = time +1
    print(s)
    for u in G[s]:
        if v[u].visited == False:
            v[u].parent = s
            tEdge.append([s,u])
            dfs(G,u)
        else:
            if v[u].parent != s and v[s].parent !=u :
                bEdge.append([v[u].parent,u])
    v[s].ft = time
    time = time +1




def main():
    G = []
    file=open('input.txt','r')
    for line in file:
        line = line.strip()
        adjV =[]
        first = True
        for nd in line.split(' '):
            if first:
                first = False
                continue
            adjV.append(int(nd))
        G.append(adjV)
    file.close()
    print(G)
    for i in range(0,len(G)):
        v.append(Node(i))
    s = input("Enter src")
    s = int(s)
    print("Nodes in traversal order:")
    dfs(G,s)
    for i in range(len(G)):
        print(v[i])
    print("Tree edges")
    for i in range(len(tEdge)):
        print(tEdge[i])
    print("Back edges")
    for i in range(len(bEdge)):
        print(bEdge[i])


if __name__ == '__main__':
    main()
