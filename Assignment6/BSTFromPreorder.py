class Node():
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def getPreIndex():
    return constructTreeUtil.preIndex

def incrementPreIndex():
    constructTreeUtil.preIndex += 1
 
def constructTreeUtil(preorder, low, high, n):
    if(getPreIndex() >= n or low > high):
        return None

    root = Node(preorder[getPreIndex()])
    incrementPreIndex()

    if low == high:
        return root

    for i in range(low, high+1):
        if (preorder[i] > root.data):
            break

    root.left = constructTreeUtil(preorder, getPreIndex(),  i-1, n)
    root.right = constructTreeUtil(preorder, i, high, n)
 
    return root

def constructTree(preorder):
    constructTreeUtil.preIndex = 0
    return constructTreeUtil(preorder, 0, len(preorder)-1, len(preorder))
 
 
def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data, end = " ")
    printInorder(root.right)

preorder = list(map(int, input().split()))
bst = constructTree(preorder)
printInorder(bst)