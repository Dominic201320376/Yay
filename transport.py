line_number = 48
trains = {1:[17,33,37,16,18],2:[19,25,32,38,41],3:[30,24,26,27]}

class path():
	def __init__(self, train1, connection, line):
		self.types = {}
		self.connections = connection
		self.line = line
		self.initialize(train1)

	def initialize(self, train1):
		self.types[100] = 0
		self.types[30] = 40

		if train1 == 1:
			self.types[20] = 20
		
	def add_connection(self, temp):
		self.connections.append(temp)

	def get_connection(self):
		return self.connections

	def get_types(self):
		return self.types

	def get_line(self):
		return self.line

class code():
	def __init__(self):
		self.map = []
		self.start = 0
		self.end = 0
		self.initialize()

	def initialize(self):
		for line in range(1,line_number+1):
			train1 = 0
			for x in range(1,4):
				if line in trains[x]:
					train1 = 1
					break
			connection = []

			if line == 1:
				connection.append(2)
				connection.append(7)

			elif line == 2:
				connection.append(1)
				connection.append(3)
				connection.append(4)
				connection.append(7)
				connection.append(8)

			elif line == 3:
				connection.append(2)
				connection.append(4)
				connection.append(8)

			elif line == 4:
				connection.append(2)
				connection.append(3)
				connection.append(5)
				connection.append(8)
				connection.append(9)
				connection.append(11)			

			elif line == 5:
				connection.append(4)
				connection.append(6)
				connection.append(9)
				connection.append(11)
				connection.append(13)

			elif line == 6:
				connection.append(5)
				connection.append(13)

			elif line == 7:
				connection.append(1)
				connection.append(2)
				connection.append(15)
				connection.append(16)
				connection.append(17)

			elif line == 8:
				connection.append(2)
				connection.append(3)
				connection.append(4)
				connection.append(9)	
				connection.append(14)

			elif line == 9:
				connection.append(4)
				connection.append(5)
				connection.append(8)
				connection.append(11)
				connection.append(14)

			elif line == 10:
				connection.append(11)
				connection.append(12)
				connection.append(18)
				connection.append(19)

			elif line == 11:
				connection.append(4)
				connection.append(5)
				connection.append(9)
				connection.append(10)
				connection.append(12)

			elif line == 12:
				connection.append(10)
				connection.append(11)
				connection.append(13)
				connection.append(20)
				connection.append(21)

			elif line == 13:
				connection.append(5)
				connection.append(6)
				connection.append(12)
				connection.append(20)
				connection.append(21)

			elif line == 14:
				connection.append(8)
				connection.append(9)
				connection.append(16)
				connection.append(18)

			elif line == 15:
				connection.append(7)
				connection.append(16)
				connection.append(17)

			elif line == 16:
				connection.append(7)
				connection.append(14)
				connection.append(15)
				connection.append(17)
				connection.append(18)

			elif line == 17:
				connection.append(7)
				connection.append(15)
				connection.append(16)
				connection.append(22)
				connection.append(30)
				connection.append(33)

			elif line == 18:
				connection.append(10)
				connection.append(14)
				connection.append(16)
				connection.append(19)

			elif line == 19:
				connection.append(10)
				connection.append(18)
				connection.append(20)
				connection.append(22)
				connection.append(25)

			elif line == 20:
				connection.append(12)
				connection.append(13)
				connection.append(19)
				connection.append(21)
				connection.append(22)
				connection.append(25)

			elif line == 21:
				connection.append(12)
				connection.append(13)
				connection.append(20)
				connection.append(26)
				connection.append(27)
				connection.append(28)

			elif line == 22:
				connection.append(17)
				connection.append(19)
				connection.append(20)
				connection.append(25)
				connection.append(30)
				connection.append(33)

			elif line == 23:
				connection.append(27)
				connection.append(28)
				connection.append(29)
				connection.append(34)

			elif line == 24:
				connection.append(25)
				connection.append(26)
				connection.append(30)
				connection.append(31)
				connection.append(32)

			elif line == 25:
				connection.append(19)
				connection.append(20)
				connection.append(22)
				connection.append(24)
				connection.append(26)
				connection.append(32)

			elif line == 26:
				connection.append(21)
				connection.append(24)
				connection.append(25)
				connection.append(27)
				connection.append(28)
				connection.append(32)
				
			elif line == 27:
				connection.append(21)
				connection.append(23)
				connection.append(26)
				connection.append(28)
				connection.append(29)

			elif line == 28:
				connection.append(21)
				connection.append(23)
				connection.append(26)
				connection.append(27)
				connection.append(34)

			elif line == 29:
				connection.append(23)
				connection.append(27)

			elif line == 30:
				connection.append(17)
				connection.append(22)
				connection.append(24)
				connection.append(31)
				connection.append(33)

			elif line == 31:
				connection.append(24)
				connection.append(30)
				connection.append(32)
				connection.append(35)
				connection.append(38)	

			elif line == 32:
				connection.append(24)
				connection.append(25)
				connection.append(26)
				connection.append(31)
				connection.append(35)
				connection.append(38)

			elif line == 33:
				connection.append(17)
				connection.append(22)
				connection.append(30)
				connection.append(37)
				connection.append(39)

			elif line == 34:
				connection.append(23)
				connection.append(28)
				connection.append(35)
				connection.append(36)
				connection.append(43)

			elif line == 35:
				connection.append(31)
				connection.append(32)
				connection.append(34)
				connection.append(36)
				connection.append(38)
				connection.append(43)

			elif line == 36:
				connection.append(34)
				connection.append(35)
				connection.append(43)

			elif line == 37:
				connection.append(33)
				connection.append(39)
				connection.append(40)
				connection.append(41)
				connection.append(44)

			elif line == 38:
				connection.append(31)
				connection.append(32)
				connection.append(35)
				connection.append(39)
				connection.append(41)
				connection.append(42)

			elif line == 39:
				connection.append(33)
				connection.append(37)
				connection.append(38)
				connection.append(41)
				connection.append(42)

			elif line == 40:
				connection.append(37)
				connection.append(41)
				connection.append(44)

			elif line == 41:
				connection.append(37)
				connection.append(38)
				connection.append(39)
				connection.append(40)
				connection.append(42)
				connection.append(44)

			elif line == 42:
				connection.append(38)
				connection.append(39)
				connection.append(41)
				connection.append(43)
				connection.append(45)
				connection.append(46)

			elif line == 43:
				connection.append(34)
				connection.append(35)
				connection.append(36)
				connection.append(42)
				connection.append(45)
				connection.append(46)

			elif line == 44:
				connection.append(37)
				connection.append(40)
				connection.append(41)

			elif line == 45:
				connection.append(42)
				connection.append(43)
				connection.append(46)
				connection.append(47)
				connection.append(48)

			elif line == 46:
				connection.append(42)
				connection.append(43)
				connection.append(45)
				connection.append(47)
				connection.append(48)

			elif line == 47:
				connection.append(45)
				connection.append(46)
				connection.append(48)

			elif line == 48:
				connection.append(45)
				connection.append(46)
				connection.append(47)

			self.map.append(path(train1, connection, line))


	def set_start(self, temp):
		self.start = self.map[temp-1]

	def set_end(self, temp):
		self.end = self.map[temp-1]

	def get_start(self):
		return self.start

	def get_end(self):
		return self.end

	def get_map(self, temp):
		return self.map[temp]

