def KSmallestElement(li, k):
    li.sort()
    for i in range(k):
        print(li[i], end= " ")
li = list(map(int, input().split()))
k= int(input())
KSmallestElement(li, k)