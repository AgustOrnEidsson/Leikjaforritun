#Höfundur Ágúst Örn Eiðsson
#10.1.18

import pygame
from random import *
import _thread

pygame.init()

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)
mutex = _thread.allocate_lock()

pygame.display.set_caption('Pong')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

kottur=randint(1,2)

x_velocity = 0
y_velocity = 0

stig1=0
stig2=0

teljari=0
teljari1=0

pong="PRESS SPACEBAR"

font = pygame.font.SysFont("comicsansms", 72)

window.fill(BLACK)
x_position = 320
y_position = 0

y_position1 = 90
y_velocity1 = 0

y_position2 = 90
y_velocity2 = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if stig1-stig2<5 or stig2-stig1<5:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                y_velocity1 = -0.5
                running = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                y_velocity1 = 0.5
                running = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                y_velocity2=-0.5
                running = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                y_velocity2 = 0.5
                running = True

        if stig1-stig2>5:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                y_velocity1 = -0.5
                running = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                y_velocity1 = 0.5
                running = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                y_velocity2=-0.7
                running = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                y_velocity2 = 0.7
                running = True

        if stig2-stig1>5:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                y_velocity1 = -0.7
                running = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                y_velocity1 = 0.7
                running = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                y_velocity2=-0.5
                running = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                y_velocity2 = 0.5
                running = True

        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            y_velocity1 = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_s:
            y_velocity1 = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            y_velocity2 = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            y_velocity2 = 0
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and x_velocity==0 and y_velocity==0:
            pong=""
            if kottur == 1:
                x_velocity = 0.3
                y_velocity = 0.1
            elif kottur == 2:
                x_velocity = -0.3
                y_velocity = -0.1

    if y_position > 460 or y_position < 0:
        y_velocity *= -1

    if x_position > 620:
        x_position = 320
        y_position = 0
        x_velocity = 0
        y_velocity = 0
        stig1+=1
        kottur=2
        teljari=0
        pong = "PRESS SPACEBAR"

    if x_position < 0:
        x_position = 320
        kottur=1
        teljari=0
        pong="PRESS SPACEBAR"
        y_position = 0
        x_velocity=0
        y_velocity=0
        stig2+=1

    if 398<y_position1:
        y_position1=398

    if 398<y_position2:
        y_position2=398

    if y_position2<0:
        y_position2=0

    if y_position1<0:
        y_position1=0

    if 40<x_position<60 and y_position1-10<y_position<y_position1+80:
        x_velocity *=-1
        teljari+=1

    if 560<x_position<580 and y_position2-10<y_position<y_position2+80:
        x_velocity *=-1
        teljari+=1

    if teljari1+10==teljari:
        teljari1=teljari
        x_velocity*=2
        y_velocity*=2

    player1=pygame.draw.rect(window, RED, pygame.Rect(40, y_position1, 20, 80))
    player2=pygame.draw.rect(window, RED, pygame.Rect(580, y_position2, 20, 80))
    bolti=pygame.draw.rect(window, BLUE, pygame.Rect(x_position, y_position, 20, 20))
    textinn = font.render(str(stig1) + " | " + str(stig2), True, (255, 255, 255))
    text = font.render(pong, True, (0, 128, 0))

    window.blit(text,
                (320 - text.get_width() // 2, 240 - text.get_height() // 2))

    window.blit(textinn,
                (320 - textinn.get_width() // 2, 30 - textinn.get_height() // 2))

    pygame.display.update()
    window.fill(BLACK)

    x_position += x_velocity
    y_position += y_velocity

    y_position1 += y_velocity1
    y_position2 += y_velocity2

pygame.quit()
