class Player:
	player_name = ''
	player_number = 0
	player_target = 0
	player_current_round = 1
	player_hits = 0
	player_multi_bonus = 0
	player_bull = 0
	player_19 = 0
	player_18 = 0
	player_17 = 0
	player_16 = 0
	player_15 = 0
	player_total_score = 0

class GamePlayers:

	''' Player list dictionary, keeps track of player number and player name '''
	player_list = []

	number_of_players = 0
	input_number = 1

	def player_input(self):
		how_many_players = raw_input("Please enter the number of players: ") # TODO, add validation that limits the input to numbers and the number of players to 4
		self.number_of_players = int(how_many_players)
		while self.number_of_players > 0:
			new_player = Player()
			new_player.player_name = raw_input(self.input_prompt() + " enter your name: ")
			new_player.player_number = self.input_number
			self.player_list.append(new_player)
			self.number_of_players -= 1
			self.input_number += 1

	def input_prompt(self):
		return "Player " + str(self.input_number)

class Throw:
	valid_dart = False
	last_dart_input = 0

	''' Dart input function '''
	def throw_dart(self):
		while self.valid_dart == False:
			dart_input = raw_input("Use T, D, S or X to enter dart: ")
			self.last_dart_input = dart_input
			self.is_valid(self.last_dart_input)
		else:
			self.dart_hit_value()
			self.dart_mult_value()

	''' Dart input validation '''		
	def is_valid(self, x):
		if self.last_dart_input == "t" or self.last_dart_input == "d" or self.last_dart_input == "s" or self.last_dart_input == "x":
			self.valid_dart = True
		else:
			self.valid_dart = False
			print "============="
			print "Invalid dart input! Please use T, D, S or X to enter dart."
			print "============="
		
	def dart_hit_value(self):
		return self.hit_calc(self.last_dart_input)
		
	def dart_mult_value(self):
		return self.dart_score(self.last_dart_input)
			
	''' Give hit value to throw input '''
	def hit_calc(self, dart):
		if dart.lower() == "t":
			return 3
		if dart.lower() == "d":
			return 2
		if dart.lower() == "s":
			return 1
		if dart.lower() == "x":
			return 0
	
	''' Give mult value to throw input '''
	def dart_score(self, dart):
		if dart.lower() == "t":
			return 100
		if dart.lower() == "d":
			return 50
		if dart.lower() == "s":
			return 10
		if dart.lower() == "x":
			return 0	

