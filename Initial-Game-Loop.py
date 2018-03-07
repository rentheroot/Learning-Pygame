#learning to use pygame
#following this tutorial: https://pythonprogramming.net/pygame-python-3-part-1-intro/

#imports
import pygame

#initialize pygame so I can use it, necessary for every program using pygame
pygame.init()

#make the display/canvas that pygame will draw on
#makes the display 800px wide and 60 px tall
gameDisplay = pygame.display.set_mode((800,600))

#name the window
#names the window "A bit Racey"
pygame.display.set_caption('A bit Racey')

#set the game's clock
#the clock tracks time in the game, mostly used for FPS
#generally isn't good form to use fps to speed up a game; wasted processing power
clock = pygame.time.Clock()

#tell the computer that the game has not crashed
crashed = False

#main game loop
#run until game crashes (user exits out of window)
while not crashed:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#tell pygame the game has crashed
			crashed = True

		#print out everything done by user in pygame
		print(event)

	pygame.display.update()
	clock.tick(60)