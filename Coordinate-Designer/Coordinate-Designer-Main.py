#imports
import pygame

#setup main variables
display_height = int(input("what is the width"))
display_width = int(input("what is the height"))

#set up pygame
def pygame_setup(display_width,display_height):

	#start pygame
	pygame.init()

	#display game window
	gameDisplay = pygame.display.set_mode((display_width,display_height))
	#name display window
	pygame.display.set_caption("Coordinate Designer")
	#fill game display
	gameDisplay.fill(white)

#draw coordinate grid
def coordinate_grid():


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


#run functions
pygame_setup(display_width,display_height)
main_loop()
crash_handling()