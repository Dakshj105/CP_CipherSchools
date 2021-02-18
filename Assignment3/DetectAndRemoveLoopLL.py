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

    def AddLoop(self):
        self.tail.next = self.head
    
    def DetectLoopAndRemove(self):
        slow = self.head
        fast = self.head
        i = 0
        while(i != self.length):
            fast = fast.next
            if slow and fast:
                slow = slow.next
                fast = fast.next
            else:
                break
            if slow == fast:
                break
            i += 1
               
        if slow == fast:
            print("Loop Exists")
            c = self.CountNodesInLoop(slow)
            cur = self.head
            if slow == cur:
                for _ in range(c - 1):
                    cur = cur.next
                cur.next = None
                print("Loop Deleted")
                return
            while(slow != cur):
                pre = slow
                slow = slow.next
                cur = cur.next
            pre.next = None
            print("Loop Deleted")
            return


        else:
            print("No Loop exists")

    def CountNodesInLoop(self, slow):
        cur = slow
        c = 0
        while(cur != slow):
            c += 1
            cur = cur.next

        return c

a = LinkedList()
a.add(5)
a.add(6)
a.add(3)
a.AddLoop()
a.DetectLoopAndRemove()