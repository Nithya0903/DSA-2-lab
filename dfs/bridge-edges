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
low = []
def dfs(G,s):
    global time
    v[s].visited = True
    v[s].st = time
    low[s] = time
    time = time +1
    for u in G[s]:
        if v[u].visited == False:
            v[u].parent = s
            low[s] =  min(low[s],dfs(G,u))
            if low[u] > v[s].st:
                print("[ {}, {} ] is a bridge end".format(s,u))

        elif u!= v[s].parent:
            low[s] = min(low[s],v[u].st)
    return low[s]
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
    for i in range(len(G)):
        low.append(-1)
    dfs(G,0)




if __name__ == '__main__':
    main()
