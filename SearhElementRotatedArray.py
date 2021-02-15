def SearchElementRotatedArray(li, ele):
    beg = 0
    end = len(li) - 1
    while(beg <= end):
        mid = beg + (end - beg) // 2
        if li[mid] == ele:
            return mid
        elif li[beg] < li[mid] and li[beg] <= ele <= li[mid]:
            end = mid - 1
        elif li[mid] < li[end] and li[mid] <= ele <= li[end]:
            beg = mid + 1
        elif li[mid] < li[end]:
            end = mid - 1
        else:
            beg = mid + 1
    return -1

li= list(map(int, input().split()))
ele = int(input())
index = SearchElementRotatedArray(li, ele)
print(index if (index != -1) else "Element Not Found")