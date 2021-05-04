from game_lib.animation.counter import Counter
import pygame



class Invaders(object):
    def __init__(self):
        self._width      : int    = 35
        self._height     : int    = 35
        self._positions  : list   = []
        self._moveCounter: object = Counter()
        self._speed      : int    = 20

        self._makeInvaders()

    def _makeInvaders(self):
        for column in range(5):
            for row in range(11):
                c = 20 + column * self._height + column * 10
                r = 300 + row * self._width + row * 10
                self._positions.append( [r, c] )
                
    def draw(self, wn):
        for position in self._positions: 
            pygame.draw.rect(wn, (255, 0, 0), (*position, self._width, self._height))

    def _checkBouns(self, screenDimensions):
        for pos in self._positions:
            if ((pos[0] + self._width+abs(self._speed) >= screenDimensions[0] and self._speed > 0) or 
                (pos[0]-abs(self._speed) <= 0 and self._speed) < 0):
                return True
        return False

    def move(self, dt, screenDimensions):
        if self._moveCounter(dt, 1):

            if self._checkBouns(screenDimensions):
                self._speed *= -1
                for idx, position in enumerate(self._positions):
                    self._positions[idx][1] += 20
            else:
                for idx, position in enumerate(self._positions):
                    self._positions[idx][0] += self._speed
                 
                

    

    