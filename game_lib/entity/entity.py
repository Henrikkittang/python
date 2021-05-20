import pygame

class Entity(object):
    def __init__(self, x: float, y: float, width:float, height:float, speed:int, color: tuple=(255, 255, 255)):
        self.x         :float = x 
        self.y         :float = y
        self._width    :int   = width
        self._height   :int   = height
        self._speed    :int   = speed
        self._color    :tuple = color
        self._direction:list  = [0, 0]

    def getRect(self) -> tuple:
        return (self.x, self.y, self.width, self.height)

    def getCenter(self) -> tuple:
        return (self.x + self._width//2, self.y + self._height//2)

    def draw(self, wn: object) -> None:
        pygame.draw.rect(wn, self._color, self.getRect())

    def move(self, dt: float) -> None:
        self.x += self._speed * self._direction[0] * dt 
        self.y += self._speed * self._direction[1] * dt 



