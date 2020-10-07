import test
from random import randint
from math import sqrt
import pygame
pygame.init()

s_width = 600
s_height = 600
square_length = 25
wn = pygame.display.set_mode((s_width, s_height))

main_grid = []
for q in range(0, s_height//square_length):
    main_grid.append([])
    for t in range(0, s_width//square_length):
        main_grid[q].append(0)

# Adds the border around the whole screen
for i in range(0, len(main_grid[0])):
    main_grid[0][i], main_grid[-1][i] = 1000000, 1000000  # Top and bottom


for i in range(0, len(main_grid)):
    main_grid[i][0], main_grid[i][-1] = 1000000, 1000000  # Left and right


class Snake(object):
    def __init__(self, start_pos):
        self.grid_pos = start_pos
        self.length = 3
        self.direction = "left"
        self.path = []

    def draw(self, wn):
        for i in range(0, len(main_grid)):
            for q in range(0, len(main_grid[i])):
                if main_grid[i][q] > 0:
                    pygame.draw.rect(wn, (255, 0, 0), (q*square_length + 1, i*square_length + 1, square_length - 1, square_length - 1))
                    main_grid[i][q] -= 1

    def find_path(self):
            self.path = test.find_path(main_grid, player.grid_pos, food.pos, False)
            while self.path == None:
                food.new_pos()
                self.path = test.find_path(main_grid, player.grid_pos, food.pos, False)

    def move(self):
        next_tile = self.path[0]
        self.path.pop(0)

        self.grid_pos = next_tile

        x = self.grid_pos[0]
        y = self.grid_pos[1]

        main_grid[y][x] = self.length

        if self.grid_pos[0] < 0 or self.grid_pos[1] < 0:
            quit()


class Apple(object):
    def __init__(self, pos):
        self.pos = pos
        self.x = self.pos[0] * square_length
        self.y = self.pos[1] * square_length

    def draw(self, wn):
        self.x = self.pos[0] * square_length
        self.y = self.pos[1] * square_length
        pygame.draw.rect(wn, (0, 255, 0), (self.x + 1, self.y + 1, square_length, square_length))

    def new_pos(self):
        pos = (randint(1, (s_width//square_length) - 2), randint(1, (s_height//square_length) - 2))
        while main_grid[pos[1]][pos[0]] != 0:
            pos = (randint(1, (s_width // square_length) - 2), randint(1, (s_height // square_length) - 2))
        self.pos = pos


def calc_distance(cor1, cor2):
    distance = sqrt((cor1[0] - cor2[0])**2 + (cor1[1] - cor2[1])**2)
    return distance


def draw_grid():
    """Draws the lines representing the grid"""
    for i in range(0, s_height, square_length):
        pygame.draw.line(wn, (255, 0, 0), (0, i), (s_width, i), 1)

    for i in range(0, s_width, square_length):
        pygame.draw.line(wn, (255, 0, 0), (i, 0), (i, s_height))


def draw_window():
    wn.fill((0, 0, 0))

    draw_grid()

    player.draw(wn)
    food.draw(wn)

    score = font.render("Score: " + str(player.length - 3), 1, (240, 255, 0))
    wn.blit(score, (5, 5))

    pygame.display.update()


x_pos = 400
y_pos = 300
player = Snake((10, 10))
food = Apple((5, 10))
font = pygame.font.SysFont(" ", 30, True)
player.path = test.find_path(main_grid, player.grid_pos, food.pos, False)
run = True
while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player.direction != "down":
        player.direction = "up"
    elif keys[pygame.K_DOWN] and player.direction != "up":
        player.direction = "down"
    elif keys[pygame.K_LEFT] and player.direction != "right":
        player.direction = "left"
    elif keys[pygame.K_RIGHT] and player.direction != "left":
        player.direction = "right"

    if player.grid_pos == food.pos:
        player.length += 1
        food.new_pos()
        player.find_path()

    player.move()

    draw_window()
