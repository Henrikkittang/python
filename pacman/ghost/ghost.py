from ghost.pathfinding import find_path
import pygame
pygame.init()

class Ghost(object):
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.dir = [0, 0]
        self.length = length-2
        self.color = None
        self.path = []
        self.speed = 120

    def draw(self, wn):
        pygame.draw.rect(wn, (255, 0, 0), (self.x, self.y, self.length, self.length))

        for p in self.path:
            pygame.draw.rect(wn, (0, 255, 0), (p[0]*(self.length+2), p[1]*(self.length+2), (self.length+2), (self.length+2)))

    def getGridPos(self, x: float, y: float, sql: int) -> list:
        return (int(x//sql), int(y//sql))


    def _insideTile(self, layout):
        corners = (
            (self.x, self.y), # Top left
            (self.x+self.length, self.y), # Top right
            (self.x, self.y+self.length), # Bottom left
            (self.x+self.length, self.y+self.length) # Bottom right
        )

        gridCorners = [self.getGridPos(x[0], x[1], layout.getSql()) for x in corners ]
        return all(x==gridCorners[0] for x in gridCorners)


    def move(self, layout, pacmanPos, dt):

        gridPos = self.getGridPos(self.x, self.y, layout.getSql())
        if len(self.path) < 4: 
            destination = self.getDestination(pacmanPos, layout.getSql())
            self.path = find_path(layout.getWalls(), gridPos, destination)

        if self._insideTile(layout):
            self.path.pop()

        self.getDirection(gridPos)

        self.x += self.dir[0] * self.speed * dt 
        self.y += self.dir[1] * self.speed * dt

    def getDirection(self, gridPos):
        self.dir = [0, 0]
        nextPos = self.path[-1]

        if gridPos[0] > nextPos[0]:
            self.dir = [-1, 0]
        elif gridPos[0] < nextPos[0]:
            self.dir = [1, 0]
        elif gridPos[1] > nextPos[1]:
            self.dir = [0, -1]
        elif gridPos[1] < nextPos[1]:
            self.dir = [0, 1]

        # print(gridPos, nextPos, self.dir)


    def getDestination(self, pacmanPos, sql):
        raise NotImplementedError() # Making the function kinda virtual



class Blinky(Ghost):
    def __init__(self, x, y, length):
        super().__init__(x, y, length)
        self.color = (255, 0, 0) # Red


    def getDestination(self, pacmanPos, sql):
        return (pacmanPos[0]//sql, pacmanPos[1]//sql)






 