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
	def __init__(self):
		self.types = []

	def initialize(self):
		bike = transport()
		bike.set_cost(0)
		bike.set_time(100)

		jeep = transport()
		jeep.set_cost(7.50)
		jeep.set_time(70)

		tricycle = transport()
		tricycle.set_cost(17)
		tricycle.set_time(50)
		
		taxi = transport()
		taxi.set_cost(40)
		taxi.set_time(30)

		self.types.append[bike]
		self.types.append[jeep]
		self.types.append[tricycle]
		self.types.append[taxi]