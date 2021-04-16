from math import sqrt
from random import randint
from enum import Enum
from ghost.sprites import ImageCroper
import pygame
pygame.init()

class Mode(Enum):
    CHASE = 1
    FRIGHTEND = 2
    SCATTER = 3

class Ghost(object):
    def __init__(self, pixelPos: tuple, cornerPos: tuple, sql: int):
        self.x, self.y = pixelPos
        self._corner = self.getGridPos(cornerPos[0], cornerPos[1], sql)
        self.length = sql-3
        self.speed = 120
        self.dir = (0, 0)
        self._animation_counter = 0
        self.counter = 0
        self._mode = Mode.CHASE
        self._frighend_mode_animation = (
            pygame.image.load('ghost/textures/frightend1.png'),
            pygame.image.load('ghost/textures/frightend2.png'),
        )
    
    def draw(self, wn, dt: float) -> None:
        self._animation_counter += dt

        idx = int(self._animation_counter // 0.05)
        if idx >= 2: 
            idx = self._animation_counter = 0
        
        directions = {
            (1,  0): (self._animations[0], self._animations[1]),
            (-1, 0): (self._animations[2], self._animations[3]),
            (0, -1): (self._animations[4], self._animations[5]),
            (0,  1): (self._animations[6], self._animations[7]),
        }
        
        if self._mode == Mode.CHASE or self._mode == Mode.SCATTER:
            wn.blit(directions[self.dir][idx], (self.x, self.y))
    
        elif self._mode == Mode.FRIGHTEND:
            wn.blit(self._frighend_mode_animation[idx], (self.x, self.y))

    def getGridPos(self, x: float, y: float, sql: int) -> list:
        return (int(x//sql), int(y//sql))

    def move(self, layout: object, pacman: object, dt: float):
        # Check that ghost is fully inside square
            # Find available tiles
                # Cant move backwards or to wall-tiles
            # Find closest tile to target
                # Pytagoras from sqaure to target
        # Move in next tile`s direction
        
        self.counter += dt
        if self._insideTile(layout) and self.counter > 0.030:
            self.counter = 0

            tiles = self._findTiles(layout)

            if self._mode == Mode.CHASE:
                target = self._getDestination(layout, pacman)
                tiles.sort(key = lambda tile: self.dist(tile[0], tile[1], target[0], target[1]))
                self._setDirection(layout, tiles[0])

            elif self._mode == Mode.FRIGHTEND:
                idx = randint(0, len(tiles)-1)
                self._setDirection(layout, tiles[idx])

            elif self._mode == Mode.SCATTER:
                target = self._corner
                tiles.sort(key = lambda tile: self.dist(tile[0], tile[1], target[0], target[1]))
                self._setDirection(layout, tiles[0])

        self.x += self.dir[0] * self.speed * dt 
        self.y += self.dir[1] * self.speed * dt
        


    def _findTiles(self, layout):
        # Find all tiles that are not walls
        # Remove tile behind ghost

        tiles = []
        gridPos = self.getGridPos(self.x, self.y, layout.getSql())
        if not layout.isWall(gridPos[0]+1, gridPos[1]):
            tiles.append( (gridPos[0]+1, gridPos[1]) )

        if not layout.isWall(gridPos[0]-1, gridPos[1]):
            tiles.append( (gridPos[0]-1, gridPos[1]) )

        if not layout.isWall(gridPos[0], gridPos[1]+1):
            tiles.append( (gridPos[0], gridPos[1]+1) )

        if not layout.isWall(gridPos[0], gridPos[1]-1):
            tiles.append( (gridPos[0], gridPos[1]-1) )
      
        prevTile = (gridPos[0]-self.dir[0], gridPos[1]-self.dir[1])
        self.prevPos = prevTile

        if prevTile in tiles: tiles.remove(prevTile)
        return tiles

    def dist(self, x1: int, y1: int, x2: int, y2: int) -> float:
        return sqrt((x2-x1)**2 + (y2-y1)**2)

    def _setDirection(self, layout, nextTile: tuple) -> None:
        gridPos = self.getGridPos(self.x, self.y, layout.getSql())

        if   gridPos[0] > nextTile[0]: self.dir = (-1,  0)
        elif gridPos[0] < nextTile[0]: self.dir = ( 1,  0)
        elif gridPos[1] > nextTile[1]: self.dir = ( 0, -1)
        elif gridPos[1] < nextTile[1]: self.dir = ( 0,  1)

    def _insideTile(self, layout) -> bool:
        corners = (
            (self.x, self.y), # Top left
            (self.x+self.length, self.y), # Top right
            (self.x, self.y+self.length), # Bottom left
            (self.x+self.length, self.y+self.length) # Bottom right
        )

        gridCorners = [self.getGridPos(x[0], x[1], layout.getSql()) for x in corners ]
        return all(x==gridCorners[0] for x in gridCorners)
    
    def _loadGhosts(self, idx1, idx2):
        baseImage = ImageCroper.loadImage('ghost/textures/spritesheet.png')
        transparent = ImageCroper.makeTransparant(baseImage, (0, 0, 0))
        croped = ImageCroper.crop(transparent, 14, 14, 2)
        rezied = [ImageCroper.resize(x, 22, 22) for x in croped]
        
        sprites = [pygame.image.fromstring(image.tobytes(), (self.length, self.length), 'RGBA') for image in rezied]
        return sprites[idx1:idx2]

    def _getDestination(self, layout: object, pacman: object) -> tuple:
        raise NotImplementedError() # Making the function kinda virtual



class Blinky(Ghost):
    def __init__(self, pixelPos: tuple, cornerPos: tuple, sql: int):
        super().__init__(pixelPos, cornerPos, sql)
        self._animations = super()._loadGhosts(0, 8)
        
    # Chases pacman exact position
    def _getDestination(self, layout: object, pacman: object) -> tuple:
        return pacman.getGridPos(pacman.x, pacman.y, layout.getSql())


class Pinky(Ghost):
    def __init__(self, pixelPos: tuple, cornerPos: tuple, sql: int):
        super().__init__(pixelPos, cornerPos, sql)
        self._animations = super()._loadGhosts(8, 16)

        self.facing = [0, 0] # tracks pacman facing instead of direction


    # Finds position 4 tile ahead of pacman
    def _getDestination(self, layout: object, pacman: object) -> tuple:
        if pacman.dir != [0, 0]:
            self.facing = pacman.dir

        pacGridPos = pacman.getGridPos(pacman.x, pacman.y, layout.getSql())
        for i in range(4, -1, -1):
            row    = pacGridPos[0] + self.facing[0] * i
            column = pacGridPos[1] + self.facing[1] * i
            if not layout.isWall(row, column):
                return (row, column)
        return pacGridPos 

class Inky(Ghost):
    def __init__(self, pixelPos: tuple, cornerPos: tuple, sql: int):
        super().__init__(pixelPos, cornerPos, sql)
        self.blinkyPos = (0, 0)
        self._animations = super()._loadGhosts(16, 24)


    def setBlinkyPosition(self, blinkyPos: tuple) -> None:
        self.blinkyPos = blinkyPos

    def _getDestination(self, layout: object, pacman: object) -> tuple:
        pacPos = pacman.getGridPos(pacman.x, pacman.y, layout.getSql())
        # gridPos = self.getGridPos(self.x, self.y, layout.getSql())

        vect = [self.blinkyPos[0]-pacPos[0], self.blinkyPos[1]-pacPos[1]]
        vect = [-x for x in vect]

        target = (pacPos[0]+vect[0], pacPos[1]+vect[1])
        return target


class Clyde(Ghost):
    def __init__(self, pixelPos: tuple, cornerPos: tuple, sql: int):
        super().__init__(pixelPos, cornerPos, sql)
        self._animations = super()._loadGhosts(24, 32)

    # Same as blinkey, but runs to corner when close to pacman
    def _getDestination(self, layout: object, pacman: object) -> tuple:
        pacPos = pacman.getGridPos(pacman.x, pacman.y, layout.getSql())
        selfPos = super().getGridPos(self.x, self.y, layout.getSql())

        dist = sqrt((selfPos[0] - pacPos[0])**2 + (selfPos[1] - pacPos[1])**2)

        return (self._corner if dist < 8 else pacPos)
        



 