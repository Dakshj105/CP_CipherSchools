from queue import Queue
class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def sumCalc(self):
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
        
        return sum(li)

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)
print(tree.sumCalc())