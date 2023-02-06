class Item:
	def __init__(self, name, short, skill_bonus, will_bonus):
		#initialises an item object
		self.name = name
		self.short = short
		self.skill_bonus = int(skill_bonus)
		self.will_bonus = int(will_bonus)

	def get_name(self):
		#returns an item's name
		return self.name

	def get_short(self):
		#returns a short description of an item
		return self.short

	def get_info(self):
		#outputs the stats of a given item
		print(self.name)
		print('Grants a bonus of {} to SKILL.'.format(self.skill_bonus))
		print('Grants a bonus of {} to WILL.'.format(self.will_bonus))
		return

	def get_skill(self):
		#returns the Skill bonus of an item
		return self.skill_bonus
	
	def get_will(self):
		#returns the Will bonus of an item
		return self.will_bonus
