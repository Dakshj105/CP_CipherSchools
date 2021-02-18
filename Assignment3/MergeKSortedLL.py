class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.length = 1
            return

        cur = self.head
        new_node = Node(data)
        while(cur.next):
            cur = cur.next

        cur.next = new_node
        self.tail = cur.next
        self.length += 1

    def printLL(self):
        if self.head== None:
            print("Empty Linked List")
            return

        cur = self.head
        while(cur.next):
            print(cur.data, end = "->")
            cur = cur.next
        print(cur.data)

def MergeKSortedLL(li):
    mainhead = LinkedList()
    while(li):
        mini = li[0]
        index = 0
        for i in range(1,len(li)):
            if li[i].data < mini.data:
                mini = li[i]
                index = i
        mainhead.add(mini.data)
        li[index] = li[index].next
        li = removeFinishedLL(li)

    mainhead.printLL()

def removeFinishedLL(li):
    updated_li = []
    for i in li:
        if i:
            updated_li.append(i)
    del li
    return updated_li

a = LinkedList()
a.add(1)
a.add(4)
a.add(7)
a.add(10)

b = LinkedList()
b.add(2)
b.add(5)
b.add(8)
b.add(11)
b.add(14)

c = LinkedList()
c.add(3)
c.add(6)
c.add(9)
c.add(12)
c.add(15)
c.add(18)

li_heads = [a.head, b.head, c.head]
MergeKSortedLL(li_heads)
