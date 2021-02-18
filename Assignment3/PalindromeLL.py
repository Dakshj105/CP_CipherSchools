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

    def checkPalindrome(self):
            cur = self.head
            if cur == None or cur.next == None:
                return True
            if self.length == 2:
                return cur.data == cur.next.data
            pre = cur
            for i in range(self.length // 2):
                pre = cur
                cur = cur.next

            if self.length % 2:
                cur = cur.next
                pre = pre.next

            head_2ndpart = self.reverseLL(cur)
            pre.next = head_2ndpart
            cur = self.head
            temp = head_2ndpart
            status = True
            
            for _ in range(self.length // 2 - 1):
                if cur.data != head_2ndpart.data:
                    status = False
                    break
                cur = cur.next
                head_2ndpart = head_2ndpart.next
            
            temp = self.reverseLL(temp)
            pre.next = temp

            return status
            
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
a.add(3)
a.add(5)
a.add(6)
a.add(5)
a.add(3)
print(a.checkPalindrome())
a.printLL()
