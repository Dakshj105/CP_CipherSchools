class BinarySearchTree:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def add_BinarySearchTree(self, value):
        if self.data == value:
            return

        elif self.data > value:
            if self.left:
                self.left.add_BinarySearchTree(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.add_BinarySearchTree(value)
            else:
                self.right = BinarySearchTree(value)
    
    def inorder(self, li):
        li = []
        if self.left:
            li += self.left.inorder(li)
        li.append(self.data)
        if self.right:
            li += self.right.inorder(li)

        return li

def buildTree(li):
    root = BinarySearchTree(li[0])
    for i in range(1, len(li)):
        root.add_BinarySearchTree(li[i])

    return root
    
li = [9,8,7,6,5,4,3,2,1]
root = buildTree(li)
print(root.inorder(li))