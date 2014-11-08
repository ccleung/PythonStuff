from node import Node
from graph import Graph
from graphtraversal import *

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

adjacency_list = {
	a : [b, c],
	b : [c, d],
	c : [d],
	d : [c , e],
	e : [f],
	f : [c]
}

graph = Graph(adjacency_list)


#def test_bfs_traverses_all_nodes():
bfs(graph, a)