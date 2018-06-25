import numpy as np

#standard grab bag style of piece generation (also known as "random bag" or "7 system")
class GrabBag:
	def __init__(self, seed=None):
		#for testing purposes
		np.random.seed(seed)

		#randomly orders integers between 1 and 7
		self.grab_bag = np.arange(1,8)
		np.random.shuffle(self.grab_bag)
		#current keeps track of the current piece
		self.current = 0

	#returns an integer between 1 and 7 for the next piece
	def next(self):
		ret = self.grab_bag[self.current]
		#check if all the pieces are drawn and generate new bag if all pieces are drawn
		if self.current >= 6:
			self.current = 0
			self.grab_bag = np.random.shuffle(self.grab_bag)
		else:
			self.current +=1
		return ret

	#returns a tuple with two integers between 1 and 7 in the format (int next_piece, int preview)
	def next_with_preview(self):
		next_piece = self.grab_bag[self.current]
		#check if all the pieces are drawn and generate new bag if all pieces are drawn
		if self.current >= 6:
			self.current = 0
			np.random.shuffle(self.grab_bag)
		else:
			self.current +=1
		preview = self.grab_bag[self.current]
		return next_piece, preview

#original random style of piece generation
class RandomPiece:
	def __init__(self, seed=None):
		#for testing purposes
		np.random.seed(seed)
		#random number between 1 and 7
		self.current = np.random.randint(1,8)
		self.next = np.random.randint(1,8)

	#returns an integer between 1 and 7 for the next piece
	def next(self):
		ret = self.current
		self.current = self.next
		self.next = np.random.randint(1,8)
		return ret

	#returns a tuple with two integers between 1 and 7 in the format (int next_piece, int preview)
	def next_with_preview(self):
		ret = self.current, self.next
		self.current = self.next
		self.next = np.random.randint(1,8)
		return ret
