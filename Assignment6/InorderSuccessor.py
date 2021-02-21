class Node:
	def __init__(self, key):
		self.data = key 
		self.left = None
		self.right = None

def inOrderSuccessor(root, n):	
	if n.right is not None:
		return minValue(n.right)
	succ=Node(None)

	while( root):
		if(root.data<n.data):
			root=root.right
		elif(root.data>n.data):
			succ=root
			root=root.left
		else:
			break
	return succ

def minValue(node):
	cur = node
	while(cur is not None):
		if cur.left is None:
			break
		cur = cur.left

	return cur

bst = Node(20) 
bst.left = Node(8) 
bst.right = Node(22) 
bst.left.left = Node(4) 
bst.left.right = Node(12) 
bst.left.right.left = Node(10) 
bst.left.right.right = Node(14) 
cur = Node(int(input()))

succ = inOrderSuccessor(bst, cur)
if succ:
	print(cur.data, "-->" ,succ.data)
else:
	print("Doesn't exist")