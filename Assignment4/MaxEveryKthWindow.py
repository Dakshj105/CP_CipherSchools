from collections import deque

li = list(map(int, input().split()))
k = int(input())

q = deque()
maxi = li[0]
q.append(li[0])
for i in range(1, k):
    if li[i] > maxi:
        maxi = li[i]
    elif li[i] >= q[-1]:
        q[-1] = li[i]
        q.append(li[i])
    else:
        q.append(li[i])
print(maxi)
for i in range(k, len(li)):
    ele = q.popleft()
    if ele == maxi:
        maxi = q[0]
    if li[i] > maxi:
        maxi = li[i]
    elif li[i] >= q[-1]:
        q[-1] = li[i]
    q.append(li[i])
    print(maxi)
