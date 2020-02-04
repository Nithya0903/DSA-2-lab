from collections import deque 
q = deque()
color = []
cl =[]
count =0


def bfs(G,s):
    if color[s] == "white":
        global count
        count = count+1
        cl[s] = count
        n=len(G)
        color[s] = "grey"
        q.append(s)
        while len(q)!=0:
            n=q.popleft()
            cl[n] = count

            for neighbour in G[n]:
                if color[neighbour] == "white":
                    color[neighbour] = "grey"
                    cl[neighbour] = count
                    q.append(neighbour)
            color[n] = "black"


def cc(G):

    n=len(G)
    for i in range(0,n):
        color.append("white")
    for i in range(0,n):
        cl.append(0)
    for i in range(0,n):
        bfs(G,i)


def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 

    file=open('input.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for node in line.split(' '):
            if first:
                first=False
                continue
            adjacentVertices.append(int(node))
        G.append(adjacentVertices)

    file.close()

    print(G)
    cc(G)
    n=len(G)
    for i in range (n):
        for k in range(n):
            if cl[k] == i:
                print(k,end = " ")
        print(" ")

if __name__ == '__main__':
    main()