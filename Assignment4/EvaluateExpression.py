from queue import LifoQueue
import string
from queue import LifoQueue as Stack

def infix_to_prefix(s):
	stack=Stack()
	s=list(s[::-1])
	s1=[]
	precedence = {'-':1,'+':1,'*':2,'/':2,'^':3,')':0}
	for i in s:
		if ((i in string.ascii_lowercase) or (i in '0123456789') or (i in string.ascii_uppercase)):
			s1.append(i)
		else:
			if stack.empty() or i==')':
				stack.put(i)
				
			else:
				if i=='(':
					while(stack.queue[-1]!=')'):
						s1.append(stack.get())
				
				elif i==stack.queue[-1]=='^':
					s1.append('^')
				
				else:
					while(precedence[i]<precedence[stack.queue[-1]]):
						s1.append(stack.get())
						if stack.empty():
							break
					stack.put(i)


	while(stack.qsize()>0):
		i=stack.get()
		s1.append(i)

	s2=''
	for i in s1:
		if i!=')':
			s2+=i
	print("".join(s2[::-1]))

infix_to_prefix('(A-B/C)*(A/K-L)')







