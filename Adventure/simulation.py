from room import Room
from item import Item
from adventurer import Adventurer
from quest import Quest
import sys
##################################################################################
#Required Functions

def read_paths(source):
	#returns a list of lists according to the specification of a configuration file
	#configuration file will be given as a command line arguement
	f = open(source, 'r')
	#opens the file for reading
	the_paths = [] #list to be returned
	while True:
		line = f.readline()
		line = line.rstrip('\n')
		#reads each line a strips the new line character from the end
		if line == '':
			#breaks the loop when there are no more lines in the config file
			break
		else:
			split_line = line.split(' > ')
			#splits each line into 3 components: starting point, direction and destination
			if len(split_line) != 3:
				#breaks the loop if a line does not have 3 components (as the program needs 3 in order to run)
				break
			else:
				single_path = []
				single_path.append(split_line[0])
				single_path.append(split_line[1])
				single_path.append(split_line[2])
				#creates a path using the 3 main components
				the_paths.append(single_path)
				#appends all path objects to one main list
	return the_paths


def create_rooms(all_paths):
	#uses the list of paths recieved from the read_paths function and creates a list of rooms based on this
	myrooms = [] #list to be returned
	list_of_names = []
	for room_object in all_paths:
		#below, I've assigned a variable to each of the components of a path
		starting_room = room_object[0]
		room_direction = room_object[1]
		finishing_room = room_object[2]
		
		#the following if statements iterates through list_of_names to see if a given item has already been added to the list
		#the following blocks prevent the creation of duplicate rooms, as it only adds the item if it does no yet exist inside the list
		if starting_room in list_of_names: # checks to see if the starting_room is already in the list
			pass
		else:
			#appends the item to the list in the case that it is not
			list_of_names.append(starting_room) 
			myrooms.append(Room(starting_room)) # appends the object to the list to be returned as a Room object

		if finishing_room in list_of_names: #checks to see if finishing_room is already in the lsit
			pass
		else:
			#appends the item to the list in the case that it is not
			list_of_names.append(finishing_room)
			myrooms.append(Room(finishing_room)) # appends the item to the list to be returned as a Room object

		index_start = list_of_names.index(starting_room) # here, we store the index of the starting room as a variable, for the purposes of readability
		index_destination = list_of_names.index(finishing_room) # here, we store the index of the destination as a variable, for the purposes of readability
		# here, we take the index of the starting room and the destination room. We use the set_path method, as well as the indexes we have obtained in order to link the starting room to the correct destination.
		myrooms[index_start].set_path(room_direction, myrooms[index_destination])
	return myrooms


def generate_items(source):
	#returns a list of item objects according to the specifications of a config' file
	#config' file will be given as a command line arguement
	f = open(source, 'r') #opens the config' file for reading
	all_items = [] #list to be returned
	while True:
		line = f.readline()
		line = line.rstrip('\n')
		#reads a line, then strips the newline character from the end
		if line == '':
			#breaks the loop once there are no more lines to be read
			break
		else:
			split_line = line.split(' | ') #splits the line into individual components
			single_item = Item(split_line[0], split_line[1], split_line[2], split_line[3]) #creates an item object using these components
			all_items.append(single_item) #appends the item object to the list to be returned
	
	return all_items


def generate_quests(source, items, rooms):
	#returns a list of quest objects according to the specifications of a config' file
	#config' file will be given as a command line arguement
	f = open(source, 'r') #opens the config' file for reading
	all_quests = [] #list to be returned
	i = 0
	d = 0
	read_file = f.read() #reads the file
	generated_quests = []
	completed_file = read_file.split('\n') #splits the new line character off the end of the lines in the config' file
	for lines in completed_file:
		split_file = lines.split(' | ')
		#iterates through each line and splits it into individual components
		if len(split_file) != 9:
			#checks whether the length of the line object is 9
			#pass in the case that the length of the line is not 9, as the program will not work witha quest object with any more/less components than 9
			pass
		else:
			#creates a quest object
			single_quest = Quest(split_file[0], split_file[1], split_file[2], split_file[3], split_file[4], split_file[5], split_file[6], split_file[7], split_file[8])

			for object in items:
				#searches through the provided item list for an item object with the same name as the quest reward
				if object.get_name() == single_quest.reward:
					single_quest.reward = object
			
			for room_object in rooms:
				#this is where we iterate through quests and assign them to the appropriate room
				#searches through the room list provided and searches for a room that matches a quests room name
				if room_object.name == single_quest.room:
					room_object.set_quest(single_quest) #this is where the quest is set for the given room
			
			generated_quests.append(single_quest)
				
	return generated_quests
###################################################################################################################################################3
#Prior loop
#this is where a majority of the error checking is done
#it ensures that all the configuration files are working and that the right amount of files were provided
#if an errors occur, the program exits

if len(sys.argv) != 4:
	#checks whether or not the correct amount of command line arguements were provided
	print("Usage: python3 simulation.py <paths> <items> <quests>")
	sys.exit()
	

try:
	#checks whether the paths configuration file can be read
	paths_list = read_paths(sys.argv[1])
	rooms_list = create_rooms(paths_list)
	
except Exception:
	#excepts the Exception and quits the program
	print('Please specify a valid configuration file.')
	sys.exit()

try:
	#checks whether or not the items configuration file cis working and can be read
	list_items = generate_items(sys.argv[2])
	
except Exception:
	#excepts the Exception and quits the program
	print('Please specify a valid configuration file.')
	sys.exit()

try:
	#checks whether the quests configration file is working and can be read
	list_of_quests = generate_quests(sys.argv[3], list_items, rooms_list)
	
