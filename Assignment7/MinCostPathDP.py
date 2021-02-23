def minCost(cost, row, col):
	
	for i in range(1, row):
		cost[i][0] += cost[i - 1][0]

	for j in range(1, col):
		cost[0][j] += cost[0][j - 1]

	for i in range(1, row):
		for j in range(1, col):
			cost[i][j] += (min(cost[i - 1][j - 1], 
						min(cost[i - 1][j],
							cost[i][j - 1])))

	return cost[row - 1][col - 1]
	
row = int(input())
column = int(input())
table = [list(map(int, input().split())) for i in range(row)]
print(minCost(table, row, column))