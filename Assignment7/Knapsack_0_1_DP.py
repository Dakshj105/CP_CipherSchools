def knapsack(wt, val, W, n):
	if n == 0 or W == 0:
		return 0

	if table[n][W] != -1:
		return table[n][W]

	if wt[n-1] <= W:
		table[n][W] = max(
			val[n-1] + knapsack(
				wt, val, W-wt[n-1], n-1),
			knapsack(wt, val, W, n-1))
		return table[n][W]
        
	elif wt[n-1] > W:
		table[n][W] = knapsack(wt, val, W, n-1)
		return table[n][W]

val = [60, 100, 120 ]
wt = [10, 20, 30 ]
W = 50
n = len(val)
table = [[-1 for i in range(W + 1)] for j in range(n + 1)]
print(knapsack(wt, val, W, n))