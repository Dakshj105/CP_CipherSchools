def first(li, element):
    beg = 0
    end = len(li) - 1
    while(beg <= end):
        mid = int(beg + (end - beg) / 2)
        if li[mid] == element and li[mid] != li[mid - 1]:
            return mid
        elif li[mid] >= element:
            end = mid -1
        else:
            beg = mid + 1
    return -1

def last(li, element):
    beg = 0
    end = len(li) - 1
    while(beg <= end):
        mid = int(beg + (end - beg) / 2)
        if li[mid] == element and li[mid] != li[mid + 1]:
            return mid
        elif li[mid] <= element:
            beg = mid + 1
        else:
            end = mid - 1
    return -1

def firstLastPosElementSortedArray(li, element):
    if li[0] == element:
        if li[len(li) - 1] == element:
            return [0, len(li) - 1]
        return  [0, last(li, element)]
    elif li[len(li) - 1] == element:
        return [first(li ,element), len(li) - 1]
    return [first(li, element), last(li, element)]

li = list(map(int, input().split()))
element = int(input())
a = firstLastPosElementSortedArray(li, element)
print(f"first:-> {a[0]} and last:-> {a[1]}" if a != -1 else "Element not found")