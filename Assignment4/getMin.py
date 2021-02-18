from collections import deque

class Stack:

    def __init__(self):
        self.s = deque()
        self.length = 0
        self.mini = None

    def push(self, x):
        if self.length == 0:
            self.s.append(x)
            self.mini = x
        elif x < self.mini:
            self.s.append(2 * x - self.mini)
            self.mini = x
        else:
            self.s.append(x)
        self.length += 1


    def pop(self):
        if self.length == 0:
            return " UnderFlow"

        if self.peek() > self.mini:
            self.length -= 1
            return self.s.pop()

        else:
            mini = self.mini
            self.mini = 2 * self.mini - self.peek()
            self.s.pop()
            self.length -= 1
            return mini


    def peek(self):
        if self.length:
            return self.s[-1]

        return "Empty Stack"

    def size(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def printer(self):
        print()
        for i in range(self.length - 1, -1, -1):
            print(f"| {self.s[i]} |")
            print("-----")

    def getMin(self):
        return self.mini


s = Stack()
s.push(4)
s.push(3)
s.push(4)
s.push(1)
s.printer()
print(s.getMin())
s.pop()
print(s.getMin())
