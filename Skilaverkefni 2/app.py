# Ágúst Örn Eiðsson
# 7.3.18

import os
import random
import pygame



# Class for the orange dude
class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(16, 16, 16, 16)
        global antibombs
        self.antibombs = 0
        self.defuse = 0

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def draw(self):
        if self.antibombs >= 1:
            man = pygame.draw.rect(screen, (255, 200, 0), player.rect)
        else:
            man = pygame.draw.rect(screen, (255, 128, 0), player.rect)
        return man

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy


        # If you collide with a veggur, move out based on velocity
        for veggur in veggurs:
            if self.rect.colliderect(veggur.rect):
                if dx > 0:  # Moving right; Hit the left side of the veggur
                    self.rect.right = veggur.rect.left
                if dx < 0:  # Moving left; Hit the right side of the veggur
                    self.rect.left = veggur.rect.right
                if dy > 0:  # Moving down; Hit the top side of the veggur
                    self.rect.bottom = veggur.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the veggur
                    self.rect.top = veggur.rect.bottom

        for bomb in bombs:
            if self.rect.colliderect(bomb.rect):
                if self.antibombs >= 1:
                    if dx > 0:  # Moving right; Hit the left side of the veggur
                        self.rect.right = bomb.rect.left
                        bombs.remove(bomb)
                        self.defuse -= 1
                        self.antibombs -= 1
                    if dx < 0:  # Moving left; Hit the right side of the veggur
                        self.rect.left = bomb.rect.right
                        bombs.remove(bomb)
                        self.defuse += 1
                        self.antibombs -= 1
                    if dy > 0:  # Moving down; Hit the top side of the veggur
                        self.rect.bottom = bomb.rect.top
                        bombs.remove(bomb)
                        self.defuse += 1
                        self.antibombs -= 1
                    if dy < 0:  # Moving up; Hit the bottom side of the veggur
                        self.rect.top = bomb.rect.bottom
                        bombs.remove(bomb)
                        self.defuse += 1
                        self.antibombs -= 1
                else:
                    raise SystemExit("You hit something")
                if dx > 0:  # Moving right; Hit the left side of the veggur
                    self.rect.right = bomb.rect.left
                if dx < 0:  # Moving left; Hit the right side of the veggur
                    self.rect.left = bomb.rect.right
                if dy > 0:  # Moving down; Hit the top side of the veggur
                    self.rect.bottom = bomb.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the veggur
                    self.rect.top = bomb.rect.bottom
        for antibomb in antibombs:
            if self.rect.colliderect(antibomb.rect):
                if dx > 0:  # Moving right; Hit the left side of the veggur
                    self.antibombs+=1
                    antibombs.remove(antibomb)
                if dx < 0:  # Moving left; Hit the right side of the veggur
                    self.antibombs+=1
                    antibombs.remove(antibomb)
                if dy > 0:  # Moving down; Hit the top side of the veggur
                    self.antibombs+=1
                    antibombs.remove(antibomb)
                if dy < 0:  # Moving up; Hit the bottom side of the veggur
                    self.antibombs+=1
                    antibombs.remove(antibomb)



# Nice class to hold a veggur rect
class veggur(object):

    def __init__(self, pos):
        veggurs.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class Bomb(object):

    def __init__(self,pos):
        bombs.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class AntiBomb(object):

    def __init__(self, pos):
        antibombs.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class gate(object):

    def __init__(self, pos):
        gates.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)




# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "300"
pygame.init()

# Set up the display
pygame.display.set_caption("Bomb Squad")
screen = pygame.display.set_mode((960, 720))

clock = pygame.time.Clock()
veggurs = []  # List to hold the veggurs
bombs = []  # List to hold the bombs
antibombs = []
gates=[]
player = Player()  # Create the player

