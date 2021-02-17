def PowerSet(s):
    sets = []
    __SetGenerator__(s, 0, [], sets)
    print(sets)

def __SetGenerator__(s, cur, cur_set, sets):
    if cur == len(s):
        sets.append("".join(cur_set))
        return

    cur_set.append(s[cur])
    __SetGenerator__(s, cur + 1, cur_set, sets)
    cur_set.pop()
    __SetGenerator__(s, cur + 1, cur_set, sets)

    

s = list(input().split())
PowerSet(s)