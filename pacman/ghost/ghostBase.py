from math import sqrt
from random import randint
from enum import Enum
from sprite.sprite import ImageCroper
import pygame
pygame.init()

class Mode(Enum):
    CHASE = 1
    FRIGHTEND = 2
    SCATTER = 3
    RETURN = 4

class GhostBase(object):
    def __init__(self, pixelPos: tuple, cornerPos: tuple, sql: int):
        self.x, self.y = pixelPos
        self._start = self.getGridPos(self.x, self.y, sql)
        self._corner = self.getGridPos(cornerPos[0], cornerPos[1], sql)
        self._length = sql-3
        self._speed = 120
        self._direction = (0, 0)
        self._animationCounter = 0
        self._moveCounter = 0
        self._mode = Mode.CHASE
        self._frighendModeAnimation = (
            pygame.image.load('ghost/textures/frightend1.png'),
            pygame.image.load('ghost/textures/frightend2.png'),
        )
        self._eyesSprites = {}
        self._frightendCounter = 0

        self._loadEyes()

    def setModeFrightend(self) -> None:
        self._frightendCounter = 0
        if self._mode != Mode.RETURN:
            self._mode = Mode.FRIGHTEND
            self._speed = 100
    def setModeChase(self) -> None:
        self._mode = Mode.CHASE
        self._speed = 120
    def setModeScatter(self) -> None:
        self._mode = Mode.SCATTER
        self._speed = 120
    def setModeReturn(self) -> None:
        self._mode = Mode.RETURN
        self._speed = 180

    def isFrightend(self) -> bool:
        return self._mode == Mode.FRIGHTEND
    
    def draw(self, wn, dt: float) -> None:
        self._animationCounter += dt

        idx = int(self._animationCounter // 0.05)
        if idx >= 2: 
            idx = self._animationCounter = 0
        
        directions = {
            (1,  0): (self._animations[0], self._animations[1]),
            (-1, 0): (self._animations[2], self._animations[3]),
            (0, -1): (self._animations[4], self._animations[5]),
            (0,  1): (self._animations[6], self._animations[7]),
        }
        
        if self._mode == Mode.CHASE or self._mode == Mode.SCATTER:
            wn.blit(directions[self._direction][idx], (self.x, self.y))
    
        elif self._mode == Mode.FRIGHTEND:
            wn.blit(self._frighendModeAnimation[idx], (self.x, self.y))

        elif self._mode == Mode.RETURN:
            wn.blit(self._eyesSprites[self._direction], (self.x, self.y))
            # pygame.draw.rect(wn, (255, 255, 255), (self.x, self.y, self._length, self._length))

    def getGridPos(self, x: float, y: float, sql: int) -> list:
        return (int(x//sql), int(y//sql))

    def move(self, layout: object, pacman: object, dt: float):
        
        # if isinstance(self, Blinky): print(self._frightendCounter)
        if self._mode == Mode.FRIGHTEND and self._frightendCounter >= 0.080:
            self.setModeChase()

        gridPos = self.getGridPos(self.x, self.y, layout.sql)
        if self._mode == Mode.RETURN and gridPos == self._start:
            self.setModeChase()
                    
        self._moveCounter += dt
        if self._insideTile(layout) and self._moveCounter > 0.030:
            self._moveCounter = 0

            tiles = self._findTiles(layout)

            if self._mode == Mode.CHASE:
                target = self._getDestination(layout, pacman)
                tiles.sort(key = lambda tile: self.dist(tile[0], tile[1], target[0], target[1]))
                self._setDirection(layout, tiles[0])

            elif self._mode == Mode.FRIGHTEND:
                self._frightendCounter += dt
                idx = randint(0, len(tiles)-1)
                self._setDirection(layout, tiles[idx])

            elif self._mode == Mode.SCATTER:
                target = self._corner
                tiles.sort(key = lambda tile: self.dist(tile[0], tile[1], target[0], target[1]))
                self._setDirection(layout, tiles[0])
            
            elif self._mode == Mode.RETURN:
                target = self._start
                tiles.sort(key = lambda tile: self.dist(tile[0], tile[1], target[0], target[1]))
                self._setDirection(layout, tiles[0])


        self.x += self._direction[0] * self._speed * dt 
        self.y += self._direction[1] * self._speed * dt
        
    def _findTiles(self, layout: object):
        '''
        Finds the adjecent but not diagonal to ghosts grid position
        @param layout: object
        '''
        # Find all tiles that are not walls
        # Remove tile behind ghost

        tiles = []
        gridPos = self.getGridPos(self.x, self.y, layout.sql)
        if not layout.isWall(gridPos[0]+1, gridPos[1]):
            tiles.append( (gridPos[0]+1, gridPos[1]) )
        if not layout.isWall(gridPos[0]-1, gridPos[1]):
            tiles.append( (gridPos[0]-1, gridPos[1]) )
        if not layout.isWall(gridPos[0], gridPos[1]+1):
            tiles.append( (gridPos[0], gridPos[1]+1) )
        if not layout.isWall(gridPos[0], gridPos[1]-1):
            tiles.append( (gridPos[0], gridPos[1]-1) )
      
        prevTile = (gridPos[0]-self._direction[0], gridPos[1]-self._direction[1])
        self.prevPos = prevTile

        if prevTile in tiles: tiles.remove(prevTile)
        return tiles

    def dist(self, x1: float, y1: float, x2: float, y2: float) -> float:
        return sqrt((x2-x1)**2 + (y2-y1)**2)

    def _setDirection(self, layout, nextTile: tuple) -> None:
        gridPos = self.getGridPos(self.x, self.y, layout.sql)

        if   gridPos[0] > nextTile[0]: self._direction = (-1,  0)
        elif gridPos[0] < nextTile[0]: self._direction = ( 1,  0)
        elif gridPos[1] > nextTile[1]: self._direction = ( 0, -1)
        elif gridPos[1] < nextTile[1]: self._direction = ( 0,  1)

    def _insideTile(self, layout: object) -> bool:
        corners = (
            (self.x, self.y), # Top left
            (self.x+self._length, self.y), # Top right
            (self.x, self.y+self._length), # Bottom left
            (self.x+self._length, self.y+self._length) # Bottom right
        )

        gridCorners = [self.getGridPos(x[0], x[1], layout.sql) for x in corners ]
        return all(x==gridCorners[0] for x in gridCorners)
    
    def _loadEyes(self):
        baseImage   = ImageCroper.loadImage('ghost/textures/eyes.png')
        transparent = ImageCroper.makeTransparant(baseImage, (0, 0, 0))
        croped      = ImageCroper.crop(transparent, 14, 14, 2)
        rezied      = [ImageCroper.resize(x, self._length, self._length) for x in croped]

        temp = [pygame.image.fromstring(image.tobytes(), (self._length, self._length), 'RGBA') for image in rezied]
        self._eyesSprites  = {
            (1,  0): temp[0],
            (-1, 0): temp[1],
            (0, -1): temp[2],
            (0,  1): temp[3],
        }

    def _loadSprites(self, idx1: int, idx2: int) -> list:
        baseImage   = ImageCroper.loadImage('ghost/textures/spritesheet.png')
        transparent = ImageCroper.makeTransparant(baseImage, (0, 0, 0))
        croped      = ImageCroper.crop(transparent, 14, 14, 2)
        rezied      = [ImageCroper.resize(x, self._length, self._length) for x in croped]

        sprites = [pygame.image.fromstring(image.tobytes(), (self._length, self._length), 'RGBA') for image in rezied]
        return sprites[idx1:idx2]

    def _getDestination(self, layout: object, pacman: object) -> tuple:
        raise NotImplementedError() # Making the function kinda virtual

