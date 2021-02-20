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

def CheckMirror(a, b): 
    if a == b == None: 
        return True

    if a is None or b is None: 
        return False

    return (a.data == b.data and CheckMirror(a.left, b.right) and CheckMirror(a.right , b.left))

tree1 = BinaryTree()
print(tree1)
tree1.root = Node(1)
tree1.root.left = Node(3)
tree1.root.right = Node(2)
tree1.root.left.left = Node(4)
tree1.root.left.right = Node(5)
tree1.root.right.right = Node(6)

tree2 = BinaryTree()
print(tree2)
tree2.root = Node(1)
tree2.root.left = Node(2)
tree2.root.right = Node(3)
tree2.root.left.left = Node(6)
tree2.root.right.left = Node(5)
tree2.root.right.right = Node(4)

print(CheckMirror(tree1.root, tree2.root))