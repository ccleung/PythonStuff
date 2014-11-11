from enum import Enum

class Direction(Enum):
	left = 1
	up = 2
	right = 3
	down = 4

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
	return x >= 0 and x < horizontalMax

def withinVerticalLimits(y):
	verticalMax = len(maze)
	return y >= 0 and y < verticalMax

def moveOneStep(position, direction):
	return {
			Direction.left : Position(position.x - 1, position.y),
			Direction.up : Position(position.x, position.y - 1),
			Direction.right : Position(position.x + 1, position.y),
			Direction.down : Position(position.x, position.y + 1),
	}[direction]

def getNextPosition(position, direction):
	newPosition = position
	proposedPosition = moveOneStep(newPosition, direction)
	while (withinHorizontalLimits(proposedPosition.x) and withinVerticalLimits(proposedPosition.y) and maze[proposedPosition.y][proposedPosition.x] != 'x'):
		newPosition = proposedPosition
		proposedPosition = moveOneStep(newPosition, direction)
	return newPosition


def getNextPositions(position):
	print "START ###################"
	for direction in Direction:
		result = getNextPosition(position, direction)
		print(direction)
		result.printPosition()
	print "END   ###################"

middlePosition = Position(4, 3)

getNextPositions(Position())

getNextPositions(middlePosition)
#reult =



