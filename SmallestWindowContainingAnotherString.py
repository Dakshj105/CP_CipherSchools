def SmallestWindowContainingAnotherString(st1, st2):
    d = {}
    d1 = {}
    for i in st1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for i in st2:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1

    index_start = 0
    index_end = len(st1) - 1
    i = 0
    j = len(st1) - 1
    
    while(i == index_start):
        if st1[i] in d1:
            if d1[st1[i]] < d[st1[i]]:
                d[st1[i]] -= 1
                index_start += 1        
        else:
            index_start += 1
        i += 1

    while(j == index_end):
        if st1[j] in d1:
            if d1[st1[j]] < d[st1[j]]:
                d[st1[j]] -= 1
                index_end -= 1
        else:
            index_end -= 1
        j -= 1

    return [index_start, index_end + 1] 

        


string1 = input()
string2 = input()
r = SmallestWindowContainingAnotherString(string1, string2)
for i in range(r[0], r[1]):
    print(string1[i], end= "")