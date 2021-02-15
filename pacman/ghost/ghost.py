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

    def draw(self, wn):
        pygame.draw.rect(wn, (255, 0, 0), (self.x, self.y, self.length, self.length))

        for p in self.path:
            pygame.draw.rect(wn, (0, 255, 0), (p[0]*self.length, p[1]*self.length, self.length, self.length))


    def move(self, layout, pacmanPos):
        gridPos = (int((self.x+self.length/2)//layout.sql), int((self.y+self.length/2)//layout.sql))

        if len(self.path) < 4:
            destination = self.getDestination(pacmanPos, layout.sql)
            self.path = find_path(layout.walls, gridPos, destination, False)
        
        while gridPos != self.path[-1]:
            self.path.pop()

        self.getDirection(gridPos)
        self.x += self.dir[0] * 0.5 
        self.y += self.dir[1] * 0.5

    def getDirection(self, gridPos):
        self.dir = [0, 0]
        nextPos = self.path[-2]

        for idx in range(2):
            if gridPos[idx] > nextPos[idx]: self.dir[idx] = -1
            elif gridPos[idx] < nextPos[idx]: self.dir[idx] = 1 

    def getDestination(self, pacmanPos, sql):
        raise NotImplementedError() # Making the function kinda virtual



class Blinky(Ghost):
    def __init__(self, x, y, length):
        super().__init__(x, y, length)
        self.color = (255, 0, 0) # Red


    def getDestination(self, pacmanPos, sql):
        return (pacmanPos[0]//sql, pacmanPos[1]//sql)






 