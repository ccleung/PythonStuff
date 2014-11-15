from grid_traversal_helper import *
from position import Position
from direction import Direction

# always mark down the current depth
# if node is discovered previously, only go down the path if we get a greater path number
# depth first search, with aforementioned way to keep going down more nodes

max_height = 4
max_width = 4

# record the number of steps taken at each position
steps_taken = [[0 for x in xrange(max_width)] for x in xrange(max_height)] 

# the 2d array where we need to find the longest path of increasing int's
# no diagnoal movement, only left up right down
numbers = [[0 for x in xrange(max_width)] for x in xrange(max_height)]

'''
|  3   4  2  5   |
|	 1	 7  10 12	 |
|	 5	 8	20 15  |
|	 2	 31	30 40  |
'''

y = 0
x = 0
numbers[y][x] = 3
numbers[0][1] = 4
numbers[0][2] = 2
numbers[0][3] = 5

numbers[1][0] = 1
numbers[1][1] = 7
numbers[1][2] = 10
numbers[1][3] = 12

numbers[2][0] = 5
numbers[2][1] = 8
numbers[2][2] = 20
numbers[2][3] = 15

numbers[3][0] = 2
numbers[3][1] = 31
numbers[3][2] = 30
numbers[3][3] = 40

print numbers

def getNextPositions(grid, position):
	next_positions = []
	for direction in Direction:
		proposed_position = moveOneStep(position, direction)
		print "PROP POSITION: %s" % proposed_position
		if (withinGridLimits(grid, proposed_position) 
			and isNextPositionValueGreaterThanCurrentValue(position, proposed_position) 
			and isPositionVisitable(position, proposed_position)):
			next_positions.append(proposed_position)
	return next_positions

def isNextPositionValueGreaterThanCurrentValue(current_pos, next_pos):
	return getValueAtPosition(numbers, next_pos) > getValueAtPosition(numbers, current_pos)

# if we had visited in the past, compare the visited position's count with our current count
def isPositionVisitable(current_pos, next_pos):
	return getValueAtPosition(steps_taken, next_pos) <= getValueAtPosition(steps_taken, current_pos)

def getValueAtPosition(array, position):
	return array[position.y][position.x]

# tests
#print "GET POSITIONNNNS::::::"
#for x in getNextPositions(numbers, Position(0,0)):
#	print x

def findLongestIncreasingPath(curr_pos):
	# this should only happened once. For the very first position put in
	if steps_taken[curr_pos.y][curr_pos.x] == 0:
		steps_taken[curr_pos.y][curr_pos.x] += 1
	print "CURRENT NODE: %s" % curr_pos
	for next_pos in getNextPositions(numbers, curr_pos):
		# since next_pos already went through validation and is a valid next step
		# capture steps taken by adding 1 more to our aggregate count stored in steps_taken[y][x]
		steps_taken[next_pos.y][next_pos.x] = steps_taken[curr_pos.y][curr_pos.x] + 1
		findLongestIncreasingPath(next_pos)

findLongestIncreasingPath(Position(0,0))
print steps_taken


