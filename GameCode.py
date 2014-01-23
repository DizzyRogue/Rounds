# TODO add player and game class

class Round:
	target = 0
	throws = 0
	hits = 0	
	round = 1
	mult_score = 0 # Posted to scoreboard once target is advanced
	bonus_score = 0	# Posted to scoreboard once target is advanced
	
	''' Initialize scoreboard for current round '''
	def __init__(self, scoreBoard):
		self.scoreBoard = scoreBoard
	
	def play(self):
		while self.is_game_over() == False and self.throws < 3:
			self.is_game_over()
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
	
	''' Determines if the game is over '''
	def is_game_over(self):
		if self.target == 6 and self.hits >= 3: # MIGHT NEED CODE HERE TO COVER HANGERS ON 15's
			return True
		else:
			return False
	
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
		print "Current Target: " + str(game.target)
		print "Current Round: " + str(game.round)
		print "Throws remaining: " + str(3 - game.throws)
		print "Hits on current target: " + str(game.hits)
		print "Set Mult Score: " + str(game.mult_score)
		print "TOTAL SCORE: " + str(sum(self.scoreBoard.player_scoreboard.values()))
		print "============="
	
	
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

class Scoreboard:

	''' Player's Scoreboard '''
	player_scoreboard = {
		"Bull": 0,
		"20  ": 0,
		"19  ": 0,
		"18  ": 0,
		"17  ": 0,
		"16  ": 0,
		"15  ": 0,
	}

	''' Takes in current target and sets player_scoreboard value for that target '''
	def score_updater(self, target):
		if target == 0:
			self.player_scoreboard['Bull'] = game.mult_score + game.bonus_score
		if target == 1:
			self.player_scoreboard['20  '] = game.mult_score + game.bonus_score
		if target == 2:
			self.player_scoreboard['19  '] = game.mult_score + game.bonus_score
		if target == 3:
			self.player_scoreboard['18  '] = game.mult_score + game.bonus_score
		if target == 4:
			self.player_scoreboard['17  '] = game.mult_score + game.bonus_score
		if target == 5:
			self.player_scoreboard['16  '] = game.mult_score + game.bonus_score
		if target == 6:
			self.player_scoreboard['15  '] = game.mult_score + game.bonus_score

			
''' Game Loop '''
score = Scoreboard()
game = Round(score)
game.play()
