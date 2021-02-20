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


    def height(self, node):
        if node is None:
            return -1 
        else :
            left_h = self.height(node.left)
            right_h = self.height(node.right)
            if (left_h > right_h):
                return left_h+1
            else:
                return right_h+1

tree = BinaryTree()
print(tree)
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)
print(tree.height(tree.root))
        