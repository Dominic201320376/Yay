line_number = 49
trains = {1:[17,33,39,16,18],2:[19,25,34,38,42],3:[31,26,27,28]}

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

def path():
	def __init__(self, train1):
		self.types = []
		self.connections = []
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

		self.types.append(bike)
		self.types.append(jeep)
		self.types.append(taxi)
		self.types.append(train)

	def add_connection(self, temp):
		self.connections.append(temp)

class code():
	def __init__(self):
		self.map = []
		self.start = ""
		self.end = ""

	def initialize(self):
		for line in range(1,line_number+1):
			train1 = 0
			for x in range(1,4):
				if line in trains[x]:
					train1 = 1
					break
			self.map.append(path(train1))

	def set_start(self, temp):
		self.start = temp

	def set_end(self, temp):
		self.end = temp

	def get_start(self):
		return self.start

	def get_end(self):
		return self.end

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

	def algorithm(self, start, goal, heuristic):
		self.previous[start] = None
		self.path[start] = 0
		self.heuristic[start] = heuristic(start, goal)
		self.opened.put(start, 0)
		
		for x in xrange(10000000):
			curr = self.opened.get()

			if curr == goal:
				print "cost:", self.path[curr], "steps:", x
				return self.path[curr], x, self.traverse(start, goal, self.previous)

			else:
				self.generate(curr)
				cost = self.path[curr] + 1
				for move in self.moves:
					if move not in self.path or cost < self.path[move]:
						self.heuristic[move] = heuristic(move, goal) + cost
						self.path[move] = cost
						self.previous[move] = curr
						self.opened.put(move, cost + self.heuristic[move])

		print("No solution")

a = A_star()
b = code()
b.set_start(None)
b.set_end(None)
a.algorithm(b.get_start(), b.get_end(), None)