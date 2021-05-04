import pygame

class Invaders(object):
    def __init__(self):
        self._width  = 35
        self._height = 35
        self._positions = []
        self._moveCounter = 0
        self._direction = (1, 0)

        self._makeInvaders()

    def _makeInvaders(self):
        self._positions.append([50, 50])

    def draw(self, wn):
        for position in self._positions: 
            pygame.draw.rect(wn, (255, 0, 0), (*position, self._width, self._height))


    def move(self, dt):
        self._moveCounter += dt
        if self._moveCounter > 1.5:
            self._moveCounter = 0
            for idx, position in enumerate(self._positions):
                self._positions[idx][0] += 20
                 
                

    

    