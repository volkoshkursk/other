def bfs(V, n):
	D = [None for i in range(n+1)]
	D[beg] = 0
	Q = [beg]
	Qbeg = 0
	while Qbeg < len(Q):
		i = Q[Qbeg]
		Qbeg += 1 
		for j in V[i]: 
			if D[j] is None: 
				D[j] = D[i] + 1 
				Q.append(j)
	return D