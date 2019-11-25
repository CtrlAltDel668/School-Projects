class Item():
	def __init__(self,value):
		self.value = value
		self.nxt = None
		self.prev = None

	def get_nxt(self):
		return self.nxt
	def get_prev(self):
		return self.prev
	def get_val(self):
		return self.value
	def set_nxt(self,nxt_):
		self.nxt = nxt_
	def set_prev(self,prev_):
		self.prev = prev_

class LinkList():
	
	def __init__(self):
		self.items = 0
		self.tail = 0
		self.head = 0

	def push(self,value):
		node = Item(value)

		if self.items == 0 :
			self.head = node
			self.tail = node
			
		else :

			temp_val = node
			temp_tail = self.tail
			temp_val.set_nxt(temp_tail)
			temp_tail.set_prev(temp_val)
			self.tail = temp_val
			
		self.items += 1

	def pop_head(self):
		temp = self.head.get_val()
		del temp
		self.items -= 1

	def pop_tail(self):
		temp = self.tail.get_val()
		del temp
		self.items -= 1 

	def peek(self):
		return self.tail.get_val()

	def search(self,node,value):
		if node.get_val() == value :
			return node
		elif node.get_prev() == None :
			return None
		else :
			temp = node.get_prev()
			return self.search(temp,value)

	def remove(self,value) :

		elem = self.search(self.head,value)
		if elem == None :
			return print('Their are no such element in the list')
		else :
			temp_prev = elem.get_prev()
			temp_nxt = elem.get_nxt()
			temp_prev.set_nxt(temp_nxt)
			temp_nxt.set_prev(temp_prev)
			self.items -= 1
			del elem

link = LinkList()
link.push(2)
link.push(32)
link.push(24)
link.push(1)
link.push(21)
link.push(3)
link.pop_head()
link.pop_tail()
link.pop_tail()
link.remove(24)
link.peek()


