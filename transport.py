line_number = 0
jeepneys = []
trains = []

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
	def __init__(self, jeep1, train1):
		self.types = []
		self.initialize(jeep1, train1)

	def initialize(self, jeep1, train1):
		bike = transport()
		bike.set_cost(0)
		bike.set_time(100)

		if jeep1 == 1:
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

class code():
	def __init__(self):
		self.map = []
		self.start = ""
		self.end = ""

	def initialize(self):
		for line in range(line_number):
			jeep1 = 0
			train1 = 0
			if line in jeepneys:
				jeep1 = 1
			if line in trains:
				train1 = 1
			self.map.append(path(jeep1, train1))

	def set_start(self, temp):
		self.start = temp

	def set_end(self, temp):
		self.end = temp

	