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