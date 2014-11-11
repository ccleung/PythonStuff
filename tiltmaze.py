#from enum import Enum

#class Direction(Enum):
#	left = 1
#	up = 2
#	right = 3
#	down = 4

'''
'o' is an open position, 'x' is a wall within the maze

Rules: the ball, once in motion, can only roll in one direction
(left, right, up, down) until it hits a wall

e.g., 8x8 array
| o o o o o x o x |
| o o o o x x o o |
| o o o o o o o o |
| x x x x o o o o |
| o o o x o o o x |
| o o o x o o o x |
| o o o x o o o o |
| o o o x o o o o |
'''

size = 8
maze = [ ['o' for x in xrange(size)] for x in xrange(size) ]

y = 0
x = 0
maze[y][x] = '0'

maze[0][5] = 'x'
maze[0][7] = 'x'
maze[4][7] = 'x'
maze[5][7] = 'x'

maze[3][0] = 'x'
maze[3][1] = 'x'
maze[3][2] = 'x'
maze[3][3] = 'x'

maze[4][3] = 'x'
maze[5][3] = 'x'
maze[6][3] = 'x'
maze[7][3] = 'x'


print maze

class Position:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def printPosition(self):
		print "Position %s %s" % (self.x, self.y)

def withinHorizontalLimits(x):
	horizontalMax = len(maze[0])
	print "HORIZONTAL MAX: %s" % horizontalMax
	return x >= 0 and x < horizontalMax

def withinVerticalLimits(y):
	verticalMax = len(maze)
	print "VERTICAL MAX: %s" % verticalMax
	return y >= 0 and y < verticalMax

def moveOneStep(position, direction):
	return {
			'left' : Position(position.x - 1, position.y),
			'up' : Position(position.x, position.y - 1),
			'right' : Position(position.x + 1, position.y),
			'down' : Position(position.x, position.y + 1),
	}[direction]

def getNextPosition(position, direction):
	newPosition = position
	print "NEW POSITION INIT"
	while (withinHorizontalLimits(newPosition.x) and withinVerticalLimits(newPosition.y) and maze[newPosition.y][newPosition.x] != 'x'):
		newPosition = moveOneStep(newPosition, direction)
		print 'incrementing '
		newPosition.printPosition()
	return newPosition


result = getNextPosition(Position(), 'right')
result.printPosition()
print '##################some initial tests'

result = getNextPosition(Position(), 'left')
result.printPosition()
print '##################some initial tests'

result = getNextPosition(Position(), 'up')
result.printPosition()
print '##################some initial tests'

result = getNextPosition(Position(), 'down')
result.printPosition()
print '##################some initial tests'



