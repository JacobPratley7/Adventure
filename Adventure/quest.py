class Quest:
	def __init__(self, reward, action, desc, before, after, req, fail_msg, pass_msg, room):
		#initialises a Quest object
		self.reward = reward
		self.action = action
		self.desc = desc
		self.before = before
		self.after = after
		self.req = req
		self.fail_msg = fail_msg
		self.pass_msg = pass_msg
		self.room = room
		#Whether or not the Quest is completed:
		self.complete = False

	def get_info(self):
		#returns a description of a given quest
		return self.desc

	def is_complete(self):
		#returns whether or not the quest has been completed
		return self.complete

	def get_action(self):
		#returns the command/input the user can use to attempt a quest
		return self.action

	def get_room_desc(self):
		#returns a description of the room
		#description depends on whether or not the quest within the room has been completed
		#if statements below decide on which description to output
		if self.is_complete() == True:
			print(self.after)
		else:
			print(self.before)

	def attempt(self, player):
		#allows to player to attempt the given quest
		quest_requirements = self.req.split(" ")
		#splits the requirements into a two components, Skill and Will
		if quest_requirements[0] == 'SKILL':
			#checks to see whether the player has the required Skill level to complete the quest
			if player.get_skill() < int(quest_requirements[1]):
				#in the event of failing the quest
				print(self.fail_msg)
				return
			elif player.get_skill() >= int(quest_requirements[1]):
				#in the event of completing the quest
				self.complete = True
				player.take(self.reward)
				print(self.pass_msg)
				return
		elif quest_requirements[0] == 'WILL':
			#checks to see whether the player has the required Will level to complete the quest
			if player.get_will() < int(quest_requirements[1]):
				#in the event of failing the quest
				print(self.fail_msg)
				return
			elif player.get_will() >= int(quest_requirements[1]):
				#in the event of passing the quest
				self.complete = True
				player.take(self.reward)
				print(self.pass_msg)
				return
