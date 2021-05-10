import pygame

class Entity(object):
    def __init__(self, x, y, width, height, speed, color=(255, 255, 255)):
        self.x = x 
        self.y = y
        self._width = width
        self._height = height
        self._di
        self._speed = speed
        self._color = color

    def getRect(self) -> tuple:
        return (self.x, self.y, self.width, self.height)

    def draw(self, wn: object) -> None:
        pygame.draw.rect(wn, self._color, self(self.x, self.y, self.width, self.height))

    def move(self, dt: float) -> None:
        self.x += self._speed * dt 
        self.y += self._speed * dt 