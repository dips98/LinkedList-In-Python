class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Linked_list:

	def __init__(self, head = None, length = 0):
		self.head = head
		self.length = length

	def append(self, value):
		if not self.head:
			newnode = Node(value)
			self.head = newnode
			self.length = 1
		else:
			curr = self.head
			while curr.next:
				curr = curr.next
			curr.next = Node(value)
			self.length += 1

	def display(self):
		if not self.head:
			print("Empty")
		else:
			curr = self.head
			print(curr.value)
			while curr.next !=None:
				curr = curr.next
				print(curr.value)

	def get_position(self, pos):
		if pos >= 0:
			count = 0
			curr = self.head
			while curr.next:
				if pos == count:
					print(f'The value is {curr.value}')
				curr = curr.next
				count += 1
			if pos == count:
				print(f'The value is {curr.value}')
			elif pos > count:
				print("Not valid Position")
		else:
			print("Not valid Position")
		
	def insert(self, val, pos):
		curr = self.head
		count = 0
		if pos > 0 and pos < self.length:
			pos = pos - 1
			while curr.next:
				if pos == count:
					newnode = Node(val)
					newnode.next = curr.next
					curr.next = newnode
					self.length += 1
				curr = curr.next
				count += 1
		elif pos == 0:
			newnode = Node(val)
			newnode.next = self.head
			self.head = newnode
			self.length += 1
		else:
			print(f"Enter valid Position Where length is {self.length}")

	def dele(self, value):
		if self.head.value == value:
			self.head =self.head.next
			self.length -+ 1
		else:
			prev = self.head
			current =self.head
			while current.next:
				current = current.next
				if current.value == value:
					prev.next =current.next
					self.length -+1
				prev = current


ll = Linked_list()
ll.append(8)
ll.append(9)
ll.append(10)
ll.append(11)
ll.append(12)
ll.display()
print("After Inserting at specific value and specific postion")
ll.insert(99, 0)
ll.insert(999, 2)
ll.display()
print("After Deletion")
ll.dele(99)
ll.dele(999)
ll.display()
print("Getting postion")
ll.get_position(5)

