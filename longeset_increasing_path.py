from grid_traversal_helper import *
from position import Position
from direction import Direction

# always mark down the current depth
# if node is discovered previously, only go down the path if we get a greater path number
# depth first search, with aforementioned way to keep going down more nodes

max_step_value = 0
last_position_in_longest_path = None

max_height = 4
max_width = 4

# record the number of steps taken at each position, and also previous Position we came from
positions_history = [[Position(idx, idy) for idx, x in enumerate(xrange(max_width))] for idy, x in enumerate(xrange(max_height))]


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

def getNextPositions(grid, cur_pos):
	next_positions = []
	for direction in Direction:
		# returns a temporary Position object with x and y position of next step
		proposed_position = moveOneStep(cur_pos, direction)
		#print "PROP POSITION: %s" % proposed_position
		if not withinGridLimits(grid, proposed_position):
			continue
		next_position = positionsHistoryValueAt(proposed_position)
		if (isNextPositionValueGreaterThanCurrentValue(cur_pos, next_position)
			and isPositionVisitable(cur_pos, next_position)):
			next_positions.append(next_position)
	return next_positions

def isNextPositionValueGreaterThanCurrentValue(current_pos, next_pos):
	return getValueAtPosition(numbers, next_pos) > getValueAtPosition(numbers, current_pos)

# if we had visited in the past, compare the visited position's count with our current count
def isPositionVisitable(current_pos, next_pos):
	return positionsHistoryValueAt(next_pos).value <= positionsHistoryValueAt(current_pos).value

def getValueAtPosition(array, position):
	return array[position.y][position.x]

def positionsHistoryValueAt(position):
	return getValueAtPosition(positions_history, position)

# tests
#print "GET POSITIONNNNS::::::"
#for x in getNextPositions(numbers, Position(0,0)):
#	print x

def printResults():
	for idy, x in enumerate(xrange(max_height)):
		for idx, x in enumerate(xrange(max_width)):
			print positions_history[idy][idx]

printResults()

def findLongestIncreasingPath(curr_pos):
	global max_step_value
	global last_position_in_longest_path
	# this should only happened once. For the very first position put in
	position = positionsHistoryValueAt(curr_pos)
	if position.value == 0:
		position.value += 1
	print "CURRENT NODE: %s" % position
	if max_step_value < position.value:
			max_step_value = position.value
			last_position_in_longest_path = position
	for next_pos in getNextPositions(numbers, position):
		# check if our position is still visitable, because some other path might have come here
		# first during recursive dfs
		if isPositionVisitable(position, next_pos):
			# since next_pos already went through validation and is a valid next step
			# capture steps taken by adding 1 more to our aggregate count stored in positions_history[y][x]
			next_pos.value = position.value + 1
			next_pos.prev_position = position
		findLongestIncreasingPath(next_pos)

findLongestIncreasingPath(Position(0,0))
printResults()

print "LAST NODE: %s" % last_position_in_longest_path

print "PATH TO BEGINNING: "
printPath(last_position_in_longest_path)


