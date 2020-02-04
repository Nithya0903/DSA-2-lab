
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
treeedge=[]
backedge=[]
vs=[]

def dfs(s) :
	global tim
	v[s].visited=1
	v[s].st=tim;
	tim=tim+1;
	for u in G[s] :
		if v[u].visited == 0 :
			treeedge.append([s,u])
			v[u].parent=s
			dfs(u)
		elif v[s].parent!=u and v[u].parent!=u :
			backedge.append([u,v[u].parent])
	v[s].ft=tim
	tim=tim+1
	print(v[s])




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
    dfs(s)
    print("tree edge :",treeedge,"\nback edge :",backedge)


if __name__ == '__main__':
    main()