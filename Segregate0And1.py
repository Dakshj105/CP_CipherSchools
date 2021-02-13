def Segregate0And1(li):
    i = 0
    j = len(li) - 1
    while(i < j):
        if li[i] == 1 and li[j] ==0:
            li[i], li[j] = li[j], li[i]
        if li[i] == 0:
            i += 1
        if li[j] == 1:
            j -= 1

li = list(map(int, input().split()))
Segregate0And1(li)
for i in li:
    print(i, end= " ")