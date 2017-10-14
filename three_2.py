#!bin/usr/python

import pygame
from pygame.locals import *
from sys import exit

background_file = 'images/background.jpg'

screen_size = (640, 480)

pygame.init()
screen = pygame.display.set_mode(screen_size, RESIZABLE, 32)
background = pygame.image.load(background_file)

while True:
	event = pygame.event.wait()
	if event.type == QUIT:
		exit()
	if event.type == VIDEORESIZE:
		screen_size = event.size
		screen = pygame.display.set_mode(screen_size, RESIZABLE, 32)
		pygame.display.set_caption("Window resized to"+str(event.size))
	screen_width, screen_high = screen_size

	#此处需要重新填满窗口
	for y in range(0, screen_high, background.get_height()):
		for x in range(0, screen_width, background.get_width()):
			screen.blit(background, (x, y))

	pygame.display.update()