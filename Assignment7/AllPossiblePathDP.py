def AllPossiblePath(p, q): 
	table = [1 for i in range(q)] 
	for i in range(p - 1): 
		for j in range(1, q): 
			table[j] += table[j - 1] 
	return table[q - 1] 

print(AllPossiblePath(int(input()), int(input()))) 
