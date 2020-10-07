from global_things import *
import pygame
pygame.init()

def makeGrid(walls):
    grid = []
    for q in range(g_height):
        grid.append([])
        for k in range(g_width):
            grid[q].append(0)

    for wall in walls:
        grid[wall[1]][wall[0]] = 1

    return grid


class Pacman():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 255, 0)
        self.speed = 4 / g_sql # for every forth fram, pacman aligns with the grid
        self.offset = 3
        self.dir = (0, 0)

    def draw(self, wn):
        pygame.draw.rect(wn, self.color, (self.x*g_sql + self.offset, self.y*g_sql + self.offset, g_sql-self.offset*2, g_sql- self.offset*2))

    def move(self, grid):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.dir = (1, 0)
        if keys[pygame.K_LEFT]:
            self.dir = (-1, 0)
        if keys[pygame.K_DOWN]:
            self.dir = (0, 1)
        if keys[pygame.K_UP]:
            self.dir = (0, -1)

        self.collision(grid)

        self.x += self.dir[0] * self.speed
        self.y += self.dir[1] * self.speed


    def collision(self, grid):
        TL = (self.x, self.y)
        TR = (self.x + g_sql, self.y)
        BL = (self.x, self.y + g_sql)
        BR = (self.x + g_sql, self.y + g_sql)

        if self.dir == (1, 0):
            BottomRightTile = grid[ BR[1] ][ BR[0] ]
            topRightTile = grid[ TR[1] ][ TR[0] ]
            if (BottomRightTile or topRightTile) == 1:
                self.dir = (0, 0)






def main():
    wn = pygame.display.set_mode((g_width, g_height))
    walls = readJsonFile('map')['wallLayout']
    grid = makeGrid(walls)

    pacman = Pacman(10, 7)
    while True:
        wn.fill((0, 0, 0))
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        displayGrid(wn)

        for wall in walls:
            drawWall(wn, wall)

        pacman.move(grid)
        pacman.draw(wn)

        pygame.display.update()
main()