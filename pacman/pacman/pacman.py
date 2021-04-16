import math

from layout.layout import Layout
import pygame
pygame.init()

class Pacman(object):
    def __init__(self, x, y, sql):
        self.x = x
        self.y = y
        self._length = sql-1
        self._direction = [0, 0]
        self._speed = 150
        self._score = 0
        self._animationCounter = 0
        self._animations = [
            pygame.image.load('pacman/textures/pac1.png'),
            pygame.image.load('pacman/textures/pac2.png'),
            pygame.image.load('pacman/textures/pac3.png'),
            pygame.image.load('pacman/textures/pac2.png')
        ]
        self._font    = pygame.font.SysFont(" ", 30, True)

    @property
    def direction(self):
        return self._direction

    def draw(self, wn, dt):
        text = self._font.render('_Score: {}'.format(self._score), 1, (255, 255, 0))
        wn.blit(text, (5, 5))

        if self._direction == [0, 0]:
            wn.blit(self._animations[0], (self.x, self.y))
            return

        self._animationCounter += dt
        idx = int(self._animationCounter // 0.05)
        if idx >= len(self._animations): 
            self._animationCounter = 0
            idx = 0

        rotation = math.degrees( -math.atan2(self._direction[1], self._direction[0]) )  
        rotated_texture = pygame.transform.rotate(self._animations[idx], rotation)
        
        wn.blit(rotated_texture, (self.x, self.y))
    def move(self, layout, dt: float) -> None:
        keys = pygame.key.get_pressed()

        # _nextTileIsFree makes sure pacman before he hits end of corridor
        if keys[pygame.K_DOWN] and self._nextTileIsFree(0, 1, layout):
            self._direction = [0, 1]
        elif keys[pygame.K_UP] and self._nextTileIsFree(0, -1, layout):
            self._direction = [0, -1]
        elif keys[pygame.K_RIGHT] and self._nextTileIsFree(1, 0, layout):
            self._direction = [1, 0]
        elif keys[pygame.K_LEFT] and self._nextTileIsFree(-1, 0, layout):
            self._direction = [-1, 0]

        self.x += self._direction[0] * self._speed * dt
        self.y += self._direction[1] * self._speed * dt

    def eat(self, layout) -> None:
        row, column = self.getGridPos(self.x, self.y, layout.getSql())
        if layout.eatPellet(row, column):
            self._score += 1

    def getGridPos(self, x: float, y: float, sql: int) -> tuple:
        return (int(x//sql), int(y//sql))

    def checkColliding(self, layout: Layout) -> None:
        corners = [
            (self.x, self.y), # Top left
            (self.x+self._length, self.y), # Top right
            (self.x, self.y+self._length), # Bottom left
            (self.x+self._length, self.y+self._length) # Bottom right
        ]

        for corner in corners:
            row, column = self.getGridPos(corner[0], corner[1], layout.getSql())
            if layout.isWall(row, column): # Detection

                # Resolution
                if self._direction[0] == 1:
                    wallPixelPosX = int(row * layout.getSql()) 
                    self.x = wallPixelPosX - self._length   - 0.01
                elif self._direction[0] == -1:
                    wallPixelPosX = int(row * layout.getSql()) 
                    self.x = wallPixelPosX + layout.getSql() + 0.01
                elif self._direction[1] == 1:
                    wallPixelPosX = int(column * layout.getSql()) 
                    self.y = wallPixelPosX - self._length  - 0.01
                elif self._direction[1] == -1:
                    wallPixelPosY = int(column * layout.getSql()) 
                    self.y = wallPixelPosY + layout.getSql() + 0.01

                self._direction = [0, 0]
                break
        

    def _nextTileIsFree(self, x_direction: int, y_direction: int, layout: Layout) -> bool:
        corners = (
            (self.x, self.y), # Top left
            (self.x+self._length, self.y), # Top right
            (self.x, self.y+self._length), # Bottom left
            (self.x+self._length, self.y+self._length) # Bottom right
        )
        
        for corner in corners:
            row, column = self.getGridPos(corner[0], corner[1], layout.getSql())
            row += x_direction
            column += y_direction
            if layout.isWall(row, column):
                return False
        return True





