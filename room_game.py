import os
from random import randint

#Global var for stop the dfs function
find_path = False

class Rooms:
	def __init__(self, n):
		self.numbers = n
		self.start_room = randint(0, self.numbers - 1)
		self.finish_room = self.set_finish_room()
		self.n_connect = 3
		self.rooms = self.generate_rooms()
		self.link_rooms()
		self.traps = self.trap_rooms()


	def generate_rooms(self):
		"""Generate the rooms dict"""
		return {i:[0 for z in range(self.n_connect)] for i in range(self.numbers)}


	def link_rooms(self):
		"""Generate the path beetween the rooms"""
		for x in range(self.numbers):
			for y in range(self.n_connect):
				self.rooms[x][y] = randint(0, self.numbers - 1)
				self.rooms[self.rooms[x][y]][randint(0, self.n_connect - 1)] = x
		self.number_path = self.dfs(self.rooms, self.start_room, frozenset(), self.finish_room)
		if self.number_path == 0:
			self.link_rooms()
		else:
			find_path = False


	def set_finish_room(self):
		"""Random finish room we just check finish != start room"""
		finish_room = randint(0, self.numbers - 1)
		if finish_room == self.start_room:
			return self.set_finish_room()
		else:
			return finish_room


	def trap_rooms(self):
		"""Define the trap's rooms"""
		return [randint(0, self.numbers - 1)]


	def trap(self, p):
		if p in self.traps:
			self.link_rooms()
			print(f"This room is a trap, all connection have change !")


	def bonus_rooms(self):
		"""Define the bonus rooms"""
		pass


	def dfs(self, g, node, visit, finish_room):
		"""Deep first search algo for check if a path exist"""
		global find_path
		if find_path == True:
			return 0
		if node == finish_room:
			find_path = True
			return 1
		if node in visit:
			return 0
		else:
			visit = visit | {node}
		return sum(self.dfs(g, n, visit, finish_room) for n in g[node])


def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	try:
		n_room = int(input('In how many rooms do you want play (Min. 10 | Max. 200) ? '))
		if 9 < n_room < 201:
			room = Rooms(n_room)
		else:
			main()
	except:
		main()

	position = room.start_room
	n_try = 0
	while position != room.finish_room:
		os.system('cls' if os.name == 'nt' else 'clear')
		# DEV MODE
		print (f"The trap room is {room.traps}, the exit is {room.finish_room}")
		print(f"""You are in the room {position}.
They are three doors in front of you : {room.rooms[position][0]}, {room.rooms[position][1]}, {room.rooms[position][2]}.""")
		room.trap(position)
		try:
			v = int(input('What door you choose ? '))
			if v in room.rooms[position]:
				position = v
				n_try += 1
			else:
				pass
		except:
			pass

	if position == room.finish_room:
		print(f"Congratulation, you find the finish room in {n_try} try !")
		choice = input("Play again ? [Y/n] ")
		if choice == "Y":
			main()
		else:
			exit()

if __name__ == "__main__":
	main()


	