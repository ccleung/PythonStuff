from enum import Enum
import Queue

class Direction(Enum):
	left = 1
	up = 2
	right = 3
	down = 4

class Position(object):
	def __init__(self, x=0, y=0, prev_position = None):
		self.x = x
		self.y = y
		# don't set prev if it is ourselves, end up in an endless loop!
		self._prev_position = prev_position

	@property 
	def prev_position(self):
		return self._prev_position

	@prev_position.setter
	def prev_position(self, p):
		if p is not None and p.x == self.x and p.y == self.y:
			print "Don't set the prev position if we didn't move!"
			#self._prev_position = None
		else:
			self._prev_position = p

	def __str__(self):
		return "Position %s %s and Parent: %s %s" % (self.x, self.y, 
														self.prev_position.x if self.prev_position is not None else 'None', 
														self.prev_position.y if self.prev_position is not None else 'None')

'''
'o' is an open position, 'x' is a wall within the maze

Rules: the ball, once in motion, can only roll in one direction
(left, right, up, down) until it hits a wall

e.g., 8x8 array
| o o o o o x o x |
| o o o o x o o o |
| o o o o o o o o |
| x x x x o o o o |
| o o o x o o o x |
| o o o x o o o x |
| o o o x o o o o |
| o o o o o o o o |

# 'o' = possible move, and not discovered or processed
# 'x' = wall, cannot move
# 'd' = discovered
# 'p' = processed
# 'e' = end position
'''

size = 8
maze = [ ['o' for x in xrange(size)] for x in xrange(size) ]

# end position
maze[7][0] = 'e'

y = 0
x = 0
maze[y][x] = 'o'

maze[1][4] = 'x'

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

#print maze

def withinHorizontalLimits(x):
	horizontalMax = len(maze[0])
	return x >= 0 and x < horizontalMax

def withinVerticalLimits(y):
	verticalMax = len(maze)
	return y >= 0 and y < verticalMax

def isValidPosition(position):
	return withinHorizontalLimits(position.x) and withinVerticalLimits(position.y) and maze[position.y][position.x] != 'x'

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
	while (isValidPosition(proposedPosition)):
		newPosition = proposedPosition
		proposedPosition = moveOneStep(newPosition, direction)

	return newPosition


# position does not move if not possible to move in given direction
def getNextPositions(position):
	next_positions = []
	#print "START ###################"
	for direction in Direction:
		result = getNextPosition(position, direction)
		result.prev_position = position
		print(direction)
		print str(result)
		next_positions.append(result)
	#print "END   ###################"
	return next_positions

middlePosition = Position(4, 3)

getNextPositions(Position())

getNextPositions(middlePosition)

# start at 0,0 can we get to 7,7?
# returns the destination node if found
processed_positions = []
def FindMazePath(start_position):
	# perform bfs to find the destination location
	queue = Queue.Queue()
	queue.put(start_position)
	maze[start_position.y][start_position.x] = 'd'
	while not queue.empty():
		# initialization
		current_position = queue.get()
		print "#### CURRENT POSITION: %s" % str(current_position)
		processed_positions.append(current_position)
		# get next possible moves
		for next_position in getNextPositions(current_position):
			if maze[next_position.y][next_position.x] != 'd':
				if maze[next_position.y][next_position.x] == 'e':
					print "FOUND THE DESTINATION"
					return next_position
				queue.put(next_position)
				# multiple candidates may have this as next step, first to discover the position marks as 'd'
				maze[next_position.y][next_position.x] = 'd'


end_position = FindMazePath(Position(0, 0))
print "END POSITION: %s" % str(end_position)

connected_position = end_position
while (connected_position is not None):
	print "trace back: %s" % str(connected_position)
	connected_position = connected_position.prev_position





