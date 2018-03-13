#imports
import pygame
import math

#setup main variables
display_height = int(input("what is the width"))
display_width = int(input("what is the height"))
display_increment = int(input("increment of pixels"))

#make rgb colors
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)

#set up pygame


#start pygame
pygame.init()

#display game window
gameDisplay = pygame.display.set_mode((display_width,display_height))
#name display window
pygame.display.set_caption("Coordinate Designer")
#fill game display
gameDisplay.fill(white)

#use distance formula for coordinate grid
#coordinate_list = list of all coordinates on grid
#x_new = x coordinate clicked
#y_new = y coordinate clicked

def distance_formula(coordinate_list, x_new, y_new):
	best_x = 0
	best_y = 0
	for coordinate in coordinate_list:
		x2 = coordinate[0]
		y2 = coordinate[1]

		x1 = int(x_new)
		y1 = int(y_new)

		#(x2 -x1)^2
		#x2 - x1
		x3 = int(x2) - x1
		#squared
		x3 = x3 ** 2

		#(y2 -y1)^2
		#y2 - y1
		y3 = int(y2) - y1
		#squared
		y3 = y3 ** 2

		#((x2 -x1)^2) + ((y2 -y1)^2)
		full_num = x3 + y3

		#square root
		new_distance = math.sqrt(full_num)

		x2 = coordinate[0]
		y2 = coordinate[1]
		#compare
		try:
			if new_distance < best_distance:
				best_distance = new_distance
				best_x = x2
				best_y = y2
		except:
			best_distance = new_distance
			best_x = x2
			best_y = y2

	return(best_x,best_y)



#draw coordinate grid
def coordinate_grid(display_width,display_increment,display_height,black):

	#make sure number is divisible
	without_remainder_width = (display_width % display_increment)
	without_remainder_width = (display_width - without_remainder_width)


	without_remainder_height = (display_height % display_increment)
	without_remainder_height = (display_height - without_remainder_height)


	#determine number of lines to draw
	number_of_lines_width = (without_remainder_width/display_increment)
	number_of_lines_height = (without_remainder_height/display_increment)


	#set the width counter to 0
	width_counter = 0

	#draw necessary number of vertical lines
	for i in range(0, int(number_of_lines_width) + 1):
		pygame.draw.line(gameDisplay, black, (width_counter, 0),(width_counter,display_height))
		width_counter = width_counter + display_increment


	#set height counter to 0
	height_counter = 0

	#draw necessary number of horizontal lines
	for i in range(0, int(number_of_lines_height) + 1):
		pygame.draw.line(gameDisplay, black, (0, height_counter),(display_width,height_counter))
		height_counter = height_counter + display_increment

	#find intersection of lines
	x_nums = 0
	y_nums = 0

	#make coordinate lists
	x_list = []
	y_list = []

	
	for i in range(0,int(number_of_lines_height)):
		for i in range(0, int(number_of_lines_width)):
			pygame.draw.circle(gameDisplay,blue,(x_nums,y_nums),2)
			x_list.append(x_nums)
			y_list.append(y_nums)

			x_nums = x_nums + display_increment
		x_nums = 0
		y_nums = y_nums + display_increment


	#make list of coordinate tuples
	full_coordinates = list(zip(x_list, y_list))

	return(full_coordinates)


#main game loop
def main_loop(display_width,display_increment,display_height, black):
	
	#set counter
	counter = []
	#game is not crashed
	crashed = False
	#setup the clock
	clock = pygame.time.Clock()
	#store lines drawn
	lines_drawn = []


	#set up coordinate grid
	full_coordinates =coordinate_grid(display_width,display_increment,display_height,black)
	#until crashed
	while not crashed:

		#log all events
		for event in pygame.event.get():

			#quit sequence
			if event.type == pygame.QUIT:
				crashed = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				#check if color clicked is blue
				clickBlue = gameDisplay.get_at(pygame.mouse.get_pos()) == blue
				clickRed = gameDisplay.get_at(pygame.mouse.get_pos()) == red
				#if blue
				if clickBlue == 1:
					xx , yy = pygame.mouse.get_pos()
					pygame.draw.circle(gameDisplay, red, (distance_formula(full_coordinates, xx, yy)),2)
					counter.append(distance_formula(full_coordinates, xx, yy))

					if (len(counter) % 2) == 0:
						print(counter[0], ',', counter[1] )
						pygame.draw.line(gameDisplay,red,(counter[0]), (counter[1]),2)
						lines_drawn.append(counter[0])
						lines_drawn.append(counter[1])
						counter = []

				if clickRed == 1:
					xx , yy = pygame.mouse.get_pos()
					pygame.draw.circle(gameDisplay, red, (distance_formula(full_coordinates, xx, yy)),2)
					counter.append(distance_formula(full_coordinates, xx, yy))

					if (len(counter) % 2) == 1 and len(counter) != 1:
						print(counter[0], ',', counter[1] )
						
						pygame.draw.line(gameDisplay,red,(counter[0]), (counter[1]),2)
						lines_drawn.append(counter[0])
						lines_drawn.append(counter[1])
						counter = []


			if event.type == pygame.KEYDOWN:
				#check if r key pressed
				if event.key == pygame.K_r:

					#ask input
					display_increment2 = int(input("increment of pixels"))

					#redraw the board with different grid size
					gameDisplay.fill(white)

					#redraw lines
					new_lines = []

					for coordinate in lines_drawn:

						new_lines.append(coordinate)

						if len(new_lines) % 2 == 0:
							pygame.draw.line(gameDisplay,red,new_lines[0], new_lines[1],2)
							new_lines = []


					#redraw coordinate grid
					full_coordinates =coordinate_grid(display_width,display_increment2,display_height,black)
					display_increment = display_increment2

			if event.type == pygame.KEYDOWN:
				#check if d key pressed
				if event.key == pygame.K_d:
					#delete last line made
					lines_drawn = lines_drawn[:-2]

					#redraw the board with different grid size
					gameDisplay.fill(white)

					#redraw lines
					new_lines = []

					for coordinate in lines_drawn:

						new_lines.append(coordinate)

						if len(new_lines) % 2 == 0:
							pygame.draw.line(gameDisplay,red,new_lines[0], new_lines[1],2)
							new_lines = []
					#redraw coordinate grid
					full_coordinates =coordinate_grid(display_width,display_increment,display_height,black)

			#display updates
			pygame.display.update()

			#set fps
			clock.tick(64)


def crash_handling():
	#quit game
	pygame.quit()


#run functions
main_loop(display_width,display_increment,display_height, black)
crash_handling()