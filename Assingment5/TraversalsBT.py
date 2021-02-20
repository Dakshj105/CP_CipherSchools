from queue import Queue
from collections import deque
from queue import LifoQueue as Stack
class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root == None:
            return "empty binary tree"

        li = self.Levelorder()
        li = list(map(str, li))
        return " ".join(li)
        
    def Levelorder(self):
        q = Queue()
        li = []
        q.put(self.root)
        while(q.empty() == False):
            cur = q.get()
            li.append(cur.data)
            if cur.left:
                q.put(cur.left)
            if cur.right:
                q.put(cur.right)
        
        return li

    def preorder(self):
        d = deque()
        li = []
        d.append(self.root)
        while(d):
            cur = d.popleft()
            if cur:
                li.append(cur.data)
            if cur.right:
                d.appendleft(cur.right)
            if cur.left:
                d.appendleft(cur.left)

        return li

    def inorder(self):
        d = deque()
        li = []
        cur = self.root
        while(True):
            while(cur):
                d.appendleft(cur)
                cur = cur.left

            if d:
                ele = d.popleft()
                li.append(ele.data)
                cur = ele.right

            else:
                break

        return li

    def postorder(self):
        li = []
        st = Stack()
        cur = self.root
        st.put(cur)
        while(st.empty() == False):
            while(cur):
                if cur.right:
                    st.put(cur.right)
                st.put(cur)
                cur = cur.left

            cur = st.get()
            if st.empty():
                li.append(cur.data)
                break
            if cur.right and cur.right == st.queue[-1]:
                ele = st.get()
                st.put(cur)
                cur = ele
            else:
                li.append(cur.data)
                cur = None
        li.pop()
        return li





tree = BinaryTree()
print(tree)
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)
print(tree)
print(tree.preorder())
print(tree.inorder())
print(tree.postorder())

        
        

