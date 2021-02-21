class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def PrintKeysInGivenRangeBST(root, k1, k2):
    if k1 > k2:
        k1, k2 = k2, k1
             
    if not root:
        return

    if k1 < root.data :
        PrintKeysInGivenRangeBST(root.left, k1, k2)
 
    if k1 <= root.data <= k2:
        print(root.data, end = " ")
 
    if k2 > root.data:
        PrintKeysInGivenRangeBST(root.right, k1, k2)
 
root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14)
PrintKeysInGivenRangeBST(root, int(input()), int(input()))