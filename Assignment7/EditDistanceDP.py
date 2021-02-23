def EditDistance(str1, str2):
	len1 = len(str1)
	len2 = len(str2)
	table = [[0 for i in range(len1 + 1)] for j in range(2)]
	for i in range(0, len1 + 1):
		table[0][i] = i

	for i in range(1, len2 + 1):
		for j in range(0, len1 + 1):
			if (j == 0):
				table[i % 2][j] = i

			elif(str1[j - 1] == str2[i-1]):
				table[i % 2][j] = table[(i - 1) % 2][j - 1]

			else:
				table[i % 2][j] = (1 + min(table[(i - 1) % 2][j], 
									min(table[i % 2][j - 1], 
								table[(i - 1) % 2][j - 1])))

	print(table[len2 % 2][len1], "")

EditDistance(input(), input())