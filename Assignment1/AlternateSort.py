def AlternateSort(li):
    n = len(li)
    for i in range(n):
        if i == (n - i - 1):
            print(li[i])
            break
        print(li[n - i - 1], end =" ")
        print(li[i], end = " ")
        

li = list(map(int, input().split()))
li.sort()
AlternateSort(li)
