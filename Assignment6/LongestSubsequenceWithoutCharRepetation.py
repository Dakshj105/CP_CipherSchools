def longestUniqueSubsttr(string):	
	d = {}
	maxi = 0
	start = 0	
	for end in range(len(string)):
		if string[end] in d:
			start = max(start, d[string[end]] + 1)

		d[string[end]] = end
		maxi = max(maxi, end-start + 1)
	return maxi

string = input()
print(longestUniqueSubsttr(string))