no_of_chars = 256
def findSubString(string, pattern):
	len1 = len(string)
	len2 = len(pattern)
	if len1 < len2:
		print("No such window exists")
		return ""

	hash_pattern = [0] * no_of_chars
	hash_string = [0] * no_of_chars
	for i in range(0, len2):
		hash_pattern[ord(pattern[i])] += 1

	start, start_index, min_len = 0, -1, float('inf')
	count = 0
	for j in range(0, len1):
		hash_string[ord(string[j])] += 1
		if (hash_string[ord(string[j])] <=
				hash_pattern[ord(string[j])]):
			count += 1

		if count == len2:
			while (hash_string[ord(string[start])] >
				hash_pattern[ord(string[start])] or
				hash_pattern[ord(string[start])] == 0):

				if (hash_string[ord(string[start])] >
						hash_pattern[ord(string[start])]):
					hash_string[ord(string[start])] -= 1
				start += 1

			len_window = j - start + 1
			if min_len > len_window:

				min_len = len_window
				start_index = start

	if start_index == -1:
		print("No such window exists")
		return ""

	return string[start_index: start_index + min_len]

print(findSubString(input(), input()))