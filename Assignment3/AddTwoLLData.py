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

    def AddData(self, head1, head2):
        carry = 0
        head1 = self.reverseLL(head1)
        head2 = self.reverseLL(head2)
        temp = [head1, head2]
        #self.printOtherLl(head1)
        #self.printOtherLL(head2)
        while(head1 and head2):
            if (head1.data + head2.data + carry)> 9:
                self.add((head1.data + head2.data + carry) % 10)
                carry = (head1.data + head2.data + carry) // 10
            else:
                self.add(head1.data + head2.data + carry)
                carry = 0
            head1 = head1.next
            head2 = head2.next

        while(head1):
            if (head1.data + carry)> 9:
                self.add((head1.data + carry) % 10)
                carry = (head1.data + carry) // 10
            else:
                self.add(head1.data + carry)
                carry = 0
            head1 = head1.next

        while(head2):
            if (head2.data + carry)> 9:
                self.add((head2.data + carry) % 10)
                carry = (head2.data + carry) // 10
            else:
                self.add(head2.data + carry)
                carry = 0
            head2 = head2.next

        if carry:
            self.add(carry)

        self.head = self.reverseLL(self.head)
        temp[0] = self.reverseLL(temp[0])
        temp[1] = self.reverseLL(temp[1])
            

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

'''   def printOtherLL(self, head):
        if head== None:
            print("Empty Linked List")
            return

        cur = head
        while(cur.next):
            print(cur.data, end = "->")
            cur = cur.next
        print(cur.data)
'''


a = LinkedList()
a.add(5)
a.add(6)
a.add(3)

b = LinkedList()
b.add(8)
b.add(4)
b.add(2)

c = LinkedList()
c.AddData(a.head, b.head)
c.printLL()