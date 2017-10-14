#!usr/bin/python

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640,480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

#设置字体
font = pygame.font.SysFont('arial', 16)
font_height = font.get_linesize()
event_text = []

while True:
	#等待一个事件发生才继续下去
	event = pygame.event.wait()
	event_text.append(str(event))
	

	if event.type == QUIT:
		exit()

	screen.fill((255, 255, 255))

	y = SCREEN_SIZE[1] - font_height

	for text in reversed(event_text):
		screen.blit(font.render(text, True, (0, 0, 0)),(0, y))
		y -= font_height
	pygame.display.update()
