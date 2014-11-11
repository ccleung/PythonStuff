import Queue

def bfs(graph, start_node):
	queue = Queue.Queue()
	queue.put(start_node)
	start_node.discovered = True
	while not queue.empty():
		node = queue.get()
		for edge_node in graph.get_adjacency_list(node):
			if not edge_node.discovered:
				queue.put(edge_node)
				edge_node.discovered = True
		print node.value
		node.processed = True

def dfs(graph, node):
	node.discovered = True
	for edge_node in graph.get_adjacency_list(node):
		if not edge_node.discovered:
			dfs(graph, edge_node)
	if not node.processed:
		print node.value
		node.processed = True