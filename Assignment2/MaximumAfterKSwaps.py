def MaximumValueAfterKSwaps(s, k):
    maxi = [s]
    MaximumAfterKSwaps(s, k, maxi)
    print(maxi[0])

def MaximumAfterKSwaps(s, k, maxi):
    if s > maxi[0]:
        maxi[0] = s
    if k == 0:
        return

    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            s = s[:i] + s[j] + s[i + 1 : j] + s[i] + s[j + 1:]
            MaximumAfterKSwaps(s, k - 1, maxi)
            s = s[:i] + s[j] + s[i + 1 : j] + s[i] + s[j + 1:]

s = input()
k = int(input())
MaximumValueAfterKSwaps(s, k)