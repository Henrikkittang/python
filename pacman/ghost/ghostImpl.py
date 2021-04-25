from math import sqrt
from ghost.ghostBase import GhostBase

class Blinky(GhostBase):
    def __init__(self, pixelPos: tuple, cornerPos: tuple, sql: int):
        super().__init__(pixelPos, cornerPos, sql)
        self._animations = super()._loadSprites(0, 8)
        self._speed = 155

    # Chases pacman exact position
    def _getDestination(self, layout: object, pacman: object) -> tuple:
        return pacman.getGridPos(pacman.x, pacman.y, layout.sql)


class Pinky(GhostBase):
    def __init__(self, pixelPos: tuple, cornerPos: tuple, sql: int):
        super().__init__(pixelPos, cornerPos, sql)
        self._animations = super()._loadSprites(8, 16)

        self.facing = [0, 0] # tracks pacman facing instead of _directionection


    # Finds position 4 tile ahead of pacman
    def _getDestination(self, layout: object, pacman: object) -> tuple:
        if pacman.direction != [0, 0]:
            self.facing = pacman.direction

        pacGridPos = pacman.getGridPos(pacman.x, pacman.y, layout.sql)
        row    = pacGridPos[0] + self.facing[0] * 4
        column = pacGridPos[1] + self.facing[1] * 4

        return (row, column)

class Inky(GhostBase):
    def __init__(self, pixelPos: tuple, cornerPos: tuple, sql: int):
        super().__init__(pixelPos, cornerPos, sql)
        self.blinkyPos = (0, 0)
        self._animations = super()._loadSprites(16, 24)


    def setBlinkyPosition(self, blinkyPos: tuple) -> None:
        self.blinkyPos = blinkyPos

    def _getDestination(self, layout: object, pacman: object) -> tuple:
        pacPos = pacman.getGridPos(pacman.x, pacman.y, layout.sql)
        # gridPos = self.getGridPos(self.x, self.y, layout.sql)

        vect = [self.blinkyPos[0]-pacPos[0], self.blinkyPos[1]-pacPos[1]]
        vect = [-x for x in vect]

        target = (pacPos[0]+vect[0], pacPos[1]+vect[1])
        return target


class Clyde(GhostBase):
    def __init__(self, pixelPos: tuple, cornerPos: tuple, sql: int):
        super().__init__(pixelPos, cornerPos, sql)
        self._animations = super()._loadSprites(24, 32)

    # Same as blinkey, but runs to corner when close to pacman
    def _getDestination(self, layout: object, pacman: object) -> tuple:
        pacPos = pacman.getGridPos(pacman.x, pacman.y, layout.sql)
        selfPos = super().getGridPos(self.x, self.y, layout.sql)

        dist = sqrt((selfPos[0] - pacPos[0])**2 + (selfPos[1] - pacPos[1])**2)

        return (self._corner if dist < 8 else pacPos)
        
