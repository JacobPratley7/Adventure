class Room:
	def __init__(self, name):
		#Initialises the room
		self.name = name
		self.north_exit = 0
		self.south_exit = 0
		self.east_exit = 0
		self.west_exit = 0
		self.north = None
		self.south = None
		self.west = None
		self.east = None
		self.short_desc = None
		self.has_quest = False
		self.quest = None

		
	def get_name(self):
		#returns the room name
		return self.name

	def get_short_desc(self):
		#returns a description of the room.
		if self.quest == None:
			print('There is nothing in this room.')
		else:
			self.quest.get_room_desc()


	def get_quest_action(self):
		#returns a comand that the user can input to complete a quest, if a quest exists in the room
		if self.quest == None:
			print('You can''t be done')
		else:
			print(self.quest.get_info())
		return
			
	def set_quest(self, q):
		#assigns the room object a quest object
		self.quest = q
		self.has_quest = True
		return self.quest


	def get_quest(self):
		#returns a quest object that can be completed in the room
		return self.quest
		
	def set_path(self, dir, dest):
		#creates a path whicj leads from the current room to another room
		self.dir = dir
		self.dest = dest
		if self.dir == 'NORTH':
			self.north = dest
			self.north_exit = 1
		elif self.dir == 'SOUTH':
			self.south = dest
			self.south_exit = 1
		elif self.dir == 'EAST':
			self.east = dest
			self.east_exit = 1
		elif self.dir == 'WEST':
			self.west = dest
			self.west_exit = 1
		else:
			print('Invalid direction.')


	def draw(self):
		#creates a drawing depicting the current room the player is in, including all exits for the room
		#below is a group of variables I've created, each one representing one of the possible lines that can be printed
		a = '+--------------------+'
		a_n = '+---------NN---------+'
		a_s = '+---------SS---------+'
		b = '|                    |'
		b_e = '|                    E'
		b_w = 'W                    |'
		b_ew = 'W                    E'
		print('')
		#the following if statements check what exits exist within the room and decides on which of the variables above should be printed
		if self.north_exit == 1:
			print(a_n)
		else:
			print(a)
		print(b)
		print(b)
		print(b)
		print(b)
		if self.west_exit and self.east_exit == 1:
			print(b_ew)
		elif self.west_exit == 1 and self.east_exit == 0:
			print(b_w)
		elif self.west_exit == 0 and self.east_exit == 1:
			print(b_e)
		else:
			print(b)
		print(b)
		print(b)
		print(b)
		print(b)
		if self.south_exit == 1:
			print(a_s)
		else:
			print(a)
		print("You are standing at the {}.".format(self.get_name()))
		self.get_short_desc()
		

	def move(self, dir):
		#returns an ajoining room based on the desrciption given
		if dir == 'NORTH':
			return self.north
		elif dir == 'SOUTH':
			return self.south
		elif dir == 'EAST':
			return self.east
		elif dir == 'WEST':
			return self.west
		else:
			return None
