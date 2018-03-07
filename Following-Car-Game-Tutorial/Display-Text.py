#learning to use pygame
#following this tutorial: https://pythonprogramming.net/displaying-images-pygame/?completed=/pygame-python-3-part-1-intro/

#imports
import pygame
import time

#start pygame
pygame.init()

#store width and height vars
display_width = 800
display_height = 600

#init display
gameDisplay = pygame.display.set_mode((display_width,display_height))
#name window
pygame.display.set_caption('A bit Racey')
#set the game's clock
clock = pygame.time.Clock()

#load the car image
carImg = pygame.image.load('racecar.png')

#define rgb colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#tell program where right side of car is
car_width = 73


#function to place car on display
#blit draws car to screen
def car(x,y):
	gameDisplay.blit(carImg, (x,y))

#create fonts
def text_objects(text,font):
	textSurface = font.render(text, True, black)
	return textSurface , textSurface.get_rect()

#display the text
def message_display(text):

	#define the large text
	largeText = pygame.font.Font('freesansbold.ttf',115)
	#define text and rectangle to encompass large text
	TextSurf, TextRect = text_objects(text, largeText)
	#center the text
	TextRect.center = ((display_width/2),(display_height/2))
	#draws in text
	gameDisplay.blit(TextSurf, TextRect)

	#update display
	pygame.display.update()

	time.sleep(2)

	game_loop()

#make main game loop
def game_loop():

	#define x and y for car
	x = (display_width * 0.45)
	y = (display_height * 0.8)

	#define x_change
	x_change = 0

	#game not exited
	gameExit = False

	#run until game exits
	while not gameExit:


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

		#check if car has hit edge of window
		if x > display_width - car_width or x <0:
			gameExit = True

		#update display
		pygame.display.update()

		#run at 60 fps
		clock.tick(60)

#run main game loop
game_loop()
#quit game
pygame.quit()
quit()
