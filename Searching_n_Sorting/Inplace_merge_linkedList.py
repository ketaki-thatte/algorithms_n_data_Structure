class node(object):
	def  __init__(self,data):
		self.data = data
		self.next = None
class LinkedList(object):
	def  __init__(self):
		self.head = None	

	def add(self,element):
		current = self.head
		node_ele = node(element)
		if current == None:
			current = node_ele
			self.head = current
			# return current
		else:
			head_ele = current
			while current.next != None:
				current = current.next
			current.next = node_ele
			# return head_ele
		return self.head

	def displayList(self):
		current = self.head
		while current != None:
			print(str(current.data) + " -> ",end=" ")
			current = current.next
		print("None")

def mergeUtil(head1,head2):
	node1 = head1
	node2 = head2
	nextNode1 = node1.next
	nextNode2 = node2.next
	while node1 and node2:
		if node2.data > node1.data and node2.data < nextNode1.data:
			nextNode2 = node2.next
			node1.next = node2
			node2.next = nextNode1		
		else:
			if nextNode1.next:
				nextNode1 = nextNode1.next
				node1 = node1.next
			else:
				nextNode1.next = node2
				return node1
	return node1

def mergeTwoSortedList(head1,head2):
	if head1.head.data > head2.head.data:
		return mergeUtil(head2.head,head1.head)
	else:
		return mergeUtil(head1.head,head2.head)


if __name__ == '__main__':
	l1 = LinkedList()
	l1.add(10)
	l1.add(18)
	l1.add(24)
	l1.add(40)
	l1.displayList()
	l2 = LinkedList()
	l2.add(8)
	l2.add(16)
	l2.add(18)
	l2.add(22)
	l2.add(36)
	l2.add(40)
	l2.displayList()
	mergeTwoSortedList(l1,l2)
	l2.displayList()