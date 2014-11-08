class Graph:
	def __init__(self, adjacency_list={}):
		self.adjacency_list = adjacency_list
	
	def get_adjacency_list(self, node):
		return self.adjacency_list[node]
