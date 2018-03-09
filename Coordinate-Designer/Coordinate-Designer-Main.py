#imports
import pygame

#setup main variables
display_height = int(input("what is the width"))
display_width = int(input("what is the height"))
display_increment = int(input("increment of pixels"))

#make rgb colors
white = (255,255,255)
black = (0,0,0)

#set up pygame
def pygame_setup(display_width,display_height,white):

	#start pygame
	pygame.init()

	#display game window
	gameDisplay = pygame.display.set_mode((display_width,display_height))
	#name display window
	pygame.display.set_caption("Coordinate Designer")
	#fill game display
	gameDisplay.fill(white)

#draw coordinate grid
def coordinate_grid(display_width,display_increment,display_height,black):

	#make sure number is divisible
	without_remainder_width = (display_width % display_increment)
	without_remainder_width = (display_width - without_remainder_width)
	print(without_remainder_width)

	without_remainder_height = (display_height % display_increment)
	without_remainder_height = (display_height - without_remainder_height)
	print(without_remainder_height)

	#determine number of lines to draw
	number_of_lines_width = (without_remainder_width/display_increment)
	numner_of_lines_height = (without_remainder_height/display_increment)

	#draw necessary number of lines
	for i in range(0, number_of_lines_width):
		




#main game loop
def main_loop(display_width,display_increment,display_height, black):
	
	#set local variables

	#game is not crashed
	crashed = False
	#setup the clock
	clock = pygame.time.Clock()


	#set up coordinate grid
	coordinate_grid(display_width,display_increment,display_height, black)
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
pygame_setup(display_width,display_height,white)
main_loop(display_width,display_increment,display_height, black)
crash_handling()