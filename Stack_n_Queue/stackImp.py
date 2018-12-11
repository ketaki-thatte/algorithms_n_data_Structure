class stack(object):
	def init(self):
		self.stack = []
		self.top = -1
	
	def push(self,element):
		self.stack.append(element)
		top = len(self.stack) - 1
		return self.stack
	def pop(self):
		if len(stack) == 0:
			return -1
		else:
			return self.stack.pop()

	def getMin(self):


	def isEmpty(self):
		if len(self.stack) == 0:
			return True
		else:
			return False

	def printStack(self)
			

if __name__ == '__main__':
	s = stack()
	s.push(12)
	s.pust(19)
	s.pust(1)
	s.pust(290)
	s.pust(10)
	s.pust(90)