import pygame


class Wall(object):
    def __init__(self, startPos: tuple, width: int, height: int):
        self._startPos = startPos
        self._width = width
        self._height = height
        self._sql = 10
        self._blocks = set()

        self._makeBlocks()

    def _makeBlocks(self):
        for column in range(self._height):
            for row in range(self._width):
                self._blocks.add((
                    self._startPos[0] + row*self._sql, 
                    self._startPos[1] + column*self._sql
                ))

    def bulletCollision(self, bullets):
        for idx, bullet in enumerate(bullets):
            temp = (bullet.x//self._sql*self._sql, bullet.y//self._sql*self._sql)
            if temp in self._blocks:
                self._blocks.remove(temp)
                bullets.popBullet(idx)
    
    def draw(self, wn):
        for block in self._blocks:
            pygame.draw.rect(wn, (0, 255, 0), (*block, self._sql, self._sql))




