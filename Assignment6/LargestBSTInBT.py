INT_MIN = -2147483648
INT_MAX = 2147483647
 
class Node:  
      def __init__(self, data = None):  
        self.data = data  
        self.left = None
        self.right = None

def LargestBSTInBT(root):  
    if (root == None): 
        return 0, INT_MIN, INT_MAX, 0, True
    if (root.left == None and root.right == None) : 
        return 1, root.data, root.data, 1, True
  
    l = LargestBSTInBT(root.left)  
    r = LargestBSTInBT(root.right)  
  
    li = [0, 0, 0, 0, 0]  
    li[0] = (1 + l[0] + r[0])  

    if (l[4] and r[4] and (l[1] <  root.data) and (r[2] > root.data)) :      
        li[2] = min(l[2], min(r[2], root.data))  
        li[1] = max(r[1], max(l[1], root.data))    
        li[3] = li[0]  
        li[4] = True 
        return li

    li[3] = max(l[3], r[3])  
    li[4] = False
  
    return li 

root = Node(60)  
root.left = Node(65)  
root.right = Node(70)  
root.left.left = Node(50) 
root.left.right = Node(75)
root.left.right.left = Node(71)
root.left.right.right = Node(80)
print(LargestBSTInBT(root)[3])