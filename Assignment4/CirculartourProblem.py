from queue import Queue

def CircularTour(li, n):
    q = Queue(maxsize = n+1)
    carry = 0
    q.put(li[0])
    for i in li:
        if (i[0] - i[1]) >= 0 or (i[0] - i[1] + carry) >= 0:
            q.put(i)
            carry += i[0] - i[1]

        else:
            if q.empty() == False:
                q.get()

            carry += i[0] - i[1]

    if q.empty() == False and carry >= 0:
        print(li.index(q.get()))

    else:
        print("Not possible")

n = int(input())
li =[]
for i in range(n):
    li.append(list(map(int, input().split())))

CircularTour(li, n)
        



