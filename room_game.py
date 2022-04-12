import os
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


def main():
	# It's hard to put more than 40 rooms beacause after dfs algo it's too long to find one all path
	room = Rooms(10)
	position = room.start_room
	while position != room.finish_room:
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f"""You are in the room {position}.
They are three doors in front of you : {room.rooms[position][0]}, {room.rooms[position][1]}, {room.rooms[position][2]}.""")
		try:
			v = int(input('What door you choose ? '))
			if v in room.rooms[position]:
				position = v
			else:
				pass
		except:
			pass

	if position == room.finish_room:
		print("Congratulation, you find the finish room !")
		choice = input("Play again ? [Y/n] ")
		if choice == "Y":
			main()
		else:
			exit()

if __name__ == "__main__":
	main()