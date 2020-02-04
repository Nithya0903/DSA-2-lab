
class vertex :
    def __init__(self,val) :
        self.node=val
        self.visited=0
        self.st=0
        self.ft=0
        self.parent=0
    def __str__(self) :
        return str(self.node)+" "+str(self.st)+" "+str(self.ft)
tim=0;
G = [] 
v=[]


def min(i,j) :
    if(i>j) :
        return j
    else :
        return i

def tec(s,ss) :
    global tim
    v[s].visited=1
    v[s].st=tim;
    tim=tim+1;
    sst=v[s].st;
    for u in G[s] :
        print(s,u)
        if v[u].visited == 0 :
            print("not visited :",s,u)
            v[u].parent=s
            sst=min(tec(u,ss),sst)
        elif v[s].parent!=u :
            print("visited :",u,v[u].parent)
            sst=min(v[u].st,sst)
    v[s].ft=tim
    tim=tim+1
    if sst==v[s].st and s!=ss :
        print("not two edge connected")
        exit(-1)
    return sst




def main():
    ''' Adjacency List representation. G is a list of lists. '''

    file=open('input.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for node in line.split(' '):
            if first:
                v.append(vertex(int(node)))
                first=False
                continue
            adjacentVertices.append(int(node))
        G.append(adjacentVertices)

    file.close()
    print(G)
    s=input("\n source vertex")
    s=int(s)
    n=tec(s,s)
    print("two edge connected")
    #print("tree edge :",treeedge,"\nback edge :",backedge)


if __name__ == '__main__':
    main()