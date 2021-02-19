from queue import LifoQueue

def reverseStack(s):
    if not s.empty():
        ele = s.get()
        reverseStack(s)
        AppendAtBottom(s, ele)

def AppendAtBottom(s, ele):
    if s.empty():
        s.put(ele)

    else:
        temp = s.get()
        AppendAtBottom(s, ele)
        s.put(temp)
    
def MergeOverLappingInterval(li, n):
    stack = LifoQueue()
    li.sort()
    stack.put(li[0][0])
    stack.put(li[0][1])
    for i in range(1, n):
        if li[i][0] > stack.queue[-1]:
            stack.put(li[i][0])
            stack.put(li[i][1])

        elif li[i][0] <= stack.queue[-1] and li[i][1] > stack.queue[-1]:
            stack.get()
            stack.put(li[i][1])
    li = []
    reverseStack(stack)
    while(stack.empty()):
        print(f"[{stack.get()} {stack.get()}]")
    return


n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))

MergeOverLappingInterval(li, n)