class Round:
	bonus_score = 0	# Posted to scoreboard once target is advanced

	def play(self):
			throw = Throw()
			throw.throw_dart()
			self.hits += throw.dart_hit_value()
			self.mult_score += throw.dart_mult_value()
			self.throws += 1
			self.maxRounds()
			self.nextRound()
			self.is_hanger()
			self.calculate_current_target()
			self.toString()
			if self.is_game_over() == True:
				self.bonus_score = self.round_bonus_score(self.round) # Calculates bonus_score for completed round
				self.scoreBoard.score_updater(self.target) # Set Mult Score and add it to bonus_score for previous round and post it to the scoreboard
				print "============="
				print "GAME OVER!"
				print "Previous round bonus score: " + str(self.bonus_score)
				print "Previous round multi score: " + str(self.mult_score)
				print "============="
				print "Score as of last round: "
				for key in sorted(self.scoreBoard.player_scoreboard.iterkeys(), reverse=True):
					print "%s: %s" % (key, self.scoreBoard.player_scoreboard[key])
				print "============="
				print "YOUR FINAL SCORE: " + str(sum(self.scoreBoard.player_scoreboard.values()))
				print "============="	
	
	
	''' Determine if the user needs to advance to the next round on CURRENT target, then add 1 to round '''
	def nextRound(self):
		if self.hits < 3 and self.throws == 3:
			self.round += 1
			self.throws = 0
			mult_score = 0
			if self.round < 6:
				print "============="
				print "You are still aiming at, " + str(self.target) + ", begin next round!"
			else:
				print "============="
				print "You failed to finish out, " + str(self.target) + ", start round one of next target!"
				
	''' Max round function to prevent user from playing more than 5 rounds in a set '''
	def maxRounds(self):
		if self.round == 6:
			return True
	
	''' Calculate if ready to advance to next target '''
	def newTarget(self):
		if self.target < 6:
			if self.hits >= 3 or self.maxRounds() == True:
				return True
		else:
			return False
	
	''' Calculate & set new target based on when hits > 3 '''
	def calculate_current_target(self):
		if self.newTarget() == True and self.is_hanger() == False: # Advance target, non-hanger workflow
			self.bonus_score = self.round_bonus_score(self.round) # Calculates bonus_score for completed round
			self.scoreBoard.score_updater(self.target) # Set Mult Score and add it to bonus_score for previous round and post it to the scoreboard
			print "============="
			print "Previous round bonus score: " + str(self.bonus_score)
			print "Previous round multi score: " + str(self.mult_score)
			print "============="
			print "Score as of last round: "
			for key in sorted(self.scoreBoard.player_scoreboard.iterkeys(), reverse=True):
				print "%s: %s" % (key, self.scoreBoard.player_scoreboard[key])
			print "============="
			self.target += 1
			self.hits = 0
			self.round = 1
			self.throws = 0
			self.mult_score = 0
			self.bonus_score = 0
		if self.newTarget() == True and self.is_hanger() == True: # Advance target, hanger workflow
			self.bonus_score = self.round_bonus_score(self.round) # Calculates bonus_score for completed round
			self.scoreBoard.score_updater(self.target) # Set Mult Score and add it to bonus_score for previous round and post it to the scoreboard
			print "============="
			print "Previous round bonus score: " + str(self.bonus_score)
			print "Previous round multi score: " + str(self.mult_score)
			print "============="
			print "Score as of last round: "
			for key in sorted(self.scoreBoard.player_scoreboard.iterkeys(), reverse=True):
				print "%s: %s" % (key, self.scoreBoard.player_scoreboard[key])
			print "============="
			print "HANGER TIME!"
			self.hanger_target() # This may need work...
			
		
	''' Calculate if the user has hangers '''	
	def is_hanger(self):
		if self.target < 6:
			if self.throws < 3 and self.hits >=3:
				return True
			else:
				return False
		else:
			return False
			
	''' Special hanger throws function '''		
	def hanger_target(self):
			self.target += 1
			self.hits = 0
			self.round = 0 
			self.mult_score = 0
			self.bonus_score = 0
			
		
	''' Round Bonus point calculation '''
	def round_bonus_score(self, x):
		if x == 0:
			return 250
		if x == 1:
			return 100
		if x == 2:
			return 50
		if x == 3:
			return 25
		if x == 4:
			return 15
		if x == 5:
			return 5
		if x == 6:
			return 0
		

	''' Prints post throw status '''		
	def toString(self):
		print "============="
		#print "Current Player: " + str(game_players.roundPlayers)
		print "Current Target: " + str(new_round.target)
		print "Current Round: " + str(new_round.round)
		print "Throws remaining: " + str(3 - new_round.throws)
		print "Hits on current target: " + str(new_round.hits)
		print "Set Mult Score: " + str(new_round.mult_score)
		#print "TOTAL SCORE: " + str(sum(self.scoreBoard.player_scoreboard.values()))
		print "============="			

class Game:	
	game_players = GamePlayers()

	game_started = 0

	'''Flag to start the game once all players have been entered'''
	while game_started == 0:
		game_players.player_input()
		game_started += 1
	if game_started == 1:
		new_round = Round()
		new_round.play()

	''' Determines if the game is over '''
	def is_game_over(self):
		if self.target == 6 and self.hits >= 3: # MIGHT NEED CODE HERE TO COVER HANGERS ON 15's
			return True
		else:
			return False	


	while self.is_game_over() == False and self.throws < 3:
		pass				


			
''' Game Loop '''


#players = Players()
#enter_players = players.player_input()
#game_players = players.player_list
#score = Scoreboard()
#game = Round(score, game_players)
#game.play()