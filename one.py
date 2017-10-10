#!usr/bin/python

backgrouund_file = 'images/background.jpg'
mouse_file = 'images/mouse.png'

import pygame
from pygame.locals import *
from sys import exit

#初始化pygame，为使用硬件做准备
pygame.init()

#创建一个窗口
screen = pygame.display.set_mode((640,480), 0, 32)

#创建窗口标题
pygame.display.set_caption('Hello, world!')

#加载图片
background = pygame.image.load(backgrouund_file)
mouse_cursor = pygame.image.load(mouse_file)

#游戏主循环
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	screen.blit(background, (0,0))

	#获得鼠标位置
	x, y = pygame.mouse.get_pos()

	#计算光标左上角的位置
	x -= mouse_cursor.get_width() / 2
	y -= mouse_cursor.get_height() / 2

	screen.blit(mouse_cursor, (x, y))

	#刷新画面
	pygame.display.update()
