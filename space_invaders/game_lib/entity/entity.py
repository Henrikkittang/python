import pygame

class Entity(object):
    def __init__(self, x, y, width, height, speed):
        self.x = x 
        self.y = y
        self._width = width
        self._height = height
        self._speed = speed

    def getRect(self) -> tuple:
        return (self.x, self.y, self.width, self.height)

    def draw(self, wn: object) -> None:
        pygame.draw.rect(wn, (0, 255, 0), (self.x, self.y, self.width, self.height))

    def move(self, dt: float) -> None:
        self.x += self._speed * dt 
        self.y += self._speed * dt 