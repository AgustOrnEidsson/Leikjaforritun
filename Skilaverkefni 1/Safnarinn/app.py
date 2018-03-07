#Höfundur Ágúst Örn Eiðsson
#10.1.18

import pygame
from random import *
import _thread
import time

pygame.init()

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)
mutex = _thread.allocate_lock()
shrek=pygame.image.load("sherkkyrr.png")

pygame.display.set_caption('Safnarinn')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pong="PRESS SPACEBAR"

font = pygame.font.SysFont("comicsansms", 72)

window.fill(BLACK)

x_position = 320
y_position = -150

y_velocity=0

size=80
lif=10

x_position1 = 280
x_velocity1 = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x_velocity1 = -0.4
            shrek=pygame.image.load("shrekhaegri.png")
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x_velocity1 = 0.4
            shrek=pygame.image.load("shrekvinstri.png")

        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            x_velocity1=0
            shrek=pygame.image.load("sherkkyrr.png")
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            x_velocity1=0
            shrek=pygame.image.load("sherkkyrr.png")
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            y_velocity=0.2
            shrek=pygame.image.load("sherkkyrr.png")
            pong=""

        if 398 < y_position:
            lif-=1
            print(lif)

        if lif<=0:
            pong="You Lose"
            text = font.render(pong, True, (255, 255, 255))
            window.blit(text,
                        (320 - text.get_width() // 2, 240 - text.get_height() // 2))

        lifin="* "+str(lif)

    player1=pygame.draw.rect(window, WHITE, pygame.Rect(x_position1, 350, size, 20))
    bolti=pygame.draw.rect(window, RED, pygame.Rect(x_position, y_position, 20, 20))
    text = font.render(pong, True, (255, 255, 255))
    lifid = font.render(lifin, True, (255, 255, 255))
    window.blit(shrek,(x_position1-7, 370))

    window.blit(text,
                (320 - text.get_width() // 2, 240 - text.get_height() // 2))

    window.blit(lifid,
                (500, 25))

    pygame.display.update()
    window.fill(BLACK)

    y_position += y_velocity

    x_position1 += x_velocity1
    if pong=="You Lose":
        time.sleep(7)
        running = False

pygame.quit()