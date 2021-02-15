import json
import pygame
pygame.init()

class Layout(object):
    def __init__(self):
        self.walls = []
        self.width = 0
        self.height = 0
        self.sql = 0
        self._readWallsFromFile()

    def _readWallsFromFile(self):
        with open('layout/map.json', 'r') as jsonFile:
            data = json.load(jsonFile)
            self.width = data['config']['screen_w']
            self.height = data['config']['screen_h']
            self.sql = data['config']['square_length']
            self.walls = [[0 for i in range(self.height//self.sql)] for j in range(self.width//self.sql)] 

            for pos in data['wallLayout']:
                self.walls[ pos[1] ][ pos[0] ] = 1

    def draw(self, wn):
        for row in range(len(self.walls)):
            for column in range(len(self.walls[row])):
                if self.walls[row][column] == 1:
                    pygame.draw.rect(wn, (40, 60, 235), (column*self.sql, row*self.sql, self.sql, self.sql))




if __name__ == '__main__':
    l = Layout()
