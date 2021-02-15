def Segregate0_1_2(li):
    i = 0
    j = 0
    k = len(li) - 1
    while(j <= k):
        if li[j] == 0:
            li[i], li[j] = li[j], li[i]
            i += 1
        elif li[j] == 1:
            j += 1
        else:
            li[j], li[k] = li[k], li[j]
            k -= 1
    return li


li = list(map(int, input().split()))
li = Segregate0_1_2(li)
for i in li:
    print(i, end = " ")