def FindMajorityElement(li):
    maj_val = 1
    maj_index = li[0]
    for i in range(1,len(li)):
        if maj_val == 0:
            maj_index = i
            maj_val = 1
            continue
        if li[i] == li[maj_index]:
            maj_val+=1
        else:
            maj_val-=1
    return li[maj_index] if maj_val != 0 else -1       

li = list(map(int, input().split()))
maj_element = FindMajorityElement(li)
print(maj_element if (maj_element != -1 and li.count(maj_element) > int(len(li) / 2)) else "No Majority Element")