import math
from layout.layout import Layout
from sprite.sprite import ImageCroper
import pygame

class Pacman(object):
    def __init__(self, x, y, sql):
        self.x = x
        self.y = y
        self._length = sql-3
        self._direction = [0, 0]
        self._speed = 150
        self._score = 0
        self._animationCounter = 0
        self._animations = self._loadSprites()
        self._font    = pygame.font.SysFont(" ", 30, True)

    def _loadSprites(self) -> list:
        baseImage   = ImageCroper.loadImage('pacman/textures/pacman.png')
        transparent = ImageCroper.makeTransparant(baseImage, (0, 0, 0))
        croped      = ImageCroper.crop(transparent, 32, 32, 0)
        rezied      = [ImageCroper.resize(x, self._length, self._length) for x in croped]
        
        sprites = [pygame.image.fromstring(image.tobytes(), (self._length, self._length), 'RGBA') for image in rezied]
        sprites.reverse()
        sprites.append(sprites[1])
        return sprites

    @property
    def direction(self):
        return self._direction

    def draw(self, wn: object, dt: int):
        text = self._font.render('Score: {}'.format(self._score), 1, (255, 255, 0))
        wn.blit(text, (5, 5))

        if self._direction == [0, 0]:
            wn.blit(self._animations[0], (self.x, self.y))
            return

        self._animationCounter += dt
        idx = int(self._animationCounter // 0.05)
        if idx >= len(self._animations): 
            idx = self._animationCounter = 0

        rotation = math.degrees( -math.atan2(self._direction[1], self._direction[0]) )  
        rotated_texture = pygame.transform.rotate(self._animations[idx], rotation)
        
        wn.blit(rotated_texture, (self.x, self.y))

    def move(self, layout: Layout, dt: float) -> None:
        keys = pygame.key.get_pressed()

        # _nextTileIsFree makes sure pacman before he hits end of corridor
        if keys[pygame.K_DOWN] and self._nextTileIsFree(0, 1, layout) and self.direction != [0, 1]:
            self._direction = [0, 1]
        elif keys[pygame.K_UP] and self._nextTileIsFree(0, -1, layout) and self.direction != [0, -1]:
            self._direction = [0, -1]
        elif keys[pygame.K_RIGHT] and self._nextTileIsFree(1, 0, layout) and self.direction != [1, 0]:
            self._direction = [1, 0]
        elif keys[pygame.K_LEFT] and self._nextTileIsFree(-1, 0, layout) and self.direction != [-1, 0]:
            self._direction = [-1, 0]

        self.x += self._direction[0] * self._speed * dt
        self.y += self._direction[1] * self._speed * dt

    def eat(self, layout: Layout) -> None:
        row, column = self.getGridPos(self.x, self.y, layout.sql)
        if layout.eatPellet(row, column):
            self._score += 1

    def eatPowerPellet(self, layout: Layout, ghostWrapper: object) -> None:
        row, column = self.getGridPos(self.x, self.y, layout.sql)
        if layout.eatPowerPellet(row, column):
            self._score += 5
            ghostWrapper.setModeFrightend()

    def eatGhost(self, layout: Layout, ghostWrapper: object) -> None:
        pacPos = self.getGridPos(self.x, self.y, layout.sql)

        for ghost in ghostWrapper._ghosts:
            ghostPos = ghost.getGridPos(ghost.x, ghost.y, layout.sql)
            if pacPos == ghostPos:
                if ghost.isFrightend():
                    ghost.setModeReturn()
                    self._score += 20
                else:
                    pass
                    # Pacman loses health        

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
            row, column = self.getGridPos(corner[0], corner[1], layout.sql)
            if layout.isWall(row, column): # Detection

                # Resolution
                if self._direction[0] == 1:
                    wallPixelPosX = int(row * layout.sql) 
                    self.x = wallPixelPosX - self._length   - 0.01
                elif self._direction[0] == -1:
                    wallPixelPosX = int(row * layout.sql) 
                    self.x = wallPixelPosX + layout.sql + 0.01
                elif self._direction[1] == 1:
                    wallPixelPosX = int(column * layout.sql) 
                    self.y = wallPixelPosX - self._length  - 0.01
                elif self._direction[1] == -1:
                    wallPixelPosY = int(column * layout.sql) 
                    self.y = wallPixelPosY + layout.sql + 0.01

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
            row, column = self.getGridPos(corner[0], corner[1], layout.sql)
            row += x_direction
            column += y_direction
            if layout.isWall(row, column):
                return False
        return True





