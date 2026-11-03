INF = float('inf')
V = 8

G = [
    [INF, 2, 5, 7, INF, INF, 10, INF],
    [2, INF, INF, INF, 8, INF, INF, INF],
    [5, INF, INF, INF, 2, 4, 4, INF],
    [7, INF, INF, INF, 9, 5, 9, INF],
    [INF, 8, 2, 9, INF, 3, INF, INF],
    [INF, INF, 4, 5, 3, INF, INF, 1],
    [10, INF, 4, 9, INF, INF, INF, 6],
    [INF, INF, INF, INF, INF, 1, 6, INF]
]

selected = [False] * V
selected[0] = True
no_edge = 0

print("Edge : Weight")
while no_edge < V - 1:
    min_val = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and G[i][j] < min_val:
                    min_val = G[i][j]
                    x = i
                    y = j
    
    print(f"{x + 1} - {y + 1} : {G[x][y]}")
    selected[y] = True
    no_edge += 1
