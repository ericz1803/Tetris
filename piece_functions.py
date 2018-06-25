import numpy as np

#tries to move a piece horizontally depending on which keys are pressed
#returns the updated board
def horizontal_update(board, left_pressed, right_pressed):

	#does nothing if both are pressed or neither are pressed
	if left_pressed and right_pressed:
		return board

	#get indices of current piece
	indices_x, indices_y = np.where(board>10)
	if left_pressed:
		counter = 0
		for x, y in zip(indices_x - 1, indices_y):
			#check each of the 4 squares that the piece would move to
			if x < 0:
				continue

			if board[x, y] == 0 or board[x,y] >=10:
				counter += 1

		if counter == 4:
			for (x, y) in zip(indices_x, indices_y):
				board[x,y] = 0
				board[x-1, y] = np.max(board)

	if right_pressed:
		counter = 0
		for x, y in zip(indices_x + 1, indices_y):
			#check that it would still be on the new_board
			if x > 9:
				continue

			if board[x, y] == 0 or board[x, y] >=10:
				counter += 1

		if counter == 4:
			#flip to prevent it from writing over previous blocks with zeros
			for (x, y) in zip(np.flip(indices_x, 0), np.flip(indices_y, 0)):
				board[x,y] = 0
				board[x+1, y] = np.max(board)

	return board

#tries to move the active piece down if possible, if it cannot the piece is locked
#returns updated board
def piece_gravity(board):
	indices_x, indices_y = np.where(board>10)
	counter = 0
	for x, y in zip(indices_x, indices_y+1):
		if y > 39:
			continue

		if board[x, y] == 0 or board[x, y] >=10:
			counter += 1

	if counter == 4:
		for (x, y) in zip(np.flip(indices_x, 0), np.flip(indices_y, 0)):
			board[x, y] = 0
			board[x, y+1] = np.max(board)
	else:
		board = board % 10
	return board

