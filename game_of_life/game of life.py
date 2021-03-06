import copy_file
from random import randint
import pygame
pygame.init()

screen_width = 800
screen_height = 600

wn = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game of life")

clock = pygame.time.Clock()

class square(object):
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    def draw(self, wn):
        if self.state == 1:
            pygame.draw.rect(wn, (255, 255, 255), (self.x, self.y, (screen_width//len(states[0])), (screen_height//len(states))))
        elif self.state == 0:
            pygame.draw.rect(wn, (0, 0, 0), (self.x, self.y, (screen_width//len(states[0])), (screen_height//len(states))))


states = []
states_next_gen = []

"""Set number of cells""" 
for y in range(0, 50):
    states.append([])
    states_next_gen.append([])
    for x in range(0, 50):
        states[y].append(0)
        states_next_gen[y].append(0)


"""Generates random states for each cell"""
for y in range(0, len(states)):
    for x in range(0, len(states[0])):
        if y == 0 or x == 0 or y == len(states) or x == len(states[0]):
            states[y][x] = 0
        states[y][x] = randint(0, 1)
    
squares = []


def draw_window():
    wn.fill((0, 0, 0))
    for square in squares:
        square.draw(wn)
    squares.clear()
    live = font.render("Live cells: " + str(live_cells), 1, (255, 0, 0))
    generations = font.render("Generations: " + str(turns), 1, (255, 0, 0))
    wn.blit(live, (5, 5))
    wn.blit(generations, ((screen_width - 220), 5))
    pygame.display.update()


xs = []
ys = []
live_cells = 0
font = pygame.font.SysFont("comicsans", 30, True)
neighbours = 0
turns = 0
run = True
while run:
    clock.tick(80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            copy_file.copy()
            run = False
            
    last_gen = live_cells
    live_cells = 0

    """Checks the neighbours of each cell """
    for y in range(1, len(states) - 1):
        for x in range(1, len(states[0]) - 1):
            neighbours += states[y-1][x]  # Cell above
            neighbours += states[y+1][x]  # Cell below
            neighbours += states[y][x-1]  # Cell to the left
            neighbours += states[y][x+1]  # Cell to the right
            neighbours += states[y-1][x-1]  # Cell top left corner
            neighbours += states[y-1][x+1]  # cell to top right corner
            neighbours += states[y+1][x-1]  # Cell to lower left corner
            neighbours += states[y+1][x+1]  # Cell to lower right corner

            if neighbours < 2:
                states_next_gen[y][x] = 0
            if neighbours > 3:
                states_next_gen[y][x] = 0
            if neighbours == 3:
                states_next_gen[y][x] = 1

            neighbours = 0

    for y in range(0, len(states)):
        for x in range(0, len(states[0])):
            states[y][x] = states_next_gen[y][x]

    """Displays the cells on the screen"""
    for y in range(0, len(states)):
        for x in range(0, len(states[0])):
            s_1 = (screen_width // len(states[0])) * x
            s_2 = (screen_height // len(states)) * y
            squares.append(square(s_1, s_2, states[y][x]))


    for y in range(0, len(states)):
        for x in range(0, len(states[0])):
            if states[y][x] == 1:
                live_cells += 1

    draw_window()
    
    if live_cells != last_gen:
        turns += 1
        with open("cells_data.txt", "w") as f:
            for i in range(0, len(xs)):
                f.write(str(xs[i]) + "," + str(ys[i]))
                f.write("\n")

            
    xs.append(turns)
    ys.append(live_cells)


