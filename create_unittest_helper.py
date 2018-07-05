import numpy as np
import pygame
from tetris import functions

pygame.init()
pygame.font.init()

size = [800,800]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Unit_Test_Helper")
screen.fill((0, 0, 0))

board = np.zeros((10, 40))

#print button that prints the board when pressed
#x,y,w,h
print_button = (size[0] - 50,  size[1] - 50, 50, 50)
print_text = pygame.font.SysFont('Arial', 11).render('Print', False, (0, 0, 0))




clock = pygame.time.Clock()

done = False
while not done:
    events = pygame.event.get()
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), print_button)
    screen.blit(print_text, (size[0] - 40, size[1] - 40))

    mouse_pos = pygame.mouse.get_pos()
    functions.draw_board(screen, board)


    pygame.display.update()


    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print button pressed
            if size[0] - 50 < mouse_pos[0] < size[0] and size[1] - 50 < mouse_pos[1] < size[1]:
                print('np.' + np.array_repr(board), '\n')
            #board cell pressed
            if 50 < mouse_pos[0] < 360 and 75 < mouse_pos[1] < 695:
                coords = (int((mouse_pos[0] - 50) / 31), int((mouse_pos[1] - 75) / 31) + 20)
                board[coords[0], coords[1]] = (board[coords] + 1) % 8

        if event.type == pygame.QUIT:
            done = True
            #print('np.' + np.array_repr(board), '\n')
            pygame.display.quit()
            pygame.quit()
            break



    clock.tick(30)
