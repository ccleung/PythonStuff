class Position(object):
	def __init__(self, x=0, y=0, prev_position = None):
		self.x = x
		self.y = y
		# don't set prev if it is ourselves, end up in an endless loop!
		self._prev_position = prev_position
		self.value = 0

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
		return "Position %s %s, value: %s and Parent: %s %s" % (self.x, self.y, self.value,
														self.prev_position.x if self.prev_position is not None else 'None', 
														self.prev_position.y if self.prev_position is not None else 'None')