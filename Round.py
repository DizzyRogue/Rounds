class Round:

	def __init__(self, roundThrows, roundBonus):
		self.roundThrows = roundThrows
		self.roundBonus = roundBonus


	def play(self, player):
			throw = Throw()
			throw.throw_dart()
			player.hits += throw.dart_hit_value()
			player.multi_bonus += throw.dart_mult_value()
			self.roundThrows += 1
			atMaxRound = Round.maxRounds(player)
			needNextRound = Round.nextRound(player, self.roundThrows)
			isHanger = Round.is_hanger(player, self.roundThrows)
			needNewTarget = Round.newTarget(player, atMaxRound)
			if needNewTarget == True and isHanger == False: # Advance target, non-hanger workflow
				player.bonus_score = player.round_bonus_score(player.round) # Calculates bonus_score for completed round
				player.scoreBoard.score_updater(player.target) # Set Mult Score and add it to bonus_score for previous round and post it to the scoreboard
				print "============="
				print "Previous round bonus score: " + str(player.bonus_score)
				print "Previous round multi score: " + str(player.mult_score)
				print "============="
				print "Score as of last round: "
				for key in sorted(self.scoreBoard.player_scoreboard.iterkeys(), reverse=True):
					print "%s: %s" % (key, self.scoreBoard.player_scoreboard[key])
				print "============="
				player.target += 1
				player.hits = 0
				player.round = 1
				self.throws = 0
				player.mult_score = 0
				self.bonus_score = 0
			if needNewTarget == True and isHanger == True: # Advance target, hanger workflow
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
				self.toString()

			''' TO DO, move this code into Game '''			
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
	
	#''' Calculate & set new target based on when hits > 3 '''
	#@staticmethod
	#def calculate_current_target(player, throws):

		''' Static Methods '''	
	''' Max round function to prevent user from playing more than 5 rounds in a set '''
	@staticmethod
	def maxRounds(player):
		if player.current_round == 6:
			return True
		else:
			return False	


	''' Determine if the user needs to advance to the next round on CURRENT target, then add 1 to round '''
	@staticmethod
	def nextRound(player, throws):
		if player.hits < 3 and throws == 3:
			player.current_round += 1
			throws = 0
			player.mult_score = 0
			if player.current_round < 6:
				print "============="
				print "You are still aiming at, " + str(player.target) + ", begin next round!"
			else:
				print "============="
				print "You failed to finish out, " + str(player.target) + ", start round one of next target!"
				

	
	''' Calculate if ready to advance to next target '''
	@staticmethod
	def newTarget(player, maxRound):
		if player.target < 6:
			if player.hits >= 3 or maxRound == True:
				return True
			else:
				return False
	
		
	''' Calculate if the user has hangers '''
	@staticmethod	
	def is_hanger(player, throws):
		if player.target < 6:
			if throws < 3 and player.hits >=3:
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
	def toString(player):
		print "============="
		#print "Current Player: " + str(game_players.roundPlayers)
		print "Current Target: " + str(new_round.target)
		print "Current Round: " + str(new_round.round)
		print "Throws remaining: " + str(3 - new_round.throws)
		print "Hits on current target: " + str(new_round.hits)
		print "Set Mult Score: " + str(new_round.mult_score)
		#print "TOTAL SCORE: " + str(sum(self.scoreBoard.player_scoreboard.values()))
		print "============="		