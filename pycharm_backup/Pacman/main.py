from math import sqrt
from math import ceil
from random import randint
import pygame
import json
import path_finding
pygame.init()

s_width = 720
s_height = 640
square_length = 20

wn = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Pacman")

clock = pygame.time.Clock()

with open("map.json") as f:
    map_data = json.load(f)

grid_config = map_data["blocks"]
grid_pellets = map_data["pellets"]


map_data["settings"]["s_width"] = s_width
map_data["settings"]["s_height"] = s_height
map_data["settings"]["square_length"] = square_length


with open("map.json", "w") as f:
    json.dump(map_data, f)


class Block(object):
    def __init__(self, grid_pos):
        self.grid_pos = grid_pos
        self.x = grid_pos[0] * square_length
        self.y = grid_pos[1] * square_length

    def draw(self, wn):
        pygame.draw.rect(wn, (164, 38, 255), (self.x + 1, self.y + 1, square_length - 1, square_length - 1))


class Pacman(object):
    def __init__(self, position):
        self.position = position
        self.x = position[0] * square_length + square_length//2
        self.y = position[1] * square_length + square_length//2
        self.speed = square_length//4
        self.direction = None
        self.score = 0

    def draw(self, wn):
        pygame.draw.rect(wn, (240, 255, 0), (
        self.x - square_length // 2 + 1, self.y - square_length // 2 + 1, square_length - 1, square_length - 1))
        pygame.draw.circle(wn, (255, 0, 0), (self.x, self.y), 2)

    def move(self, direction):
        self.direction = direction
        self.position = (self.x//square_length, self.y//square_length)

        if direction == "up":
            self.y -= self.speed
        elif direction == "down":
            self.y += self.speed
        elif direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed


class Ghost(object):
    def __init__(self, position, corner_pos, name=""):
        self.position = position
        self.x = self.position[0] * square_length + square_length//2
        self.y = self.position[1] * square_length + square_length//2
        self.target = corner_pos
        self.name = name
        self.speed = square_length//5
        self.corner_pos = corner_pos
        self.frightened_pos = (randint(7, 30), randint(4, 27))
        while main_grid[self.frightened_pos[1]][self.frightened_pos[0]] == 1:
            self.frightened_pos = (randint(7, 30), randint(4, 27))
        self.path = []
        self.next_tile = None
        self.prev_position = None
        self.direction = None
        self.prev_direction = None
        self.mode = "scatter"

    def draw(self, wn):
        if self.mode == "frightened":
            pygame.draw.rect(wn, (0, 0, 255), (self.x - square_length // 2 + 1, self.y - square_length // 2 + 1, square_length - 1, square_length - 1))
        else:
            if self.name == "blinky":
                pygame.draw.rect(wn, (255, 0, 0), ( self.x - square_length // 2 + 1, self.y - square_length // 2 + 1, square_length - 1, square_length - 1))
            elif self.name == "pinky":
                pygame.draw.rect(wn, (255, 0, 251), ( self.x - square_length // 2 + 1, self.y - square_length // 2 + 1, square_length - 1, square_length - 1))
            elif self.name == "inky":
                pygame.draw.rect(wn, (0, 255, 230), ( self.x - square_length // 2 + 1, self.y - square_length // 2 + 1, square_length - 1, square_length - 1))
            elif self.name == "clyde":
                pygame.draw.rect(wn, (255, 208, 0), ( self.x - square_length // 2 + 1, self.y - square_length // 2 + 1, square_length - 1, square_length - 1))
            else:
                pygame.draw.rect(wn, (51, 255, 0), ( self.x - square_length // 2 + 1, self.y - square_length // 2 + 1, square_length - 1, square_length - 1))

        # pygame.draw.circle(wn, (255, 0, 0), (self.x, self.y), 2)

    def pinky_target(self):
        tiles = 4
        check = True
        while check:
            if player.direction == "up":
                self.target = (player.position[0], player.position[1] - tiles)
            elif player.direction == "down":
                self.target = (player.position[0], player.position[1] + tiles)
            elif player.direction == "left":
                self.target = (player.position[0] - tiles, player.position[1])
            elif player.direction == "right":
                self.target = (player.position[0] + tiles, player.position[1])

            try:
                if main_grid[self.target[1]][self.target[0]] != 1:
                    check = False
            except IndexError:
                pass
            tiles -= 1

        if (self.target[0] < 7 or self.target[0] > 30) or (self.target[1] < 4 or self.target[1] > 27) or calc_distance(self.position, player.position) < 2:
            self.target = player.position

    def find_path(self):

        # Changes the target according the mode
        if self.mode == "chase":
            self.target = player.position
        elif self.mode == "scatter":
            self.target = self.corner_pos
        elif self.mode == "frightened":
            self.target = self.frightened_pos

        if self.mode == "chase" and self.name == "pinky":
            self.pinky_target()

        # Prevents lag
        # Instead of targeting pacman/the corner, the ghost target a position roughly in the middle of the grid
        if calc_distance(self.position, player.position) > 20 and self.mode == "chase":
            self.target = (18, 12)
        elif calc_distance(self.position, self.corner_pos) > 20 and self.mode == "scatter":
            self.target = (18, 12)

        # Finds the path to its target with the A* algorithm. Resets the previous position and direction
        self.path = path_finding.find_path(main_grid, enemy.position, self.target, False)
        self.prev_position = None
        self.prev_direction = self.direction

        if self.path == None:
            self.path = path_finding.find_path(main_grid, enemy.position, (18, 12), False)

    def move(self):
        self.position = (self.x//square_length, self.y//square_length)

        if self.direction != self.prev_direction or calc_distance(player.position, self.position) < 8:
            self.find_path()

        if self.name == "clyde" and calc_distance(player.position, self.position) < 6:
            self.mode = "scatter"
        elif self.name == "clyde" and calc_distance(player.position, self.position) > 12:
            self.mode = "chase"

        if self.position == self.corner_pos and self.mode == "scatter":
            self.target = player.position
            self.mode = "chase"

        if self.position == self.frightened_pos and self.mode == "frightened":
            self.frightened_pos = (randint(7, 30), randint(4, 27))
            while main_grid[self.frightened_pos[1]][self.frightened_pos[0]] == 1:
                self.frightened_pos = (randint(7, 30), randint(4, 27))
            self.find_path()

        if self.position != self.prev_position:
            self.prev_position = self.position
            if len(self.path) > 1:
                self.path.pop(0)
            else:
                self.target = player.position
                self.find_path()
            self.next_tile = self.path[0]

        if self.position[1] - 1 == self.next_tile[1]:
            self.y -= self.speed
            self.direction = "up"
        elif self.position[1] + 1 == self.next_tile[1]:
            self.y += self.speed
            self.direction = "down"
        elif self.position[0] - 1 == self.next_tile[0]:
            self.x -= self.speed
            self.direction = "left"
        elif self.position[0] + 1 == self.next_tile[0]:
            self.x += self.speed
            self.direction = "right"


class Pellet(object):
    def __init__(self, position):
        self.position = position
        self.x = position[0] * square_length + square_length // 2
        self.y = position[1] * square_length + square_length // 2

    def draw(self, wn):
        # pygame.draw.rect(wn, (240, 255, 0), (self.x - square_length // 2 + 1, self.y - square_length // 2 + 1, square_length - 1, square_length - 1))
        pygame.draw.circle(wn, (240, 255, 0), (self.x, self.y), 2)


class Square(object):
    def __init__(self, position, color=None):
        self.x = position[0] * 20
        self.y = position[1] * 20
        self.color = color

    def draw(self, wn):
        pygame.draw.rect(wn, self.color, (self.x + 1, self.y + 1, square_length-1, square_length-1))


def calc_distance(cor1, cor2):
    distance = sqrt( (cor1[0] - cor2[0])**2 + (cor1[1] - cor2[1])**2 )
    return distance


def draw_grid():
    """Draws the lines representing the grid"""
    for i in range(0, s_height, square_length):
        pygame.draw.line(wn, (255, 0, 0), (0, i), (s_width, i))

    for i in range(0, s_width, square_length):
        pygame.draw.line(wn, (255, 0, 0), (i, 0), (i, s_height))


def draw_window():
    """Draws all the objects on the screen"""
    wn.fill((0, 0, 0))

    # draw_grid()

    score = font.render("Score: " + str(player.score), 1, (240, 255, 0))
    wn.blit(score, (square_length + 5, square_length + 5))

    for i in blocks:
        i.draw(wn)

    for i in pellets:
        i.draw(wn)

    for s in squares:
       s.draw(wn)

    for i in enemies:
        i.draw(wn)

    player.draw(wn)

    pygame.display.update()


# Creating the grid according to the window and cell size
main_grid = []
for q in range(0, s_height//square_length):
    main_grid.append([])
    for t in range(0, s_width//square_length):
        main_grid[q].append(0)


blocks = []
pellets = []
# Adds the walls(1) and pellets(2) according to the json file/editor
for i in grid_config:
    x = i["coor"][0]
    y = i["coor"][1]
    main_grid[y][x] = 1
    blocks.append(Block((x, y)))

for i in grid_pellets:
    x = i["pellet"][0]
    y = i["pellet"][1]
    main_grid[y][x] = 2
    pellets.append(Pellet((x, y)))

# Adds the border around the whole screen
for i in range(0, len(main_grid[0])):
    main_grid[0][i], main_grid[-1][i] = 1, 1  # Top and bottom
    blocks.append(Block((i, (s_height // square_length) - 1)))
    blocks.append(Block((i, 0)))


for i in range(0, len(main_grid)):
    main_grid[i][0], main_grid[i][-1] = 1, 1  # Left and right
    blocks.append(Block(((s_width // square_length) - 1, i)))
    blocks.append(Block((0, i)))


enemies = [Ghost((18, 12), (30, 5), "blinky"), Ghost((18, 12), (7, 5), "pinky"), Ghost((18, 12), (30, 27), "inky"), Ghost((18, 12), (7, 27), "clyde")]
player = Pacman((18, 23))
scatter_count = 1200
font = pygame.font.SysFont(" ", 30, True)
run = True
while run:

    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Binds the keys to the player movement
    if keys[pygame.K_UP] or player.direction == "up":
        if main_grid[player.position[1]-1][player.position[0]] != 1:
            player.move("up")
    if keys[pygame.K_DOWN] or player.direction == "down":
        if main_grid[player.position[1]+1][player.position[0]] != 1:
            player.move("down")
    if keys[pygame.K_LEFT] or player.direction == "left":
        if main_grid[player.position[1]][player.position[0]-1] != 1:
            player.move("left")
    if keys[pygame.K_RIGHT] or player.direction == "right":
        if main_grid[player.position[1]][player.position[0]+1] != 1:
            player.move("right")

    # Checks if the pellets has been eaten by the player
    for i in pellets:
        if i.position == player.position:
            player.score += 10
            pellets.remove(i)
            main_grid[i.position[1]][i.position[0]] = 0

    # Checks if the enemies has caught the player
    frightened = False
    for enemy in enemies:
        enemy.position = (enemy.x//square_length, enemy.y//square_length)
        if player.position == enemy.position and enemy.mode != "frightened":
            run = False
        if enemy.mode == "frightened":
            frightened = True
            if player.position == enemy.position:
                player.score += 200
                enemy.position = enemy.corner_pos
                enemy.x = enemy.position[0] * square_length + square_length // 2
                enemy.y = enemy.position[1] * square_length + square_length // 2
                enemy.mode = "scatter"
                enemy.find_path()
        enemy.move()

    if keys[pygame.K_SPACE]:
        for i in enemies:
            i.mode = "frightened"

    # Random count for when the enemies enter scatter mode. increased chance each iteration
    if randint(0, scatter_count) == 1:
        for i in enemies:
            i.mode = "scatter"
        scatter_count = 1200
    if frightened == False:
        scatter_count -= 1

    squares = []
    for enemy in enemies:
        for i in enemy.path:
            squares.append(Square(i, (0, 255, 0)))

    draw_window()

