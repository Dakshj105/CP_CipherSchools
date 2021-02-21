class Node: 
    def __init__(self, data = None): 
        self.data = data
        self.left = None
        self.right = None

def sortedArrayToBST(li): 
    if not li: 
        return None
  
    mid = (len(li)) // 2 
    root = Node(li[mid]) 
    root.left = sortedArrayToBST(li[:mid]) 
    root.right = sortedArrayToBST(li[mid+1:]) 

    return root 

def preorder(node): 
    if not node: 
        return
      
    print(node.data, end = " ")
    preorder(node.left) 
    preorder(node.right)  
  
li = [1, 22, 33, 44, 55, 66, 77, 88, 99] 
root = sortedArrayToBST(li) 
preorder(root)