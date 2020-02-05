class Node:
    def __init__(self,val):
        self.val = val
        self.st = 0
        self.visited = False
        self.et = 0

    def __str__(self):
        return "index: {} Start time: {} End time: {}".format(self.val,self.st,self.et)
G=[]
v=[]
stack = []
time  =0
order = []
def dfs(s):
    global time
    v[s].visited = True
    stack.append(s)
    v[s].st = time
    while len(stack)!=0:
        t = stack.pop()
        order.append(t)
        print(t)
        for u in G[t]:
            if v[u].visited ==False:
                v[u].visited = True
                stack.append(u)

    l = len(G)

    for i in range(0,l):
        v[order[i]].st = i
        v[order[i]].et = 2*l-i-1







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
    s = input("Enter src node")
    s = int(s)
    print("Nodes in order of traversal")
    dfs(0)
    print("Nodes wth starting and ending time")
    for i in range(l):
       print(v[i])


if __name__ =='__main__':
    main()
