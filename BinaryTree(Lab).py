
class Node():
  def __init__(self,value):
      self.value = value
      self.left = None
      self.right = None
      
  def get_value(self):
      return self.value
  
  def set_value(self, value):
      self.value = value
      
      
  def set_right(self,right):
      self.right = right
      
  def set_left(self,left):
      self.left = left
      
  def get_left(self):
      return self.left
  
  def get_right(self):
      return self.right


class BinaryTree():
  def __init__(self,root):
      self.root = Node(root)
      
  def insert(self,value):
      node1 = Node(value)
      
      self.h_insert(node1,self.root)

  def h_insert(self,node1, _node):
      if node1.get_value() < _node.get_value():
          if _node.get_left() is None:
              _node.set_left(node1)
          else :
              return self.h_insert(node1,_node.left)
      elif node1.get_value() > _node.get_value():
          if _node.get_right() is None:
              _node.set_right(node1)
          else :
              return self.h_insert(node1,_node.right)

  def del_node(self,value):
      self.Hdel_node(value,self.root)
  def Hdel_node(self,value, _node):
      
      if value < _node.get_value():
          if _node.get_left() is not None and _node.get_left().get_value() == value:
              _node.set_left(None)
              return
          else :
              return self.Hdel_node(value,_node.left)
      elif value > _node.get_value():
      
          if _node.get_right() is not None and _node.get_right().get_value() == value :
         
              _node.set_right(None)
              return
          else :
              return self.Hdel_node(value,_node.right)

  def print_Tree(self):
      if self.root != None :
        self._pNode(self.root)

  def _pNode(self, node):
    if node != None:
      self._pNode(node.left)
      print (str(node.value))
      self._pNode(node.right)
  def preTrav(self):
    print(self.root.get_value(),end = ',')
    self.pre_(self.root)
  def pre_(self,parent):
    if parent.get_left() is not None:
      print(parent.get_left().get_value(),end = ' ,')
      self.pre_(parent.get_left())
    if parent.get_right() is not None:
      print(parent.get_right().get_value(), end = ' ,')
      return self.pre_(parent.get_right())
  def inTrav(self):
    self.in_(self.root)

  def in_(self,parent):
    if parent.get_left() is not None :
      self.in_(parent.get_left())
    print(parent.get_value(), end = ' ,')
    if parent.get_right() is not None :
      self.in_(parent.get_right())
  def postTrav(self):
    self.post_(self.root)
  def post_(self,parent):
    if parent.get_left() is not None:
      self.pre_(parent.get_left())
      print(parent.get_left().get_value(),end = ' ,')
    if parent.get_right() is not None:
      self.pre_(parent.get_right())
      print(parent.get_right().get_value(), end = ' ,')
    print(parent.get_value(), end = ' ')
    return
c = BinaryTree(10)
c.insert(5)
c.insert(1)
c.insert(8)
c.insert(20)
c.insert(15)
c.insert(25)
#c.print_Tree()
c.preTrav()
print()
c.inTrav()
print()
c.postTrav()
#print('Pre - order Traversal')
#preOrder(c)
  


