from random import randint
from collections import deque
from a_star import find_path
import numpy as np
import pygame
pygame.init()

s_width = 600
s_height = 600
square_length = 20
wn = pygame.display.set_mode((s_width, s_height))

def makeEmptyGrid():
    grid = np.ones((s_width // square_length, s_height // square_length))
    grid[1:-1,1:-1] = 0
    return grid

class Snake(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.body = deque([(self.x, self.y)])
        self.path = []

    def draw(self, wn):
        for pos in self.body:
            xPixel = pos[0] * square_length
            yPixel = pos[1] * square_length
            pygame.draw.rect(wn, (255, 0, 0), (xPixel, yPixel, square_length, square_length))

    def collision(self):
        # Collision with body
        for idx, pos in enumerate(self.body):
            # dont check the last element (head) beacuse that is ofcourse the same as itself
            if (self.x, self.y) == pos and idx == len(self.body)-2:
                self.body = deque([(self.x, self.y)])
                return

        # Collision with apple
        if (self.x, self.y) == (food.x, food.y):
            main_grid[self.y][self.x] = 1
            self.body.append((self.x, self.y))
            food.new_pos()
            self.find_path()

    def find_path(self):
        self.path = find_path(main_grid, (self.x, self.y), (food.x, food.y), False)        
        
        if self.path == None:
            print( (self.x, self.y), (food.x, food.y))
            print('no path found')
            quit()
        
        self.path.pop()

    def move(self):
        grid_pos = self.path[-1]
        self.path.pop()

        self.x = grid_pos[0]
        self.y = grid_pos[1]

        p = self.body.popleft()
        self.body.append((self.x, self.y))

        main_grid[p[1]][p[0]] = 0
        main_grid[self.y][self.x] = 1

        self.collision()



class Apple(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def draw(self, wn):
        xPixel = self.x * square_length
        yPixel = self.y * square_length
        pygame.draw.rect(wn, (0, 255, 0), (xPixel, yPixel, square_length, square_length))

    def new_pos(self):
        self.x = randint(2, s_width//square_length - 3)
        self.y = randint(2, s_height//square_length - 3)

        idx = 0
        while idx < len(player.body) - 1:
            if (self.x, self.y) == player.body[idx]:
                self.x = randint(2, s_width//square_length - 3)
                self.y = randint(2, s_height//square_length - 3)

                idx = 0
                continue
            idx += 1
                
def draw_grid():
    """Draws the lines representing the grid"""
    for i in range(0, s_height, square_length):
        pygame.draw.line(wn, (255, 0, 0), (0, i), (s_width, i), 1)

    for i in range(0, s_width, square_length):
        pygame.draw.line(wn, (255, 0, 0), (i, 0), (i, s_height))


def draw_window():
    wn.fill((0, 0, 0))

    # draw_grid()

    player.draw(wn)
    food.draw(wn)    

    score = font.render("Score: " + str(len(player.body)), 1, (240, 255, 0))
    wn.blit(score, (5, 5))

    pygame.display.update()

main_grid = makeEmptyGrid()

food = Apple(10, 13)
player = Snake(10, 10)
player.find_path()
font = pygame.font.SysFont(" ", 30, True)
while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    player.move()

    draw_window()