except Exception:
	#excepts the Exception and quits the program
	print('Please specify a valid configuration file.')
	sys.exit()
	
#Main Loop

player = Adventurer() #initialised the adventurer here
	
try: #checks whether any rooms exist and hence can be drawn. Quits the program if no rooms exist
	player.move_player(rooms_list[0])
	player.player_position().draw()
except Exception:
	print('No rooms exist! Exiting program...')
	sys.exit()
		
#beggining of the loop	
while True:
	print('')
	user_input = input('>>> ').upper() # forced upper case here to avoid any issues with case sensitivity
	# Quit command
	if user_input == 'QUIT':
		print('Bye!')
		sys.exit()
	# Help command
	elif user_input == 'HELP':
		print('HELP       - Shows some available commands.')
		print('LOOK or L  - Lets you see the map/room again.')
		print('QUESTS     - Lists all your active and completed quests.')
		print('INV        - Lists all the items in your inventory.')
		print('CHECK      - Lets you see an item (or yourself) in more detail.')
		print('NORTH or N - Moves you to the north.')
		print('SOUTH or S - Moves you to the south.')
		print('EAST or E  - Moves you to the east.')
		print('WEST or W  - Moves you to the west.')
		print('QUIT       - Ends the adventure.')
	# Look command
	elif user_input == 'LOOK' or user_input == 'L':
		# draws a room, based on the position of the player
		player.player_position().draw()
	# Quest command	
	elif user_input == 'QUESTS':
		# each line of output has 4 main parts: a NUMBER, a NAME, a DESCRIPTION, and a COMPLETION STATUS
		quest_num = 0 # assigns a number to each quest
		i = 0
		completed_quests = 0 # keeps track of how many quests have been completed
		if len(list_of_quests) == 0: # handles the case where there aren't any quests to be completed
			print('')
			print('=== All quests complete! Congratulations! ===')
			sys.exit()
		while i < len(list_of_quests): # iterates through each quest in the main list of quests

			NAME = list_of_quests[i].reward.get_name().ljust(21) # left justified used to ensure that the quest's name is padded out to 21 characters
			DESC = list_of_quests[i].get_info()
			COMP = ""
			if list_of_quests[i].is_complete(): # checks whether the quest has been completed, changes its completion status accordingly
				COMP = ' [COMPLETED]'
				completed_quests += 1
			print("#{:02d}: {}- {}{}".format(quest_num, NAME, DESC, COMP))
			i += 1
			quest_num += 1
		if completed_quests == len(list_of_quests): #checks if all quests have been completed
			print('')
			print("=== All quests complete! Congratulations! ===")
			sys.exit()
	# Inventory command		
	elif user_input == 'INV':
		# calls on function to output the player's inventory
		player.get_inv()
	# Check command	
	elif user_input == 'CHECK':
		second_input = input('Check what? ').upper() # second input, only used in the 'CHECK' command 
		print('')
		if second_input == 'ME':
			# calls on function to output the player's info
			player.check_self()
		else:
			for object in player.inventory: # iterates through the players inventory and tries to locate an item based on the player/user's input
				if object.name.upper() == second_input or object.short.upper() == second_input: # checks if the user's input matches an item's name or short name
					object.get_info() #outputs the items info
					print('')
					break

			else:
				print('You don\'t have that!')
	# below are the directional commands: 'NORTH','N','EAST','E','SOUTH', 'S', and 'WEST', 'W' 		
	elif user_input == 'NORTH' or user_input == 'N':
		if player.player_position().move('NORTH') == None: # checks the case in which no north exit exists
			print('You can\'t go that way.')
		else:
			player.move_player(player.player_position().move('NORTH')) # moves the player to an ajoining room in the north direction
			# prints the direction of movement and the new location
			# draws new room after this
			print('You move to the north, arriving at the {}.'.format(player.player_position().get_name()))
			player.player_position().draw()

	elif user_input == 'SOUTH' or user_input == 'S':
		if player.player_position().move('SOUTH') == None: # checks the case in which no south exits exist
			print('You can\'t go that way.')
		else:
			player.move_player(player.player_position().move('SOUTH')) # moves the player to an ajoining room in the south direction
			# prints the direction of movement and the new location
			# draws new room after this
			print('You move to the south, arriving at the {}.'.format(player.player_position().get_name()))
			player.player_position().draw()
			
	elif user_input == 'EAST' or user_input == 'E':
		if player.player_position().move('EAST') == None: # checks the case in which no east exits exist
			print('You can\'t go that way.')
		else:
			player.move_player(player.player_position().move('EAST')) # moves the player to an ajoining room in the east direction
			# prints the direction of movement and the new location
			# draws new room after this
			print('You move to the east, arriving at the {}.'.format(player.player_position().get_name())) 
			player.player_position().draw()
			
	elif user_input == 'WEST' or user_input == 'W':
		if player.player_position().move('WEST') == None: # checks the case in which no west exits exist
			print('You can\'t go that way.')
		else:
			player.move_player(player.player_position().move('WEST')) # moves the player to an ajoining room in the west direction
			# prints the direction of movement and the new location
			# draws new room after this
			print('You move to the west, arriving at the {}.'.format(player.player_position().get_name()))
			player.player_position().draw()
	# Handles any other command		
	else:
		try:
			# checks whether the input was a quest action
			if user_input == player.player_position().get_quest().get_action():
				if player.player_position().get_quest().is_complete() == True: # checks to see if the quest has already been completed
					print('You have already completed this quest.')
				else:
					player.player_position().get_quest().attempt(player) # allows the player to attempt the quest
			else:		
				print('You can\'t do that.')
				
		except Exception as Error: # Handles the case in which no quests exist within the room.
			#print(Error)
			print('You can\'t do that.')
