def AllPossibleDecoding(n, length):
    if 0 <= length <= 1 :
        return 1
    c = 1
    if n[length - 1] != '0':
        c += AllPossibleDecoding(n, length - 1)
    if 0 <= int(n[length - 2] + n[length - 1]) <= 26:
        c += AllPossibleDecoding(n, length - 2)

    return c

n = input()
length = len(n)
print(AllPossibleDecoding(n, length))