# begin - номер стартовой вершины; visited - список посещённых вершин; g[i] - множество вершин, смежных с i
asked = [False for i in range(n+1)]
def dfs(begin, asked, g):
	asked[begin] = True
	for i in g[begin]:
		if not asked[i]:
			dfs(u)