# Holds the level layout in a list of strings.
level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                             W B          W",
    "W WWW W W WWWWWWWWWWW WWWWWWWWWWWWWWWWWWWWWWW WW WWWWWWWWW W",
    "W     W W           W W                          W         W",
    "WWWWWWW WWWWWW WWWWWW W WWWWWWWWWWWWWWWWWWWWWWWWWW WWWWW WWW",
    "W W       W           W W                        W   W   W W",
    "W WWWWWWWWW WWWWWW WWWW W WWWWWWWWWWWWWWWWWWWWWWWWWWWW W W W",
    "W W       W W    W W  W   W        W        W   W   W  W   W",
    "W W WWWWWWW W WW W W WWWWWW WWWWWWWW WWWWWW W W W W W WWWW W",
    "W W         W WW W W W      W        W        W   W W    W W",
    "W WWW WWWWWWW W  W W W WWW  W WWWW WWW WWWWWWWWWWWW WWWW W W",
    "W W   W       WWWW W W W WWWW WW   W    W W   W   W    W W W",
    "W W WWW WWWWWWW    W W W       W WWW WWWW W W W W W WWWW W W",
    "W W W   W       WWWW W W WWWWW W W   W      W W W   W    W W",
    "W A   WWW WWWWWWW      W     W W WWWWWWWWWWWW W WWWWW WWWW W",
    "W W W  W  W       WWWWWWWWWW W W              W     W    W W",
    "W W WW W WW WWWWWWW          W W WWWWWWWWWWWWWWWWWWWWWWW WWW",
    "W        WW W     W WWWWWWWWWW W W   W   W   W   W   W   W W",
    "W WWWWW WW  W WWWWW W          W   W   W   W   W   W   W   W",
    "W W     WW WW W   W W WWWW WWWWWWWWWWWWWWWAWWWWWWWWWWWWWWWWW",
    "W W WWWWW  W  W W W W W  W W             W W               W",
    "W W W     WW WW WWWWW WW W WWWWWWWWWWWWW W W WWWWWWWWWWWW  W",
    "W   W WWWWW  W           W               W   W          W  W",
    "W W W WW     W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W  W",
    "W W      WWW W                              W         W W  W",
    "W WWWWWWWW W WWWWWWWW                       W WWWWWWWWW W  W",
    "W W          W                              W W       W W  W",
    "W     WWWWWWWW                              W W WWWWW W W  W",
    "W W      WW                                     W      W W W",
    "W   W                        W               WWW       A   W",
    "W W W                         W      B       WWWWWWWWWWWWWWW",
    "W W W                        W                             W",
    "W W W                        W                             W",
    "W W W                       W                              W",
    "W W W                      WWWWWWWWW                       W",
    "W W W                                                      W",
    "W W WWWWW               B                                  W",
    "W W     W                                                  W",
    "W WWWWW WWWWWWWWWWWWWWWWW                                  W",
    "W W     W   W   W   W   W                                  W",
    "W W W W B W W W W W W W A                                  W",
    "W W W W W     W   W   W W                                  W",
    "W WWW W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWGWWW",
    "W     W         W                                      W   W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEW",

]

# Parse the level string above. W = veggur, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            veggur((x, y))
        if col == "E":
            endakubbur = pygame.Rect(x, y, 16, 16)
        if col == "B":
            Bomb((x, y))
        if col == "A":
            AntiBomb((x, y))
        if col == "G":
            gate((x, y))
        x += 16
    y += 16
    x = 0

running = True
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(endakubbur):
        raise SystemExit("You Win!")

    # Draw the scene
    screen.fill((0, 0, 0))
    for veggur in veggurs:
        pygame.draw.rect(screen, (255, 255, 255), veggur.rect)
    for bomb in bombs:
        pygame.draw.rect(screen, (255,0,255), bomb.rect)
    for antibomb in antibombs:
        pygame.draw.rect(screen, (50,150,120), antibomb.rect)
    for gate in gates:
        pygame.draw.rect(screen, (50,205,50), gate.rect)

    pygame.draw.rect(screen, (0, 255, 255), endakubbur)
    counter = 0
    if counter %2 == 0:
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
        counter += 1
    else:
        pygame.draw.rect(screen, (255, 128, 0), player.rect)
        counter += 1
    pygame.display.flip()