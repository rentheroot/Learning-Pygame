#tic tac toe game

#imports
import pygame

#make rgb colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

#set up pygame


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
	
#draw an x
def draw_x():
	pygame.draw.line(gameDisplay, white, (260, 100), (340, 200), 10)
	pygame.draw.line(gameDisplay, white, (260, 200) , (340, 100), 10)
	
#button
def button(x,y,w,h,ic,action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	print(click)

	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(gameDisplay,ic,(x,y,w,h),1)

		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(gameDisplay, ic, (x,y,w,h),1)


#main game loop
def main_loop():
	
	#set local variables

	#game is not crashed
	crashed = False
	#setup the clock
	clock = pygame.time.Clock()

	#draw tic tac toe board
	#until crashed
	while not crashed:
		tic_tac_counter = 0
		tic_tac_list = []
		board_points = [(225,75),(225,525),(375,75),(375,525),(75,225),(525,225),(75,375),(525,375)]
		corner_points = [(75, 75),(225, 75),(225, 225),(375, 225),(225, 375),(375, 375),(75, 225),(75, 375),(375, 75)]
		

		#draw game board lines
		for coordinate in board_points:
			tic_tac_list.append(coordinate)

			if len(tic_tac_list) % 2 == 0:
				pygame.draw.line(gameDisplay,white,tic_tac_list[0], tic_tac_list[1],10)
				tic_tac_list = []
		
		#draw squares

		for coordinate in corner_points:

			#pygame.draw.rect(gameDisplay,red,((coordinate[0] + 6),coordinate[1]+6,140,140))
			button((coordinate[0] + 6),(coordinate[1]+6),140,140,red,draw_x)


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

#tic_tac_board(gameDisplay)
main_loop()
crash_handling()