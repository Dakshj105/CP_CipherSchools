def PalindromePartition(s):
    all_palindromes = []
    __GeneratePalindrome__(s, 0, [], all_palindromes)
    print(all_palindromes)

def __GeneratePalindrome__(s, cur, cur_palindrome, all_palindromes):
    if cur == len(s):
        all_palindromes.append(" ".join(cur_palindrome))
        return

    for i in range(cur, len(s)):
        if isValid(s, cur, i):
            cur_palindrome.append(s[cur: i + 1])
            #print(cur_palindrome, "\n")
            __GeneratePalindrome__(s, i + 1, cur_palindrome, all_palindromes)
            cur_palindrome.pop()

def isValid(s, start, end):
    while(start < end):
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

s = input()
PalindromePartition(s)