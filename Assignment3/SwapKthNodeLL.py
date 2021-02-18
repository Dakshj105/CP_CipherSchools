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

    def swap(self, k):
        if k > self.length:
            print("Wrong Input")
            return
        if k == self.length + 1 - k:
            return
        if self.length == 1:
            return
        if self.length == 2:
            self.tail.next = self.head
            self.head = self.tail
            self.tail = self.head.next
            self.tail = None
        k = k - 1
        node1 = node2 = None
        node1_pre = node2_pre = None
        node1_post = node2_post = None
        cur = self.head
        for i in range(self.length - 1):
            if i == (k - 1):
                node1_pre = cur
            elif i == k:
                node1 = cur

            elif i == (k + 1):
                node1_post = cur

            elif (self.length - 1 - 1 - k) == i:
                node2_pre = cur

            elif (self.length - 1 - k) == i:
                node2 = cur

            elif (self.length - k) == i:
                node2_post = cur
            
            cur = cur.next

        if node1_pre == node2_post == None:
            self.head = node2
            node2.next = node1_post
            node2_pre.next = node1
            node1.next = None
            self.tail = node1
        
        else:
            node1.next = node2_post
            node1_pre.next = node2
            node2.next = node1_post
            node2_pre.next = node1

    def printLL(self):
        if self.head== None:
            print("Empty Linked List")
            return

        cur = self.head
        while(cur.next):
            print(cur.data, end = "->")
            cur = cur.next
        print(cur.data)

a = LinkedList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.add(6)
a.add(7)
a.add(8)
a.add(9)
k = int(input())
a.printLL()
a.swap(k)
a.printLL()