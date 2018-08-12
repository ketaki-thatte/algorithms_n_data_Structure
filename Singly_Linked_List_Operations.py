class node:
	def __init__(self,val):
		self.next = None
		self.val = val

class SinglyLinkedList:
	def __init__( self ) :
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

	def calculate_length(self):
		count = 0
		current = self.head
		if current == None:
			return 0
		else:
			while current!= None:
				count = count + 1
				current = current.next
			return count 
	def insert_list_at_pos(self,position,element):
		list_length = self.calculate_length()
		counter = 0
		prev = None
		current = self.head
		# If invalid position
		if position > list_length:
			print("Please give valid position")
			# return self.head 

		#If position at the end
		elif position == list_length:
			self.add(element)

		# If position at the satrt
		elif position == 0:
			if current == None:
				self.head = node(element)
				# return self.head
			else:
				next_ele = current
				current = node(element)
				current.next = next_ele
				self.head = current
		else:
		#If Position in between
			while current != None:
				if counter == position-1:
					prev = current
					next_ele = current.next
					current = node(element)
					prev.next = current
					current.next = next_ele
				current = current.next
				counter = counter + 1
		return self.head
	def delete_list_at_pos(self,position):
		counter = 0
		current = self.head
		list_length =self.calculate_length()
		# If position is grerter than list length
		if position > list_length-1:
			print('Element does not exist')
		#If position is at the start
		elif position == 0:
				next_element = current.next
				self.head = next_element
		# If current is in between the List
		else:
			while current != None:
				if counter == position-1:
					current.next = current.next.next
				current = current.next
				counter = counter + 1
		return self.head

	def revert_list(self):
		current = self.head
		prev = None
		while current != None:
			# Store Next Element
			next_element = current.next
			current.next = prev
			prev = current
			current = next_element
		self.head = prev
		return self.head
	def display_list(self):
		current = self.head
		while current != None:
			print(str(current.val) + " -> ",end=" ")
			current = current.next
		print("None")
	

if __name__ == '__main__':
    l = SinglyLinkedList()
    # Add the Nodes to the linked list
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(3)
    l.add(5)
    l.add(6)
    # Display the list
    l.display_list()
    #Insert the element at a given position
    l.insert_list_at_pos(3,4)
    l.insert_list_at_pos(0,0)
    l.display_list()
    # Delete the element at a given position
    l.delete_list_at_pos(3)
    l.delete_list_at_pos(0)
    l.display_list()    
    # Reverse the linked List
    l.revert_list()
    l.display_list()    
