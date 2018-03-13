#tic tac toe game

#imports
import pygame

#set up pygame
def pygame_setup():
	
	#start pygame
	pygame.init()

	#store width and height vars
	display_height = 600
	display_width = 600

	#active tic tac toe area will have 700 x 700

	#display game window
	gameDisplay = pygame.display.set_mode((display_width,display_height))
	#name display window
	pygame.display.set_caption("Tic-Tac-Toe")


#draw tic tac toe board
def tic_tac_board():
	tic_tac_counter = 0
	tic_tac_list = []
	board_points = [(225,75),(225,525),(375,75),(375,525),(75,225),(525,225),(75,375),(525,375)]
	for coordinate in board_points:
		tic_tac_list.append(coordinate)

#main game loop
def main_loop():
	
	#set local variables

	#game is not crashed
	crashed = False
	#setup the clock
	clock = pygame.time.Clock()


	#until crashed
	while not crashed:

		#log all events
		for event in pygame.event.get():

			#quit sequence
			if event.type == pygame.QUIT:
				crashed = True


			#display updates
			pygame.display.update()

			#set fps
			clock.tick(60)


def crash_handling():
	#quit game
	pygame.quit()
	quit()

pygame_setup()
main_loop()
crash_handling()