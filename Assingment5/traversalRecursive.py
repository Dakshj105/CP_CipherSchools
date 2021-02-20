from queue import Queue
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

    def preorder(self, cur):
        if cur == None:
            return

        print(cur.data, end = " ")
        self.preorder(cur.left)
        self.preorder(cur.right)

    def inorder(self, cur):
        if cur == None:
            return

        self.inorder(cur.left)     
        print(cur.data, end = " ")
        self.inorder(cur.right)

    def postorder(self, cur):
        if cur == None:
            return

        self.postorder(cur.left)
        self.postorder(cur.right)
        print(cur.data, end = " ")

tree = BinaryTree()
print(tree)
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)
print(tree)
tree.preorder(tree.root)
print()
tree.inorder(tree.root)
print()
tree.postorder(tree.root)
