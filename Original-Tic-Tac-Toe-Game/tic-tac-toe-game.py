#tic tac toe game

#imports
import pygame

#set up pygame
def pygame_setup():
	
	#start pygame
	pygame.init()

	#store width and height vars
	display_height = 800
	display_width = 800

	#active tic tac toe area will have 700 x 700

	#display game window
	gameDisplay = pygame.display.set_mode((display_width,display_height))
	#name display window
	pygame.display.set_caption("Tic-Tac-Toe")


#draw tic tac toe board
def tic_tac_board():
	pass
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