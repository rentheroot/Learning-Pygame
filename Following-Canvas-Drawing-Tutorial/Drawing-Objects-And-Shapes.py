#following this tutorial: https://pythonprogramming.net/pygame-drawing-shapes-objects/?completed=/adding-score-pygame-video-game/

#imports
import pygame

#initialize pygame
pygame.init()

#make rgb colors
white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#set up display
gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)

#change a single pixel array (located at 10,20) to the color green
pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green

#draw a blue line on game display starting at (100,200) and ending at (300,450) with a width of 5
pygame.draw.line(gameDisplay, blue, (100,200), (300,450), 5)

#draw a red filled in rectangle with the corner coordinates:
#400 (top right x)
#400 (top right y)
#50 (width)
#25 (height)
pygame.draw.rect(gameDisplay,red,(400,400,50,25))

#draw white circle with top right coordinates (150,150) and center point at 75
pygame.draw.circle(gameDisplay,white,(150,150),75)

#draw green polygon with specified points
pygame.draw.polygon(gameDisplay,green, ((25,75),(76,125),(250,375),(400,25),(60,540)))

#main loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	pygame.display.update()