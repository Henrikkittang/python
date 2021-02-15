from layout.layout import Layout
import pygame
pygame.init()


class Pacman(object):
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length-2
        self.dir = [0, 0]

    def draw(self, wn):
        pygame.draw.rect(wn, (255, 255, 0), (self.x, self.y, self.length, self.length))

    def move(self, layout):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            self.dir = [0, 1]
        elif keys[pygame.K_UP]:
            self.dir = [0, -1]
        elif keys[pygame.K_RIGHT]:
            self.dir = [1, 0]
        elif keys[pygame.K_LEFT]:
            self.dir = [-1, 0]

        self.checkColliding(layout)

        self.x += self.dir[0]
        self.y += self.dir[1]


    def checkColliding(self, layout):
        corners = [
            (self.x, self.y),
            (self.x+self.length, self.y),
            (self.x, self.y+self.length),
            (self.x+self.length, self.y+self.length)
        ]

        for corner in corners:
            row, column = (corner[0]+self.dir[0])//layout.sql, (corner[1]+self.dir[1])//layout.sql
            if layout.walls[column][row] == 1:
                self.dir = [0, 0]
                break
        







