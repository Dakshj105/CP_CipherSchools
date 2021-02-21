class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def lca(root, n1, n2): 
	while root: 
		if root.data > n1 and root.data > n2: 
			root = root.left 		
		elif root.data < n1 and root.data < n2: 
			root = root.right 

		else: 
			break

	return root.data

root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 

n1 = 10 ; n2 = 14
print(f"LCA of {n1} and {n2} is {lca(root, n1, n2)}")

n1 = 14 ; n2 = 8
print(f"LCA of {n1} and {n2} is {lca(root, n1, n2)}")

n1 = 10 ; n2 = 22
print(f"LCA of {n1} and {n2} is {lca(root, n1, n2)}")