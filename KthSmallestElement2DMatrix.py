def KthSmallestElement2DMatrix(li, k):
    smallest = li[0][0]
    largest = li[-1][-1]
    while(smallest < largest):
        mid = smallest + (largest - smallest) // 2
        c = 0
        for row in li:
            if row[0] > mid:
                continue
            elif row [-1] <= mid:
                c += len(row)
                continue
            l = 0
            r = len(li)
            while(l < r):
                mid1 = l + (r - l ) // 2
                if row[mid1] <= mid:
                    l = mid1 + 1
                else:
                    r = mid1
            c += l
        
        if c < k:
            smallest = mid + 1
        else:
            largest = mid
    return smallest
        



li = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = int(input())
element = KthSmallestElement2DMatrix(li, k)
print(element)