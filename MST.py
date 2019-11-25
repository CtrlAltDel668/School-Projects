
import random

class Vertex_():
  def __init__(self,value):
    self.value = value
    self.nb = {}
    self.traverse = False
      
  def get_val(self):
    return self.value
      
  def set_val(selfvalue):
    self.value = value
      
  def set_nb(self, node, weight):
    if node not in self.nb.keys():
        self.nb[node] = weight
     
          
  def get_nb(self):
    return self.nb
        
   

class Graph():
  def __init__(self):
    self.vertices = []
      
  def set_vertices(self,vertex):
    self.vertices.append(vertex)
      
  def get_vertices(self):
    return self.vertices
      
  def len_vertices(self):
    return len(self.vertices)


class Main():
  def __init__(self):
    self.graph = Graph()
    self._list = []
    for a in range(1,11):
        self._list.append(a)
          
          
  def gen_vertices(self,n):
    for i in range (0,n):
        choice = random.choice(self._list)
        self._list.remove(choice)
        vertex = Vertex_(choice)
        self.graph.set_vertices(vertex)
        
        if self.graph.len_vertices() != 0 :
            range_ = random.randint(1,self.graph.len_vertices())
            randWeight = random.randint(1,10)
            
            for i in range (0, range_):
                choice_vertex = random.choice(self.graph.get_vertices())
                if vertex != choice_vertex:
                    vertex.set_nb(choice_vertex, randWeight)
                    choice_vertex.set_nb(vertex, randWeight)
  def  Graph_print(self):
      
    for i in self.graph.vertices:
        print('(',i.get_val(),')')
        print('Neighbors :')
        for u in i.get_nb().keys():
            print(u.get_val(),'Weight: ', i.get_nb()[u])
        print()
    print()
    print('.========================.')
    print('||The Graph is Complete!||')
    print('.========================.')        

  def kruskal_(self):
    result = []
    i = 0
    e = 0
    self.graph = sorted(self.graph,key =lambda item: item[2])

    parent = [], rank = []

    for node in range (self.graph.vertices) :
      parent.append(node)
      rank.append(0)

    while  e < self.graph.vertices - 1:
      u,v,w = self.graph[i]

# class Kruskal :
#   def __init__(self,nodelist,n):
#     self.parent = []
#     for i in range(0,len(nodelist)):
#       self.parent.append(k)
#     self.result = self.krux(nodelist,n)
#   def get_result(self):
#     result self.result
#   def krux(self,nodelist,n):
#     current_node = nodelist[0]
#     edgelist = []
#     finallist = []
#     while len(finallist) < n-1 :
#       print(current_node.get_val())
#       nb = current_node.get_nb()
#       for i in nodelist:
#         for u in nodelist.get_nb().keys():
#           edgelist.append
        
  # def Mst_Prims(self):

  #   for i in self.graph.vertices:
  #     for u in i.get_nb().keys():
  #       set(i.get_nb





          

num_nodes = 10
j = Main()
j.gen_vertices(num_nodes)
j.Graph_print()
   
  
  
   

