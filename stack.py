
class Stack():
        
  def __init__(self):
    self.num_items = 0
            
  def push(self, item):

    if (self.num_items ==0):
      self.item = item
    else:
      self.new_item = item
      self.prev_item = self.item          
      self.new_item.set_next(self.item)
      self.prev_item.set_prev(item)
      self.item = self.new_item
      self.num_items += 1

  def pop(self):
            
    if (self.num_items != 0):
                
      self.temp_item = self.item.get_next()
      self.temp_item.set_prev(None)
      self.item = self.temp_item
                
      self.num_items -= 1
            
  def peek(self):
    return self.item.get_value()

class Item():
        
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
            
  def get_next(self):
    return self.next
        
    def get_prev(self):
      return self.prev
        
    def set_next(self,next_):
      self.next = next_
        
    def set_prev(self,prev_):
      self.prev =prev_
            
    def get_value(self):
      return self.value

item1 = Item(2)
    
item2 = Item(99)

stack = Stack()

stack.push(item1)
   
stack.peek()
stack.push(item2)
  
stack.peek()
 
stack.num_items
  
stack.peek()
  
stack.pop()
 
stack.peek()
