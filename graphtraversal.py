import Queue

def bfs(graph, start_node):
	queue = Queue.Queue()
	queue.put(start_node)
	while not queue.empty():
		node = queue.get()
		for edge_node in graph.get_adjacency_list(node):
			if not edge_node.discovered:
				queue.put(edge_node)
				edge_node.discovered = True
		print node.value
		node.processed = True

def dfs(grapn, start_node):
	print start_node