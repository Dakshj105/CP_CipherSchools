class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

def printPaths(root): 
    path = [] 
    printPathsRec(root, path, 0) 

def printPathsRec(root, path, cur_len): 
    if root is None: 
        return
 
    if(len(path) > cur_len):  
        path[cur_len] = root.data 
    else: 
        path.append(root.data)  
    cur_len = cur_len + 1
  
    if root.left is None and root.right is None: 
        printArray(path, cur_len) 
    else: 
        printPathsRec(root.left, path, cur_len) 
        printPathsRec(root.right, path, cur_len) 

def printArray(ints, len): 
    for i in ints[0 : len]: 
        print(i," ",end="") 
    print() 

tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.right = Node(6)
printPaths(tree.root)
