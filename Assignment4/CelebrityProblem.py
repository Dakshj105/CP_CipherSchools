from queue import LifoQueue

def CelebrityProblem(li, n):
    stack = LifoQueue()
    for i in range(n):
        stack.put(i)
    if n == 1:
        return "No Celebrity"
    ele = None
    while(stack.empty() == False):
        ele1 = stack.get()
        if stack.empty():
            return "No Celebrity"
        ele2 = stack.get()
        if li[ele1][ele2]:
            ele = ele2
        else:
            ele = ele1
        if stack.empty():
            break
        stack.put(ele)
    del stack
    sum_i = 0
    sum_j = 0
    for i in range(n):
        sum_i += li[ele][i]
        sum_j += li[i][ele]

    if sum_i == 0 and sum_j == n - 1:
        return f"Celebrity is:- {ele}"
    else:
        return "No Celebrity"



n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))
print(CelebrityProblem(li, n))
