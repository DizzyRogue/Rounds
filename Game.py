class Game:	
	game_players = GamePlayers()

	game_started = 0

	'''Flag to start the game once all players have been entered'''
	while game_started == 0:
		game_players.player_input()
		game_started += 1
	if game_started == 1:
		for x in game_players.player_list:
			new_round = Round(0, 0)
			new_round.play(x)


	''' Determines if the game is over '''
	def is_game_over(self):
		if self.target == 6 and self.hits >= 3: # MIGHT NEED CODE HERE TO COVER HANGERS ON 15's
			return True
		else:
			return False	


	while self.is_game_over() == False and self.throws < 3:
		pass				
