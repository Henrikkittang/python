import math

from layout.layout import Layout
import pygame
pygame.init()

class Pacman(object):
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length-1
        self.dir = [0, 0]
        self.speed = 150
        self.score = 0
        self._animation_counter = 0
        self._animations = [
            pygame.image.load('pacman/textures/pac1.png'),
            pygame.image.load('pacman/textures/pac2.png'),
            pygame.image.load('pacman/textures/pac3.png'),
            pygame.image.load('pacman/textures/pac2.png')
        ]
        self._font    = pygame.font.SysFont(" ", 30, True)


    def draw(self, wn, dt):
        text = self._font.render('Score: {}'.format(self.score), 1, (255, 255, 0))
        wn.blit(text, (5, 5))

        if self.dir == [0, 0]:
            wn.blit(self._animations[0], (self.x, self.y))
            return

        self._animation_counter += dt
        idx = int(self._animation_counter // 0.05)
        if idx >= len(self._animations): 
            self._animation_counter = 0
            idx = 0

        rotation = math.degrees( -math.atan2(self.dir[1], self.dir[0]) )  
        rotated_texture = pygame.transform.rotate(self._animations[idx], rotation)
        
        wn.blit(rotated_texture, (self.x, self.y))
        

    def _nextTileIsFree(self, xDir: int, yDir: int, layout: Layout) -> bool:
        corners = (
            (self.x, self.y), # Top left
            (self.x+self.length, self.y), # Top right
            (self.x, self.y+self.length), # Bottom left
            (self.x+self.length, self.y+self.length) # Bottom right
        )
        
        for corner in corners:
            row, column = self.getGridPos(corner[0], corner[1], layout.getSql())
            row += xDir
            column += yDir
            if layout.isWall(row, column):
                return False
        return True

    def move(self, layout, dt: float) -> None:
        keys = pygame.key.get_pressed()

        # _nextTileIsFree makes sure pacman before he hits end of corridor
        if keys[pygame.K_DOWN] and self._nextTileIsFree(0, 1, layout):
            self.dir = [0, 1]
        elif keys[pygame.K_UP] and self._nextTileIsFree(0, -1, layout):
            self.dir = [0, -1]
        elif keys[pygame.K_RIGHT] and self._nextTileIsFree(1, 0, layout):
            self.dir = [1, 0]
        elif keys[pygame.K_LEFT] and self._nextTileIsFree(-1, 0, layout):
            self.dir = [-1, 0]

        self.x += self.dir[0] * self.speed * dt
        self.y += self.dir[1] * self.speed * dt

    def eat(self, layout) -> None:
        row, column = self.getGridPos(self.x, self.y, layout.getSql())
        if layout.eatPellet(row, column):
            self.score += 1

    def getGridPos(self, x: float, y: float, sql: int) -> tuple:
        return (int(x//sql), int(y//sql))

    def checkColliding(self, layout: Layout) -> None:
        corners = [
            (self.x, self.y), # Top left
            (self.x+self.length, self.y), # Top right
            (self.x, self.y+self.length), # Bottom left
            (self.x+self.length, self.y+self.length) # Bottom right
        ]

        for corner in corners:
            row, column = self.getGridPos(corner[0], corner[1], layout.getSql())
            if layout.isWall(row, column): # Detection

                # Resolution
                if self.dir[0] == 1:
                    wallPixelPosX = int(row * layout.getSql()) 
                    self.x = wallPixelPosX - self.length   - 0.01
                elif self.dir[0] == -1:
                    wallPixelPosX = int(row * layout.getSql()) 
                    self.x = wallPixelPosX + layout.getSql() + 0.01
                elif self.dir[1] == 1:
                    wallPixelPosX = int(column * layout.getSql()) 
                    self.y = wallPixelPosX - self.length  - 0.01
                elif self.dir[1] == -1:
                    wallPixelPosY = int(column * layout.getSql()) 
                    self.y = wallPixelPosY + layout.getSql() + 0.01

                self.dir = [0, 0]
                break
        







