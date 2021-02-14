def KSmallestElement(li, k):
    c = 0
    a = max(li)
    li1 = li[:]
    while(c < k):
        c += 1
        inde = -1
        mini = a
        for i in range(len(li1)):
            if li1[i] <= mini:
                mini = li1[i]
                inde = i
        li1[inde] = a
    del li1
    for i in li:
        if i <= mini:
            print(i, end = " ")

        

li = list(map(int, input().split()))
k= int(input())
KSmallestElement(li, k)
