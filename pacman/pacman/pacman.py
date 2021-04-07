from layout.layout import Layout
import pygame
pygame.init()

class Pacman(object):
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length-1
        self.dir = [0, 0]
        self.facing = [0, 0]
        self.speed = 150
        self.score = 0
        self._texture = pygame.image.load('pacman/textures/eating.png')
        self._font    = pygame.font.SysFont(" ", 30, True)


    def draw(self, wn):
        text = self._font.render('Score: {}'.format(self.score), 1, (255, 255, 0))
        wn.blit(text, (5, 5))

        if self.dir == [0, 0]:
            pygame.draw.circle(wn, (255, 255, 0), (int(self.x+self.length//2), int(self.y+self.length//2)), int(self.length//2))
            return

        
        scaled = pygame.transform.scale(self._texture, (self.length, self.length))
        
        rotation = 0 

        if self.dir == [1, 0]:
            rotation = 0
        elif self.dir == [-1, 0]:
            rotation = 180
        elif self.dir == [0, 1]:
            rotation = 270 
        elif self.dir == [0, -1]:
            rotation = 90
        
        
        rotated = pygame.transform.rotate(scaled, rotation)
        rect =  rotated.get_rect(center = scaled.get_rect(center = (self.x+self.length//2, self.y+self.length//2)).center)

        wn.blit(rotated, rect.topleft)
        
        # wn.blit(self._texture, (self.x, self.y))
        # pygame.draw.rect(wn, (255, 255, 0), (self.x, self.y, self.length, self.length))

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
        







