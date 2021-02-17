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

    def reverseLLIter(self):
        pre = None
        next = None
        cur = self.head
        while(cur):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        self.head = pre

    def reverseLLRecur(self):
        self.head = self.recursion_LL_reverse(self.head)

    def recursion_LL_reverse(self, cur_head):
        if cur_head == None or cur_head.next == None:
            return cur_head

        new_head = self.recursion_LL_reverse(cur_head.next)
        cur_head.next.next = cur_head
        cur_head.next = None
        return new_head

        

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
a.printLL()
a.add(3)
a.add(5)
a.add(6)
a.printLL()
a.reverseLLIter()        # Reverse linked list using iteration
a.printLL()
a.reverseLLRecur()       # Reverse linked list using recursion
a.printLL()
