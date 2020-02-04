from collections import deque 
q = deque() 
color =[]
dist=[]
def bfs(G,s):
    n=len(G)
    for i in range(0,n):
        dist.append(0)
    for i in range(0,n):
        color.append("white")
    dist[s] = 0
    color[s] = "grey"
    q.append(s)
    while len(q)!=0:
        n=q.popleft()
        print(n)
        for neighbour in G[n]:
            if color[neighbour] == "white":
                color[neighbour] = "grey"
                q.append(neighbour)
                dist[neighbour] = dist[n]+1
        color[n] = "black"











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
    s = input('Enter source node')
    bfs(G,s)

if __name__ == '__main__':
    main()