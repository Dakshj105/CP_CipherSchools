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

def buildTree (inorder, start, end): 
    if start > end: 
        return None
 
    i = maxFindHelper(inorder, start, end)   
    root = Node(inorder[i])  
    if start == end:  
        return root  
 
    root.left = buildTree (inorder, start, i - 1)  
    root.right = buildTree (inorder, i + 1, end)  
  
    return root 
  
def maxFindHelper(li, start, end): 
    i, maxi = 0, li[start] 
    index = start 
    for i in range(start + 1, end + 1): 
        if li[i] > maxi: 
            maxi = li[i]  
            index = i 
    return index 

tree = BinaryTree()
inorder = [4, 2, 5, 1, 3, 6]
tree.root = buildTree(inorder, 0, len(inorder) - 1)
print(tree)