class priority_queue():
	def __init__(self):
		self.elements = {}
	
	def put(self, node, cost):
		self.elements[node] = cost
   
	def get(self):
		temp = min(cost[1] for cost in self.elements.items())
		for x in self.elements.keys():
			if self.elements[x] == temp:
				self.elements.pop(x)
				return x
		return None

class A_star():
	def __init__(self):
		self.opened = priority_queue()
		self.previous = {}
		self.path = {}
		self.heuristic = {}
		self.moves = []

	def algorithm(self, start, goal, maps, type1, heuristic):
		self.previous[start] = None
		self.path[start] = 0
		#self.heuristic[start] = heuristic(start, goal)
		self.opened.put(start, 0)
		
		for x in xrange(10000000):
			curr = self.opened.get()
			
			if curr == goal:
				print "cost:", self.path[curr], "steps:", x
				return self.path[curr], x, self.traverse(start, goal, self.previous)

			else:
				self.generate(curr, maps)
				if type1 == 0:
					cost = self.path[curr] + 100
				for move in self.moves:
					if type1 == 1:
						temp = move.get_types()
						try:
							cost = self.path[curr] + temp[20]
						except:
							cost = self.path[curr] + temp[30]
					if move not in self.path or cost < self.path[move]:
						#self.heuristic[move] = heuristic(move, goal) + cost
						self.path[move] = cost
						self.previous[move] = curr
						#self.opened.put(move, cost + self.heuristic[move])
						self.opened.put(move, cost)

		print("No solution")

	def traverse(self, start, goal, previous):
		curr = goal
		x = [curr]
		while curr != start:
			curr = previous[curr]
			x.append(curr)
		x.reverse()

		for a in x:
			print a.get_line()

	def generate(self, start, maps, mode=0, extra=None):
		self.moves = []
		temp = start.get_connection()
		for x in temp:
			self.moves.append(maps.get_map(x-1))

a = A_star()
b = code()
b.set_start(1)
b.set_end(48)
a.algorithm(b.get_start(), b.get_end(), b, 1, None)