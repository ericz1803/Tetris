import numpy as np
import pygame

#I=1, O=2, T=3, S=4, Z=5, J=6, L=7
#10 plus value for current piece

#draws board from a grid of numbers
def draw_board(screen, board = np.zeros((10, 40))):

	assert(board.shape == (10,40))
	show = board[:, 20:]
	block_size = 30

	#x_margin away from left edge
	x_margin = 50
	#y_margin away from top edge
	y_margin = 75
	#border = pixels between boxes
	border = 1


	#colors for the pieces
	#no  piece = white
	white = (255, 255, 255)

	#I piece = cyan
	cyan = (0, 225, 255)

	#O piece = yellow
	yellow = (255, 255, 0)

	#T piece = purple
	purple = (177, 13, 201)

	#S piece = green
	green = (46, 204, 64)

	#Z piece = red
	red = (252, 56, 45)

	#J piece = blue
	blue = (0, 116, 217)

	#L piece = orange
	orange = (255, 133, 27)

	colors = [white, cyan, yellow, purple, green, red, blue, orange]

	for x in range(10):
		for y in range(20):
			#draw 10x20 grid of block_size x block_size squares with a 1 px border between each box
			pygame.draw.rect(screen, colors[int(show[x,y]%10)], (x_margin + (block_size+border)*x, y_margin + (block_size+border)*y, block_size, block_size))

	return None

#returns new_board, next_piece
def spawn_piece(generator, board):
	#get current and next piece
	current, next = generator.next_with_preview()
	#I piece
	if current == 1:
		board[3:7, 18] = 11

	#O piece
	elif current == 2:
		board[4:6, 18:20] = 12

	#T piece
	elif current == 3:
		board[4, 18] = 13
		board[3:6, 19] = 13

	#S piece
	elif current == 4:
		board[4:6, 18] = 14
		board[3:5, 19] = 14

	#Z piece
	elif current == 5:
		board[3:5, 18] = 15
		board[4:6, 19] = 15

	#J piece
	elif current == 6:
		board[3, 18] = 16
		board[3:6, 19] = 16

	#Z piece
	elif current == 7:
		board[5, 18] = 17
		board[3:6, 19] = 17

	return board, next

#displays fps in the top right corner
def display_fps(screen, text_fps, fps):
	text = text_fps.render('fps: ' + str(np.round(fps, 2)), False, (255,255,255))
	screen.blit(text, (screen.get_size()[0] - 50, 7))


def display_next_piece(screen, next_piece):
		coords = (400, 350)
		block_size = 30
		#border between blocks
		border = 1

		#border
		background_color = (0, 0, 0)
		border_color = (255, 255, 255)

		border_thickness = 5
		pygame.draw.rect(screen, border_color, (coords[0] - (10 + border_thickness), coords[1] - (45 + border_thickness), 20 + 2 * border_thickness + 4 * (block_size + border), 55 + 2 * border_thickness + 2 * (block_size + border)))
		pygame.draw.rect(screen, background_color, (coords[0] - 10, coords[1] - 45, 20 + 4 * (block_size + border), 55 + 2 * (block_size + border)))

		#text that says 'next piece'
		font = pygame.font.SysFont('Arial', 24)
		text = font.render('Next Piece:', False, (255,255,255))
		screen.blit(text, (coords[0], coords[1] - 35))

		#colors
		#I piece = cyan
		cyan = (0, 225, 255)

		#O piece = yellow
		yellow = (255, 255, 0)

		#T piece = purple
		purple = (177, 13, 201)

		#S piece = green
		green = (46, 204, 64)

		#Z piece = red
		red = (252, 56, 45)

		#J piece = blue
		blue = (0, 116, 217)

		#L piece = orange
		orange = (255, 133, 27)

		colors = [background_color, cyan, yellow, purple, green, red, blue, orange]

		#define the displays for each of the pieces
		if next_piece == 1:
			disp = np.array([[0, 0, 0, 0],
							[1, 1, 1, 1]])
		elif next_piece == 2:
			disp = np.array([[2, 2, 0, 0],
							[2, 2, 0, 0]])
		elif next_piece == 3:
			disp = np.array([[0, 3, 0, 0],
							[3, 3, 3, 0]])
		elif next_piece == 4:
			disp = np.array([[0, 4, 4, 0],
							[4, 4, 0, 0]])
		elif next_piece == 5:
			disp = np.array([[5, 5, 0, 0],
							[0, 5, 5, 0]])
		elif next_piece == 6:
			disp = np.array([[6, 0, 0, 0],
							[6, 6, 6, 0]])
		elif next_piece == 7:
			disp = np.array([[0, 0, 7, 0],
							[7, 7, 7, 0]])
		else:
			disp = np.array([[0, 0, 0, 0],
							[0, 0, 0, 0]])

		disp = disp.T
		#draw it so only the piece is visible
		for x in range(4):
			for y in range(2):
				pygame.draw.rect(screen, colors[int(disp[x,y]%10)], (coords[0] + (block_size+border)*x, coords[1] + (block_size+border)*y, block_size, block_size))
