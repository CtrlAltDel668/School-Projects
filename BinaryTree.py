class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].key

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class BinaryTree:
	def __init__(self,rootObj):
		self.key=rootObj
		self.rightChild =None
		self.leftChild=None

	def insertLeft(self,newNode):
		if self.leftChild == None:
			self.leftChild=BinaryTree(newNode)

		else:
			t=BinaryTree(newNode)
			t.leftChild=self.leftChild
			self.leftChild=t

	def insertRight(self,newNode):
		if self.rightChild ==None:
			self.rightChild=BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild=self.rightChild
			self.rightChild=t

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self,obj):
		self.key=obj

	def getRootVal(self):
		return self.key



#PreOrder travesal for tree
	def preOrder(self):
		print(self.key)
		if self.leftChild:
			self.leftChild.preOrder()
		if self.rightChild:
			self.rightChild.preOrder()


#External method for the preOrder traversal

def preOrderTraversal(tree):
	
	if tree:
		print(tree.getRootVal())
		preOrderTraversal(tree.getLeftChild())
		preOrderTraversal(tree.getRightChild())


# methoid for the inOrder travesal

def inOrderTraversal(tree):
	if tree:
		inOrderTraversal(tree.getLeftChild())
		print(tree.getRootVal())
		inOrderTraversal(tree.getRightChild())

# method for the postOrderTraversal
def postOrderTraversal(tree):
	if tree:
		postOrderTraversal(tree.getLeftChild())
		postOrderTraversal(tree.getRightChild())
		print(tree.getRootVal())
# method for the levelorder traversal
def levelOrderTraversal(tree):
	if tree is None :
		return
	queue = Queue()
	queue.enqueue(tree)
	trav_ = ""
	while len(queue) > 0 :
		trav_ += str(queue.peek()) + '-'
		node = queue.dequeue()
		if node.leftChild:
			queue.enqueue(node.leftChild)
		if node.rightChild:
			queue.enqueue(node.rightChild)

	return trav_

r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('d')
r.insertLeft('b')
r.insertLeft('b')
r.insertLeft('b')
r.insertRight('d')
r.insertRight('d')
r.insertRight('d')
print("The answer to the preOrderTraversal is below")
preOrderTraversal(r)

print("The answer to the inOrderTraversal is below")
inOrderTraversal(r)

print("The answer to the postOrderTraversal is below")
postOrderTraversal(r)

print("The answer to the levelOrderTraversal is below")
print(levelOrderTraversal(r))