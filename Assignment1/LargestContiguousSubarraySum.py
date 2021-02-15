def LargestContiguousSubarraySum(li):
    maxi = li[0]
    maxi2 = li[0]
    for i in range(1, len(li)):
        maxi = max(maxi + li[i], li[i])
        if maxi > maxi2:
            maxi2 = maxi
    return maxi2

li = list(map(int, input().split()))
print(LargestContiguousSubarraySum(li))