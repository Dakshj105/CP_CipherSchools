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

def buildTree(inorder, preorder, start, end):
     
    if (start > end):
        return

    node = Node(preorder[buildTree.c])
    buildTree.c += 1

    if start == end :
        return node

    index = search(inorder, start, end, node.data)
    node.left = buildTree(inorder, preorder, start, index - 1)
    node.right = buildTree(inorder, preorder, index + 1, end)
 
    return node
 
def search(li, start, end, value):
    for i in range(start, end + 1):
        if li[i] == value:
            return i

preorder = [1, 2, 4, 5, 3, 6]
inorder = [4, 2, 5, 1, 3, 6]
buildTree.c = 0
tree = BinaryTree()
tree.root = buildTree(inorder, preorder, 0, len(inorder) - 1)
print(tree)