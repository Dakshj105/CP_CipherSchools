def CountingInversion(li):

    return mergeSort(li, [0] * len(li), 0, len(li) - 1)

def mergeSort(li, li1, l, r):

    inv_count = 0
    
    if l < r:

        mid = l + (r - l) // 2
        inv_count += mergeSort(li, li1, l, mid)
        inv_count += mergeSort(li, li1, mid + 1, r)
        inv_count += merge(li, li1, l, mid, r)
    return inv_count

def merge(li, li1, l, mid, r):
    i = l    
    j = mid + 1 
    k = l     
    inv_count = 0

    while i <= mid and j <= r:

        if li[i] <= li[j]:
            li1[k] = li[i]
            k += 1
            i += 1
        else:
            li1[k] = li[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1

    while i <= mid:
        li1[k] = li[i]
        k += 1
        i += 1

    while j <= r:
        li1[k] = li[j]
        k += 1
        j += 1

    for i in range(l, r + 1):
        li[i] = li1[i]
        
    return inv_count
    
   

li = list(map(int, input().split()))
print(CountingInversion(li))