#learning to use pygame
#following this tutorial: https://pythonprogramming.net/displaying-images-pygame/?completed=/pygame-python-3-part-1-intro/

#imports
import pygame

#start pygame
pygame.init()

#store width and height vars
display_width = 800
display_height = 600

#init display
gameDisplay = pygame.display.set_mode((display_width,display_height))

#name window
pygame.display.set_caption('A bit Racey')

#define rgb colors
black = (0,0,0)
white = (255,255,255)


#set the game's clock
clock = pygame.time.Clock()

#game not crashed
crashed = False

#load the car image
carImg = pygame.image.load('racecar.png')

#function to place car on display
#blit draws car to screen
def car(x,y):
	gameDisplay.blit(carImg, (x,y))

#define x and y for car
x = (display_width * 0.45)
y = (display_height * 0.8)

#define x_change
x_change = 0

#define car speed
car_speed = 0


#run until game crashes
while not crashed:


	#log game events
	for event in pygame.event.get():

		#if user exits window
		if event.type == pygame.QUIT:
			crashed = True
		#print out user actions
		print(event)

		#move the car
		#check for keydown event
		if event.type == pygame.KEYDOWN:
			#check if left arrow key
			if event.key == pygame.K_LEFT:
				#change x variable by -5
				x_change = -5
			#check if right arrow key
			elif event.key == pygame.K_RIGHT:
				#change x variable by 5
				x_change = 5
			#check if key is released
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				#make x variable 0
				x_change = 0
	#move car along x axis
	x += x_change

	#make everything currently in the game white
	gameDisplay.fill(white)

	#put car in postition
	car(x,y)

	#update display
	pygame.display.update()

	#run at 60 fps
	clock.tick(60)


#quit game
pygame.quit()
quit()
