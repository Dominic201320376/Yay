line_number = 48
trains = {1:[17,33,37,16,18],2:[19,25,32,38,41],3:[30,24,26,27]}

class transport():
	def __init__(self):
		self.time = 0
		self.cost = 0

	def get_cost(self):
		return self.cost

	def get_time(self):
		return self.time

	def set_time(self, temp):
		self.time = temp

	def set_cost(self, temp):
		self.cost = temp

class path():
	def __init__(self, train1, connection):
		self.types = []
		self.connections = connection
		self.initialize(train1)

	def initialize(self, train1):
		bike = transport()
		bike.set_cost(0)
		bike.set_time(100)

		jeep = transport()
		jeep.set_cost(7.50)
		jeep.set_time(70)
		
		taxi = transport()
		taxi.set_cost(40)
		taxi.set_time(30)

		if train1 == 1:
			train = transport()
			train.set_cost(20)
			train.set_time(20)
			self.types.append(train)

		self.types.append(bike)
		self.types.append(jeep)
		self.types.append(taxi)
		
	def add_connection(self, temp):
		self.connections.append(temp)

	def get_connection(self):
		return self.connections

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

			self.map.append(path(train1, connection))


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

	def algorithm(self, start, goal, maps,heuristic):
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
				cost = self.path[curr] + 1
				for move in self.moves:
					#print move.get_connection()
					if move not in self.path or cost < self.path[move]:
						#self.heuristic[move] = heuristic(move, goal) + cost
						self.path[move] = cost
						self.previous[move] = curr
						#self.opened.put(move, cost + self.heuristic[move])
						self.opened.put(move, cost)

		print("No solution")

	def traverse(self, start, goal, previous):
		return

	def generate(self, start, maps, mode=0, extra=None):
		self.moves = []
		temp = start.get_connection()
		#temp = temp[::-1]
		for x in temp:
			if x-1 not in self.path:
				self.moves.append(maps.get_map(x-1))
			#print maps.get_map(x).get_connection()

a = A_star()
b = code()
b.set_start(1)
b.set_end(4)
a.algorithm(b.get_start(), b.get_end(), b, None)