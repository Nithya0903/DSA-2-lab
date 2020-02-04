from collections import deque
q = deque()
color = []
dist = []
def bpt(G,s):
    n = len(G)
    for i in range(0,n):
        color.append("white")
        dist.append(-1)
    color[0] = "grey"
    dist[s] = 0
    q.append(s)
    while(len(q)!=0):
        u = q.popleft()
        for v in G[u]:
            if color[v] == "white":
                color[v] = "grey"
                dist[v] = dist[u] +1
                q.append(v)
            else:
                if dist[v] == dist[u]:
                    print("Not bi-partitate")
                    exit()
        color[u] = "black"
    print("Bi-partitate")



def main():
    G = []
    file=open('input.txt','r')
    for line in file:
        line = line.strip()
        adjV = []
        first = True
        for node in line.split(' '):
            if first:
                first = False
                continue
            adjV.append(int(node))
        G.append(adjV)
    file.close()
    print(G)
    bpt(G,0)

if __name__ == '__main__':
    main()
