class Adventurer:
	def __init__(self):
		#initialises the adventurer object
		self.inventory = []
		self.skill = 5
		self.will = 5
		self.location = None
		pass

	def get_inv(self):
		#returns the player's inventory
		if len(self.inventory) == 0:
			print('You are carrying:')
			print('Nothing.')
		else:
			print('You are carrying:')
			i = 0
			while i < len(self.inventory):
				print('- A {}'.format(self.inventory[i].get_name()))
				i += 1
			return self.inventory

	def get_skill(self):
		#returns the player's Skill level
		#combines Skill bonuses from items as well as the player's initial skill level
		total_skill = self.skill
		if len(self.inventory) > 0:
			#i = 0
			for object in self.inventory:
				total_skill += int(object.get_skill())
		if total_skill < 0:
			total_skill = 0
		return total_skill

	def get_will(self):
		#returns the player's Will level
		#combines Will bonuses from items as well as the player's initial Will level
		total_will = self.will
		if len(self.inventory) > 0:
			for object in self.inventory:
				total_will += int(object.get_will())
		if total_will < 0:
			total_will = 0
		return total_will
	

	def take(self, item):
		#adds item to the player's inventory
		#used only if a quest has been complete
		self.inventory.append(item)
		return

	def check_self(self):
		#shows the player's stats and all item stats
		if len(self.inventory) == 0:
			print('You are an adventurer, with a SKILL of 5 and a WILL of 5.')
			print('You are carrying:' + '\n')
			print('Nothing.' + '\n')
			print('With your items, you have a SKILL level of 5 and a WILL power of 5.')
		else:
			print('You are an adventurer, with a SKILL of 5 and a WILL of 5.')
			print('You are carrying:' + '\n')
			for object in self.inventory:
				#iterates through the player's inventory and prints the stats of each item
				print(object.get_name())
				print('Grants a bonus of {} to SKILL.'.format(object.get_skill()))
				print('Grants a bonus of {} to WILL.'.format(object.get_will()) + '\n')
			print('With your items, you have a SKILL level of {} and a WILL power of {}.'.format(self.get_skill(), self.get_will()))


	def move_player(self, room):
		#sets the player's location to a room object
		self.location = room
		return

	def player_position(self):
		#returns the player's position
		return self.location
