from random import randint

class Rooms:
	def __init__(self, n):
		self.numbers = n
		self.start_room = randint(0, self.numbers - 1)
		self.finish_room = self.set_finish_room()
		self.n_connect = 3
		self.rooms = self.generate_rooms()
		self.number_path = self.link_rooms()

		# Commented line until finding a better algo to find the paths in the graph
		# while self.number_path == 0 or self.number_path > self.numbers:
		while self.number_path == 0:
			self.number_path = self.link_rooms()



	def generate_rooms(self):
		"""Generate the rooms dict"""
		return {i:[0 for z in range(self.n_connect)] for i in range(self.numbers)}


	def link_rooms(self):
		"""Generate the path beetween the rooms"""
		for x in range(self.numbers):
			for y in range(self.n_connect):
				self.rooms[x][y] = randint(0, self.numbers - 1)
				self.rooms[self.rooms[x][y]][randint(0, self.n_connect - 1)] = x
		return self.dfs(self.rooms, self.start_room, frozenset(), self.finish_room)

	def set_finish_room(self):
		"""Random finish room we just check finish != start room"""
		finish_room = randint(0, self.numbers - 1)
		if finish_room == self.start_room:
			return self.set_finish_room()
		else:
			return finish_room

	def trap_rooms(self):
		"""Define the trap's rooms"""
		pass


	def bonus_rooms(self):
		"""Define the bonus rooms"""
		pass

	def dfs(self, g, node, visit, finish_room):
		"""Deep first search algo for check if a path exist"""
		if node == finish_room:
			return 1
		if node in visit:
			return 0
		else:
			visit = visit | {node}
		return sum(self.dfs(g, n, visit, finish_room) for n in g[node])

if __name__ == "__main__":
	# It's hard to put more than 40 rooms beacause after dfs algo it's too long to find one all path
	r = Rooms(40)
	print(f'Start room: {r.start_room}, finish room: {r.finish_room}')
	print(f'Number of path: {r.number_path}')
	for x in range(r.numbers):
		print(f'Room {x} link to {r.rooms[x]}')