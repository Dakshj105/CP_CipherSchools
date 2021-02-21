class Node: 
	def __init__(self,data): 
		self.data = data 
		self.left = None
		self.right = None

def LevelOrder(root , data): 
	if(root == None): 
		root = Node(data) 
		return root 
	
	if(data <= root.data): 
		root.left = LevelOrder(root.left, data) 
	else: 
		root.right = LevelOrder(root.right, data) 
	return root	 

def constructBst(li): 
	if not len(li): 
		return
	root = None

	for i in range(len(li)): 
		root = LevelOrder(root , li[i]) 
	
	return root 

def inorderTraversal(root): 
	if (root == None): 
		return
	
	inorderTraversal(root.left) 
	print(root.data,end = " ") 
	inorderTraversal(root.right) 

li = [7, 4, 12, 3, 6, 8, 1, 5, 10] 
root = constructBst(li) 	
inorderTraversal(root) 