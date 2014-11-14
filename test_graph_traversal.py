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
	a : [b, c, e],
	b : [d, f],
	c : [g],
	d : [],
	e : [],
	f : [e],
	g : []
}

graph = Graph(adjacency_list)

#def test_bfs_traverses_all_nodes():

print 'bfs:'
bfs(graph, a)
print '\n'

# reset values
for key in adjacency_list:
	key.processed = False
	key.discovered = False

print 'dfs:'
dfs(graph, a)
