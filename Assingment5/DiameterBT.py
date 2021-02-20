from queue import Queue
class Height:
    def __init__(self):
        self.h = 0

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

def diameter(root, height):
    left_h = Height()
    right_h = Height()
    if root is None:
        height.h = 0
        return 0
     
    left_diameter = diameter(root.left, left_h)
    right_diameter = diameter(root.right, right_h)
 
    height.h = max(left_h.h, right_h.h) + 1
    return max(left_h.h + right_h.h + 1, max(left_diameter, right_diameter))

tree = BinaryTree()
print(tree)
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
height = Height()
print(diameter(tree.root, height))