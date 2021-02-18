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

    def Reorder(self):
            cur = self.head
            for _ in range(self.length // 2 - 1):
                cur = cur.next
            if self.length % 2:
                mid = cur.next
            mid.next = self.reverseLL(mid.next)
            head2 = mid.next
            head1 = self.head
            mid.next = None
            for i in range(self.length - 1):
                if i == 0:
                    cur = self.head
                    head1 = head1.next
                elif i % 2 == 0:
                    cur.next = head1
                    head1 = head1.next
                    cur = cur.next
                else:
                    cur.next = head2
                    head2 = head2.next
                    cur = cur.next

            if head1:
                cur.next = head1
                head1 = head1.next
                self.tail = cur

            
    def reverseLL(self, head):
        cur = head
        pre = None
        post = None
        while(cur):
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post

        return pre

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
a.Reorder()
a.printLL()