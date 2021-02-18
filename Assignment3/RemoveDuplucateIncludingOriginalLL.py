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

    def RemoveDuplicateIncludingOriginal(self):
        cur1 = self.head
        cur = pre = Node()
        cur.next = cur1
        while cur1 and cur1.next:
            if cur1.data == cur1.next.data:
                while(cur1 and cur1.next and cur1.data == cur1.next.data):
                    cur1 = cur1.next
                cur1 = cur1.next
                pre.next = cur1
            else:
                pre = pre.next
                cur1 = cur1.next

        self.head = cur.next

a = LinkedList()
a.add(11)
a.add(11)
a.add(11)
a.add(11)
a.add(75)
a.add(75)
a.add(56)

a.RemoveDuplicateIncludingOriginal()
a.printLL()
