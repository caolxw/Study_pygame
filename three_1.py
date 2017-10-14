#!bin/usr/python

import pygame
from pygame.locals import *
from sys import exit

background_file = 'images/background.jpg'

screen = pygame.display.set_mode((640, 480), 0, 32);
background = pygame.image.load(background_file);

FullScreen = False

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN:
			if event.key == K_f:
				FullScreen = True
			if event.key == K_q:
				FullScreen = False
			if FullScreen:
				screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
			else :
				screen = pygame.display.set_mode((640, 480), 0, 32)
	screen.blit(background, (0, 0))
	pygame.display.update()