INF = float('inf')
V = 8

W = [
	[0,   2,   5,   7,   INF, INF, 8,   INF],
	[2,   0,   INF, INF, 8,   INF, INF, INF],
	[5,   INF, 0,   INF, 2,   4,   4,   INF],
	[7,   INF, INF, 0,   9,   5,   9,   INF],
	[INF, 8,   2,   9,   0,   3,   INF, INF],
	[INF, INF, 4,   5,   3,   0,   INF, 1  ],
	[8,   INF, 4,   9,   INF, INF, 0,   6  ],
	[INF, INF, INF, INF, INF, 1,   6,   0  ]
]

def floyd(weights):
	n = len(weights)
	D = [row[:] for row in weights]
	
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if D[i][k] + D[k][j] < D[i][j]:
					D[i][j] = D[i][k] + D[k][j]
	return D

def print_matrix(matrix):
	header = "     " + " ".join(f"{j+1:>4}" for j in range(V))
	print(header)
	print("    " + "-" * (len(header) - 4))
	for i, row in enumerate(matrix):
		row_str = " ".join(f"{(val if val != INF else 'INF'):>4}" for val in row)
		print(f"{i+1:>2} | {row_str}")

D_final = floyd(W)

print("Результуюча матриця найкоротших відстаней D^(8) (Алгоритм Флойда):")
print_matrix(D_final)
