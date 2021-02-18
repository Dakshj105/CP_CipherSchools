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

    def Merge(self, head1, head2):
        c = 0
        while(head1 and head2):
            if head1.data <= head2.data:
                c += 1
                if c == 1:
                    self.head = head1
                    cur = self.head
                else:
                    cur.next = head1
                    cur = cur.next
                head1 = head1.next
            else:
                c += 1
                if c == 1:
                    self.head = head2
                    cur = self.head
                else:
                    cur.next = head2
                    cur = cur.next
                head2 = head2.next

        while(head1):
            cur.next = head1
            cur = cur.next
            head1 = head1.next
        while(head2):
            cur.next = head2
            cur = cur.next
            head2 = head2.next



a = LinkedList()
a.add(1)
a.add(2)
a.add(4)

b = LinkedList()
b.add(3)
b.add(5)

c = LinkedList()
c.Merge(a.head, b.head)
c.printLL()