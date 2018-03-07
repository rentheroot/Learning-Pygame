#learning to use pygame
#following this tutorial: https://pythonprogramming.net/displaying-images-pygame/?completed=/pygame-python-3-part-1-intro/

#imports
import pygame
import time
import random

#start pygame
pygame.init()

#store width and height vars
display_width = 800
display_height = 600

#define rgb colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
block_color = (53,115,255)

#tell program where right side of car is
car_width = 73

#init display
gameDisplay = pygame.display.set_mode((display_width,display_height))
#name window
pygame.display.set_caption('A bit Racey')
#set the game's clock
clock = pygame.time.Clock()

#load the car image
carImg = pygame.image.load('racecar.png')





#display text showing how many objects have been avoided
def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: " + str(count),True,black)
	gameDisplay.blit(text,(0,0))

#draw rectangle (x,y,w,h,color)
def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

#Place car on display
def car(x,y):
	gameDisplay.blit(carImg, (x,y))

#create fonts
def text_objects(text,font):
	textSurface = font.render(text, True, black)
	#get the rectangle to use as a reference
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

	#display message for 2 seconds
	time.sleep(2)
	

#make the crash function
def crash():
	message_display('You Crashed')
	game_loop()

#make main game loop
def game_loop():

	#define x and y for car
	x = (display_width * 0.45)
	y = (display_height * 0.8)

	#define x_change
	x_change = 0

	#have object start at random location on the x axis
	thing_startx = random.randrange(0,display_width)
	#make object start off screen at y -600
	thing_starty = -600
	#move 7 pixels at a time
	thing_speed = 7

	#block's width and height
	thing_width = 100
	thing_height = 100

	thing_count = 1

	#Number dodged
	dodged = 0

	#game not exited
	gameExit = False


	#run until game exits
	while not gameExit:


		#log game events
		for event in pygame.event.get():

			#if user exits window
			if event.type == pygame.QUIT:
				#quit game
				pygame.quit()
				quit()
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

		#put block into postition, start moving
		things(thing_startx, thing_starty, thing_width, thing_height, block_color)
		thing_starty += thing_speed
		#put car in postition
		car(x,y)

		things_dodged(dodged)



		#check if car has hit edge of window
		if x > display_width - car_width or x <0:
			crash()

		#create block when other block runs off screen
		#if y of block is larger than the display's height
		if thing_starty > display_height:
			#make new block appear off screen
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,int(display_width - thing_width))

			#count up number dodged
			dodged += 1
			#speed up the block
			thing_speed +=1
			#make block wider
			thing_width += (dodged * 1.2)
		#check if car runs into block (y and x crossover one another)
		if y < thing_starty + thing_height:
			print('y crossover')

			if x > thing_startx and x < thing_startx +thing_width or x+car_width > thing_startx and x + car_width < thing_startx + thing_width:
				print('x crossover')
				crash()


		#update display
		pygame.display.update()

		#run at 60 fps
		clock.tick(60)

#run main game loop
game_loop()
#quit game
pygame.quit()
quit()
