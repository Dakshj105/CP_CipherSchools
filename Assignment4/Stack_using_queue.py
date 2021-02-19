from queue import Queue

class Stack:
	def __init__(self,x=0):
		self.x=x
		self.a1=Queue(maxsize=self.x)
		self.a2=Queue(maxsize=self.x)

		self.cur_size=0

	def push(self,x):
		self.cur_size+=1

		self.a2.put(x)

		while(not self.a1.empty()):
			self.a2.put(self.a1.get())

		self.a1,self.a2 = self.a2,self.a1

	def pop(self):
		if self.a1.empty():
			return "UnderFlow"
		self.cur_size-=1
		return self.a1.get()
		

	def size(self):
		return self.cur_size

	def top(self):
		return -1 if self.a1.empty() else self.a1.queue[0]

	def empty(self):
		return True if self.cur_size==0 else False

'''
a=Stack(1)
a.push(4)
a.push(5)
print(a.top())
print(a.pop())
print(a.pop()) 
print(a.empty())
'''


 