def PathCounter(m, n):
    if m == 0 or n == 0:
        return 1
    return __PossiblePathCount__(m, n)
def __PossiblePathCount__(m, n):
    if m == 1 or n == 1:
        return 1
    
    return __PossiblePathCount__(m-1, n) + __PossiblePathCount__(m, n - 1)

m, n = int(input()), int(input())
print(PathCounter(m, n))