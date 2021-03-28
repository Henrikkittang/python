import json
import pygame
pygame.init()

class Layout(object):
    def __init__(self):
        self._walls = []
        self._width = 0
        self._height = 0
        self._sql = 0
        self._readWallsFromFile()

    def _readWallsFromFile(self):
        with open('layout/map.json', 'r') as jsonFile:
            data = json.load(jsonFile)
            self._width = data['config']['screen_w']
            self._height = data['config']['screen_h']
            self._sql = data['config']['square_length']
            self._walls = [[0 for i in range(self._height//self._sql)] for j in range(self._width//self._sql)] 

            for pos in data['wallLayout']:
                self._walls[ pos[1] ][ pos[0] ] = 1

    def isWall(self, row: int, column: int) -> bool:
        return bool(self._walls[column][row])

    def getWalls(self) -> list: return self._walls
    
    def getWidth(self) -> int: return self._width
    def getHeight(self) -> int: return self._height
    def getSql(self) -> int: return self._sql

    def draw(self, wn) -> None:
        for row in range(len(self._walls)):
            for column in range(len(self._walls[row])):
                if self._walls[row][column] == 1:
                    pygame.draw.rect(wn, (40, 60, 235), (column*self._sql, row*self._sql, self._sql, self._sql))




if __name__ == '__main__':
    l = Layout()