#nintendo rotation system because it's easier to implement
#returns updated board after the rotation (clockwise)
#new value for piece is 1_, 2_, 3_, 4_ depending on the rotation
#indices_x[0], indices_y[0] is always the leftmost then topmost piece
def rotation(board):
	piece_val = np.amax(board).astype(int)

	#store old indices of piece and the ones after rotation
	old_indices_x, old_indices_y = np.where(board>10)
	new_indices_x, new_indices_y = np.zeros_like(old_indices_x), np.zeros_like(old_indices_y)
	#value of squares after rotation
	new_val = 0

	#do nothing if it is an O piece
	if piece_val % 10 == 2:
		return board

	# I piece
	elif piece_val % 10 == 1:
		#horizontal
		if piece_val == 11:
			new_indices_x.fill(old_indices_x[2])
			new_indices_y = np.linspace(old_indices_y[0] - 2, old_indices_y[0] + 1, 4).astype(int)
			new_val = 21
		#vertical
		elif piece_val == 21:
			new_indices_y.fill(old_indices_y[2])
			new_indices_x = np.linspace(old_indices_x[0] - 2, old_indices_x[0] + 1, 4).astype(int)
			new_val = 11

	#S piece
	elif piece_val % 10 == 4:
		if piece_val == 14:
			new_indices_x[0], new_indices_x[1] = old_indices_x[0] + 1, old_indices_x[0] + 1
			new_indices_x[2], new_indices_x[3] = old_indices_x[0] + 2, old_indices_x[0] + 2

			new_indices_y[0] = old_indices_y[0] - 2
			new_indices_y[1], new_indices_y[2] = old_indices_y[0] - 1, old_indices_y[0] - 1
			new_indices_y[3] = old_indices_y[0]
			new_val = 24

		elif piece_val == 24:
			new_indices_x[0] = old_indices_x[0] - 1
			new_indices_x[1], new_indices_x[2] = old_indices_x[0], old_indices_x[0]
			new_indices_x[3] = old_indices_x[0] + 1

			new_indices_y[0], new_indices_y[2] = old_indices_y[0] + 2, old_indices_y[0] + 2
			new_indices_y[1], new_indices_y[3] = old_indices_y[0] + 1, old_indices_y[0] + 1
			new_val = 14

	#Z piece
	elif piece_val % 10 == 5:
		if piece_val == 15:
			new_indices_x[0], new_indices_x[1] = old_indices_x[0] + 1, old_indices_x[0] + 1
			new_indices_x[2], new_indices_x[3] = old_indices_x[0] + 2, old_indices_x[0] + 2

			new_indices_y[0], new_indices_y[3] = old_indices_y[0], old_indices_y[0]
			new_indices_y[1] = old_indices_y[0] + 1
			new_indices_y[2] = old_indices_y[0] - 1
			new_val = 25

		elif piece_val == 25:
			new_indices_x[0] = old_indices_x[0] - 1
			new_indices_x[1], new_indices_x[2] = old_indices_x[0], old_indices_x[0]
			new_indices_x[3] = old_indices_x[0] + 1

			new_indices_y[0], new_indices_y[1] = old_indices_y[0], old_indices_y[0]
			new_indices_y[2], new_indices_y[3] = old_indices_y[0] + 1, old_indices_y[0] + 1
			new_val = 15

	#T piece
	elif piece_val % 10 == 3:
		if piece_val == 13:
			new_indices_x[0], new_indices_x[1], new_indices_x[2] = old_indices_x[0] + 1, old_indices_x[0] + 1, old_indices_x[0] + 1
			new_indices_x[3] = old_indices_x[0] + 2

			new_indices_y[0] = old_indices_y[0] - 1
			new_indices_y[1], new_indices_y[3] = old_indices_y[0], old_indices_y[0]
			new_indices_y[2] = old_indices_y[0] + 1
			new_val = 23

		if piece_val == 23:
			new_indices_x[0] = old_indices_x[0] - 1
			new_indices_x[1], new_indices_x[2] = old_indices_x[0], old_indices_x[0]
			new_indices_x[3] = old_indices_x[0] + 1

			new_indices_y[0], new_indices_y[1], new_indices_y[3] = old_indices_y[0] + 1, old_indices_y[0] + 1, old_indices_y[0] + 1
			new_indices_y[2] = old_indices_y[0] + 2
			new_val = 33

		if piece_val == 33:
			new_indices_x[0] = old_indices_x[0]
			new_indices_x[1], new_indices_x[2], new_indices_x[3] = old_indices_x[0] + 1, old_indices_x[0] + 1, old_indices_x[0] + 1

			new_indices_y[0], new_indices_y[2] = old_indices_y[0], old_indices_y[0]
			new_indices_y[1] = old_indices_y[0] - 1
			new_indices_y[3] = old_indices_y[0] + 1
			new_val = 43

		if piece_val == 43:
			new_indices_x[0] = old_indices_x[0]
			new_indices_x[1], new_indices_x[2] = old_indices_x[0] + 1, old_indices_x[0] + 1
			new_indices_x[3] = old_indices_x[0] + 2

			new_indices_y[0], new_indices_y[2], new_indices_y[3] = old_indices_y[0], old_indices_y[0], old_indices_y[0]
			new_indices_y[1] = old_indices_y[0] - 1
			new_val = 13

	#J piece
	elif piece_val % 10 == 6:
		if piece_val == 16:
			new_indices_x[0], new_indices_x[1], new_indices_x[2] = old_indices_x[0] + 1, old_indices_x[0] + 1, old_indices_x[0] + 1
			new_indices_x[3] = old_indices_x[0] + 2

			new_indices_y[0], new_indices_y[3] = old_indices_y[0], old_indices_y[0]
			new_indices_y[1] = old_indices_y[0] + 1
			new_indices_y[2] = old_indices_y[0] + 2
			new_val = 26

		if piece_val == 26:
			new_indices_x[0] = old_indices_x[0] - 1
			new_indices_x[1] = old_indices_x[0]
			new_indices_x[2], new_indices_x[3] = old_indices_x[0] + 1, old_indices_x[0] + 1

			new_indices_y[0], new_indices_y[1], new_indices_y[2] = old_indices_y[0] + 1, old_indices_y[0] + 1, old_indices_y[0] + 1
			new_indices_y[3] = old_indices_y[0] + 2
			new_val = 36

		if piece_val == 36:
			new_indices_x[0] = old_indices_x[0]
			new_indices_x[1], new_indices_x[2], new_indices_x[3] = old_indices_x[0] + 1, old_indices_x[0] + 1, old_indices_x[0] + 1

			new_indices_y[0], new_indices_y[3] = old_indices_y[0] + 1, old_indices_y[0] + 1
			new_indices_y[1] = old_indices_y[0]
			new_indices_y[2] = old_indices_y[0] - 1
			new_val = 46

		if piece_val == 46:
			new_indices_x[0], new_indices_x[1] = old_indices_x[0], old_indices_x[0]
			new_indices_x[2] = old_indices_x[0] + 1
			new_indices_x[3] = old_indices_x[0] + 2

			new_indices_y[0] = old_indices_y[0] - 2
			new_indices_y[1], new_indices_y[2], new_indices_y[3] = old_indices_y[0] - 1, old_indices_y[0] - 1, old_indices_y[0] - 1
			new_val = 16
	#L piece
	elif piece_val % 10 == 7:
		if piece_val == 17:
			new_indices_x[0], new_indices_x[1], new_indices_x[2] = old_indices_x[0] + 1, old_indices_x[0] + 1, old_indices_x[0] + 1
			new_indices_x[3] = old_indices_x[0] + 2

			new_indices_y[0] = old_indices_y[0] - 1
			new_indices_y[1] = old_indices_y[0]
			new_indices_y[2], new_indices_y[3] = old_indices_y[0] + 1, old_indices_y[0] + 1
			new_val = 27

		if piece_val == 27:
			new_indices_x[0], new_indices_x[1] = old_indices_x[0] - 1, old_indices_x[0] - 1
			new_indices_x[2] = old_indices_x[0]
			new_indices_x[3] = old_indices_x[0] + 1

			new_indices_y[0], new_indices_y[2], new_indices_y[3] = old_indices_y[0] + 1, old_indices_y[0] + 1, old_indices_y[0] + 1
			new_indices_y[1] = old_indices_y[0] + 2
			new_val = 37

		if piece_val == 37:
			new_indices_x[0] = old_indices_x[0]
			new_indices_x[1], new_indices_x[2], new_indices_x[3] = old_indices_x[0] + 1, old_indices_x[0] + 1, old_indices_x[0] + 1

			new_indices_y[0], new_indices_y[1] = old_indices_y[0] - 1, old_indices_y[0] - 1
			new_indices_y[2] = old_indices_y[0]
			new_indices_y[3] = old_indices_y[0] + 1
			new_val = 47

		if piece_val == 47:
			new_indices_x[0] = old_indices_x[0]
			new_indices_x[1] = old_indices_x[0] + 1
			new_indices_x[2], new_indices_x[3] = old_indices_x[0] + 2, old_indices_x[0] + 2

			new_indices_y[0], new_indices_y[1], new_indices_y[3] = old_indices_y[0] + 1, old_indices_y[0] + 1, old_indices_y[0] + 1
			new_indices_y[2] = old_indices_y[0]
			new_val = 17
	else:
		print(piece_val)
		return board

	counter = 0
	for x, y in zip(new_indices_x, new_indices_y):
		#check if off the board
		if x < 0 or x > 9 or y > 39:
			continue
		#check if new square would be empty
		if board[x, y] == 0 or board[x, y] >=10:
			counter += 1

	#replace old tetromino with new one
	if counter == 4:
		for x, y in zip(old_indices_x, old_indices_y):
			board[x, y] = 0
		for x, y in zip(new_indices_x, new_indices_y):
			board[x, y] = new_val

	return board

#returns new board and number of lines cleared
def check_line_clear(board):
	lines_cleared = 0
	#check if piece has been placed
	if np.amax(board) > 10:
		return board, 0
	num_clear = 0
	board = board.T
	for row_i in range(40):
		if np.amin(board[row_i]) > 0:
			num_clear += 1
			board = np.delete(board, (row_i), axis = 0)
			board = np.concatenate((np.zeros((1,10)), board))
	board = board.T
	return board, num_clear

#checks if game is over (top out)
#returns a bool True for game over, False for game not forever
def check_top_out(board):
	return np.max(board[:, :20]) > 0
