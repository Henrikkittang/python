from game_lib.animation.counter import Counter
from game_lib.collision.aabb import aabb
from game_lib.util.math import distance
import random
import pygame

class Invaders(object):
    def __init__(self):
        self._width       : int    = 35
        self._height      : int    = 35
        self._positions   : list   = []
        self._moveCounter : object = Counter()
        self._shootCounter: object = Counter()
        self._speed       : int    = 20

        self._makeInvaders()

    def _makeInvaders(self) -> None:
        for column in range(5):
            for row in range(11):
                c = 20  + column * self._height + column * 10
                r = 300 + row    * self._width  + row    * 10
                self._positions.append( [r, c] )

    def _checkBounds(self, screenDimensions: tuple) -> None:
        for pos in self._positions:
            if ((pos[0] + self._width+abs(self._speed) >= screenDimensions[0] and self._speed > 0) or 
                (pos[0]-abs(self._speed) <= 0 and self._speed) < 0):
                return True
        return False

    def draw(self, wn: object) -> None:
        for position in self._positions: 
            pygame.draw.rect(wn, (255, 0, 0), (*position, self._width, self._height))

    def move(self, dt: float, screenDimensions: tuple) -> None:
        if self._moveCounter(dt, 1):

            if self._checkBounds(screenDimensions):
                self._speed *= -1
                for idx, position in enumerate(self._positions):
                    self._positions[idx][1] += 20
            else:
                for idx, position in enumerate(self._positions):
                    self._positions[idx][0] += self._speed


    def bulletCollision(self, bullets: object) -> None:
        for idx2, position in enumerate(self._positions):
            for idx1, bullet in enumerate(bullets):
                if aabb(bullet.getRect(), (*position, self._width, self._height)):
                    bullets.popBullet(idx1)
                    self._positions.pop(idx2)

    def shoot(self, bullets: object, dt: float):
        if self._shootCounter(dt, 0.5):
            idx = random.randint(0, len(self._positions)-1)
            curInvader = self._positions[idx]
            for invader in self._positions:
                if invader[0] == curInvader[0] and invader[1] > curInvader[1]:
                    curInvader = invader

            bullets.addBullet(curInvader[0] + self._width//2, curInvader[1]+self._height+1, (0, 1))

                

    

    