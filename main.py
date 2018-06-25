import numpy as np
import pygame
import piece_generator
from functions import *
from piece_functions import *

#setup
pygame.init()
pygame.font.init()
pygame.mixer.init()

#display setup
size = [800,800]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris")
fps_text = pygame.font.SysFont('Arial', 11)
screen.fill((0, 0, 0))

clock = pygame.time.Clock()

#game board
board = np.zeros((10, 40))
next_piece = None
grab_bag = piece_generator.GrabBag()


#play tetris music forever
pygame.mixer.music.load('tetris_type_a.wav')
pygame.mixer.music.play(-1)


#variables to store if keys are pressed to improve responsiveness
left_arrow = False
right_arrow = False

#counters for figuring out update intervals
left_key_counter = 7
right_key_counter = 7
down_key_counter = 7
up_key_counter = 7
loop_counter = 0

#main loop
done=False

#score keeping
lines_cleared = 0
while not done:
	screen.fill((0,0,0))
	#get events(for key presses)
	events = pygame.event.get()
	keys=pygame.key.get_pressed()

	#check if there is a current piece and spawn one if there isn't
	#also check if game is over
	if np.amax(board) < 10:
		if check_top_out(board):
			done = True

		board, next_piece = spawn_piece(grab_bag, board)

	#check if key is pressed on that frame
	for event in events:

		#keyboard things
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				board = horizontal_update(board, True, False)
				left_key_counter = 7

			if event.key == pygame.K_RIGHT:
				board = horizontal_update(board, False, True)
				right_key_counter = 7

			if event.key == pygame.K_DOWN:
				board = piece_gravity(board)
				down_key_counter = 7

			if event.key == pygame.K_UP:
				board = rotation(board)
				up_key_counter = 7
		#exiting
		if event.type==pygame.QUIT:
			done=True
			break
	#to avoid a segmentation fault when exiting
	if done == True:
		print('Lines Cleared:', lines_cleared)
		pygame.display.quit()
		pygame.mixer.music.stop()
		pygame.quit()
		break

	#check if key is held down
	if keys[pygame.K_LEFT]:
		if left_key_counter <= 0:
			board = horizontal_update(board, True, False)
			left_key_counter = 3
		left_key_counter -= 1

	if keys[pygame.K_RIGHT]:
		if right_key_counter <= 0:
			board = horizontal_update(board, False, True)
			right_key_counter = 3
		right_key_counter -= 1

	if keys[pygame.K_UP]:
		if up_key_counter <= 0:
			board = rotation(board)
			up_key_counter = 3
		up_key_counter -= 1

	if keys[pygame.K_DOWN]:
		if down_key_counter <= 0:
			board = piece_gravity(board)
			board, num_clear = check_line_clear(board)
			lines_cleared += num_clear


			down_key_counter = 3
		down_key_counter -= 1

	if loop_counter % 15 == 0:
		board = piece_gravity(board)
		board, num_clear = check_line_clear(board)
		lines_cleared += num_clear

#get and display fps
	fps = clock.get_fps()
	display_fps(screen, fps_text, fps)

#draw updated board
	draw_board(screen, board)

	display_next_piece(screen, next_piece)

	pygame.display.update()
	loop_counter += 1

    #limit to 30 fps
	clock.tick(30)
