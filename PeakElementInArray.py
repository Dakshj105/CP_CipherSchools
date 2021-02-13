def ModifiedBinarySearch(li):
    beg = 0
    end = len(li) - 1
    while(beg<=end):
        mid = int(beg + (end - beg) / 2)
        if li[mid] > li[mid - 1] and li[mid] > li[mid + 1]:
            return li[mid]
        elif mid > 0 and li[mid] < li[mid - 1]:
            end = mid -1
        else:
            beg = mid + 1
    return -1

def PeakElementInArray(li):
    if len(li) == 0:
        return "empty list"
    elif len(li) == 1:
        return li[0]
    elif li[0] > li[1]:
        return li[0]
    elif li[len(li) - 1] > li[len(li) - 2]:
        return li[len(li) - 1]
    else:
        a = ModifiedBinarySearch(li)
        return a if a != -1 else li[0]

li = list(map(int, input().split()))
ele = PeakElementInArray(li)
print(ele)