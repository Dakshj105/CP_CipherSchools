def MergeSortedArray(li, li1):
    i, j = 0, 0
    while(i < len(li) and j < len(li1)):
        if li[i] <= li1[j]:
            print(li[i], end = ' ')
            i += 1
        else:
            print(li1[j], end = " ")
            j += 1
    if i < len(li):
        for i1 in range(i, len(li)):
            print(li[i1], end = ' ')
    elif j < len(li1):
        for j1 in range(j, len(li1)):
            print(li1[j1], end = ' ')

li = list(map(int, input().split()))
li1 = list(map(int, input().split()))
MergeSortedArray(li, li1)