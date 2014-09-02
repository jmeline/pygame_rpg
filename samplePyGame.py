## Import and Init
import pygame
from pygame.locals import K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT
pygame.init()

'''
while not done:
    #Handle a Close Event
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT or keys[K_ESCAPE]:
            done = True

    ## Set framerate to 60
    framerate.tick(60)

    #Keyborad Keypress Events, Movement
    if pygame.key.get_pressed()[K_UP]:
      ly = ly - speed
    if pygame.key.get_pressed()[K_DOWN]:
      ly = ly + speed
    if pygame.key.get_pressed()[K_LEFT]:
      lx = lx - speed
    if pygame.key.get_pressed()[K_RIGHT]:
      lx = lx + speed

    #Test for Out-of-Bounds
    if lx > rightBound:
      lx = rightBound
    if lx < 0:
      lx = 0
    if ly > bottomBound:
      ly = bottomBound
    if ly < 0:
      ly = 0

    ## draw background
    screen.blit(background, (0, 0))

    ## draw image
    screen.blit(sotcLogo, (lx, ly))
    pygame.display.flip()
    #pygame.display.update()
'''

class Game(object):
    """Handles the game itself"""
    def __init__(self):
        #Load and Convert the SOTC Logo
        self.image = pygame.image.load("cloud.png")
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        self.fps = 60.0
        self.done = False
        self.lx = 100
        self.ly = 100
        self.speed = 3
        self.rightBound = self.screen.get_width() - self.image.get_width()
        self.bottomBound = self.screen.get_height() - self.image.get_height()
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((20, 130, 157))

    def eventLoop(self):
        """Add/pop directions from player's direction stack as necessary."""
        for event in pygame.event.get():
            self.keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                pass
                ##self.player.add_direction(event.key)
            elif event.type == pygame.KEYUP:
                pass
                ##self.player.pop_direction(event.key)      

    def mainLoop(self):
        """Our main game loop; I bet you'd never have guessed."""
        delta = self.clock.tick(self.fps)/1000.0
        while not self.done:
            self.eventLoop()
            ## draw background
            self.screen.blit(self.background, (0, 0))

            ## draw image
            self.screen.blit(self.image, (self.lx, self.ly))

            ## Set framerate to 60
            self.clock.tick(60)

            #Keyborad Keypress Events, Movement
            if pygame.key.get_pressed()[K_UP]:
              self.ly = self.ly - self.speed
            if pygame.key.get_pressed()[K_DOWN]:
              self.ly = self.ly + self.speed
            if pygame.key.get_pressed()[K_LEFT]:
              self.lx = self.lx - self.speed
            if pygame.key.get_pressed()[K_RIGHT]:
              self.lx = self.lx + self.speed

            #Test for Out-of-Bounds
            if self.lx > self.rightBound:
              self.lx = self.rightBound
            if self.lx < 0:
              self.lx = 0
            if self.ly > self.bottomBound:
              self.ly = self.bottomBound
            if self.ly < 0:
              self.ly = 0
            #self.player.update(self.obstacles, delta)
            #self.draw()
            pygame.display.flip()
            #pygame.display.update()
            #delta = self.clock.tick(self.fps)/1000.0
            #self.display_fps()

def main():
    ## Set Up the window
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Sprite Test!")
    #Set Blue Background
    #Logo Position Varibales
    #Right and Bottom Bounds for Game Entities
    Game().mainLoop()

if __name__ == '__main__':
    main()