def FindMissingNumber(li, n):
    s = sum(range(1, n+1))
    for i in li:
        s -= i
    return s

li = list(map(int, input().split()))
n = int(input("total elements:- "))
print(FindMissingNumber(li, n))