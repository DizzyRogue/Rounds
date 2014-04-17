class GamePlayers:

	''' Player list dictionary, keeps track of player number and player name '''
	player_list = []

	number_of_players = 0
	input_number = 1

	def player_input(self):
		how_many_players = raw_input("Please enter the number of players: ") # TODO, add validation that limits the input to numbers and the number of players to 4
		self.number_of_players = int(how_many_players)
		while self.number_of_players > 0:
			new_player = Player('', 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
			new_player.player_name = raw_input(self.input_prompt() + " enter your name: ")
			new_player.player_number = self.input_number
			self.player_list.append(new_player)
			self.number_of_players -= 1
			self.input_number += 1

	def player_return(self):
		return self.player_list

	def input_prompt(self):
		return "Player " + str(self.input_number)