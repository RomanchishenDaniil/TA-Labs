import heapq

INF = float('inf')

G = {
	1: [(2, 2), (3, 5), (4, 7), (7, 8)],
	2: [(1, 2), (5, 8)],
	3: [(1, 5), (5, 2), (6, 4), (7, 4)],
	4: [(1, 7), (5, 9), (6, 5), (7, 9)],
	5: [(2, 8), (3, 2), (4, 9), (6, 3)],
	6: [(3, 4), (4, 5), (5, 3), (8, 1)],
	7: [(1, 8), (3, 4), (4, 9), (8, 6)],
	8: [(6, 1), (7, 6)]
}

def dijkstra(graph, s):
	pred = {v: -1 for v in graph}
	dist = {v: INF for v in graph}
	dist[s] = 0
	
	pq = []
	for v in graph:
		heapq.heappush(pq, (dist[v], v))
		
	while pq:
		d_u, u = heapq.heappop(pq)
		
		if d_u > dist[u]:
			continue
			
		for v, weight in graph[u]:
			if dist[v] > dist[u] + weight:
				dist[v] = dist[u] + weight
				pred[v] = u
				heapq.heappush(pq, (dist[v], v))
				
	return pred, dist

def reconstruct_path(pred, start, target):
	path = []
	curr = target
	while curr != -1:
		path.append(str(curr))
		curr = pred[curr]
	return " -> ".join(reversed(path))

start_node = 1
pred, dist = dijkstra(G, start_node)

print(f"Найкоротші шляхи від вершини {start_node}:")
print("-" * 55)
print(f"{'З вершини':<12} | {'У вершину':<12} | {'Шлях':<18} | {'Вага'}")
print("-" * 55)
for v in sorted(G.keys()):
	if v != start_node:
		path_str = reconstruct_path(pred, start_node, v)
		print(f"{start_node:<12} | {v:<12} | {path_str:<18} | {dist[v]}")
