from collections import deque

class Stack:

    def __init__(self):
        self.s = deque()
        self.length = 0

    def push(self, x):
        self.length += 1
        self.s.append(x)

    def pop(self):
        if self.length == 0:
            return "UnderFlow"

        self.length -= 1
        return self.s.pop()
    
    def peek(self):
        if self.length == 0:
            print("Empty Stack")
            return

        return self.s[-1]

    def isEmpty(self):
        return self.length == 0

    def printer(self):
        print()
        for i in range(self.length - 1, -1, -1):
            print(self.s[i])
        print()

def sortStack(s):
    if not s.isEmpty():
        ele = s.pop()
        sortStack(s)
        SortHelper(s, ele)

def SortHelper(s, ele):
    if s.isEmpty() or s.peek() < ele:
        s.push(ele)

    else:
        temp = s.pop()
        SortHelper(s, ele)
        s.push(temp)

s = Stack()
s.push(4)
s.push(3)
s.push(2)
s.push(1)
s.printer()
sortStack(s)
s.printer()
