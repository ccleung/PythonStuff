from position import Position
from direction import Direction

def withinHorizontalLimits(grid, x):
	horizontalMax = len(grid[0])
	return x >= 0 and x < horizontalMax

def withinVerticalLimits(grid, y):
	verticalMax = len(grid)
	return y >= 0 and y < verticalMax

def moveOneStep(position, direction):
	return {
			Direction.left : Position(position.x - 1, position.y),
			Direction.up : Position(position.x, position.y - 1),
			Direction.right : Position(position.x + 1, position.y),
			Direction.down : Position(position.x, position.y + 1),
	}[direction]

