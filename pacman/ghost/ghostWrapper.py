from ghost.ghostImpl import Blinky, Pinky, Inky, Clyde



class GhostWrapper(object):
    def __init__(self, startPos: tuple, sql: int):
        self._ghosts = [
            Blinky(startPos, (525, 25 ), sql),
            Pinky (startPos, (25 , 25 ), sql),
            Inky  (startPos, (525, 525), sql),
            Clyde (startPos, (25 , 525), sql),    
        ]
        self._frightendCounter = 0
        self._isFrightend = False

    def move(self, layout: object, pacman: object, dt: int) -> None:
        for ghost in self._ghosts:
            if isinstance(ghost, Inky):
                ghost.setBlinkyPosition(self._ghosts[0].getGridPos(self._ghosts[0].x, self._ghosts[0].y, layout.sql))
            ghost.move(layout, pacman, dt)

        if self._isFrightend and self._frightendCounter >= 8:
            [ghost.setModeChase() for ghost in self._ghosts]  
        else:
            self._frightendCounter += dt

    def draw(self, wn: object, dt: int) -> None:
        [ghost.draw(wn, dt) for ghost in self._ghosts]
        

    def setModeFrightend(self) -> None:
        self._frightendCounter = 0
        self._isFrightend = True
        [ghost.setModeFrightend() for ghost in self._ghosts]

    





