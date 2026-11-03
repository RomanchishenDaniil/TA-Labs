class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = []
		self.parent = list(range(vertices))

	def add_edge(self, u, v, w):
		self.graph.append((w, u, v))

	def find_set(self, i):
		if self.parent[i] == i:
			return i
		return self.find_set(self.parent[i])

	def union_set(self, u, v):
		self.parent[u] = self.parent[v]

	def kruskal(self):
		mst = []
		self.graph.sort()
		
		for w, u, v in self.graph:
			u_rep = self.find_set(u)
			v_rep = self.find_set(v)
			
			if u_rep != v_rep:
				mst.append((u, v, w))
				self.union_set(u_rep, v_rep)

		print("Edge : Weight")
		for u, v, w in mst:
			print(f"{u + 1} - {v + 1} : {w}")


g = Graph(8)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 5)
g.add_edge(0, 3, 7)
g.add_edge(0, 6, 10)
g.add_edge(1, 4, 8)
g.add_edge(2, 4, 2)
g.add_edge(2, 5, 4)
g.add_edge(2, 6, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 5)
g.add_edge(3, 6, 9)
g.add_edge(4, 5, 3)
g.add_edge(5, 7, 1)
g.add_edge(6, 7, 6)

g.kruskal()
