class Node:
	def __init__(self, value, processed=False, discovered=False):
		self.processed = processed
		self.discovered = discovered
		self.value = value