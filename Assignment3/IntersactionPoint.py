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

def IntersectionPoint(head1, head2):
    c_head1 = c_head2 = 0
    cur = head1
    while(cur):
        c_head1 += 1
        cur = cur.next

    cur = head2
    while(cur):
        c_head2 += 1
        cur = cur.next

    if c_head2 >= c_head1:
        diff = c_head2 - c_head1
        for i in range(diff):
            head2 = head2.next
        while(head1 != head2):
            head1 = head1.next
            head2 = head2.next

        return head1.data

    else:
        diff = c_head1 - c_head2
        for i in range(diff):
            head1 = head1.next
        while(head1 != head2):
            head1 = head1.next
            head2 = head2.next

        return head1.data


a = LinkedList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)

b = LinkedList()
b.add(5)
b.add(6)

b.tail.next = a.head.next.next

print(IntersectionPoint(a.head, b.head))