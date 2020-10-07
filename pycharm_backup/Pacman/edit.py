import json
import pygame
pygame.init()

with open("map.json") as f:
    data = json.load(f)
    print(type(data))

grid_blocks = data["blocks"]
grid_pellets = data["pellets"]

s_height = data["settings"]["s_height"]
s_width = data["settings"]["s_width"]
square_length = data["settings"]["square_length"]

wn = pygame.display.set_mode((s_width, s_height))

print()
print("Place block: SPACE")
print("Place pellet: E")
print("Toggle grid: G")

state_x = 0
state_y = 0

display_grid = True


class Block(object):
    def __init__(self, grid_pos):
        self.grid_pos = grid_pos
        self.x = grid_pos[0] * square_length
        self.y = grid_pos[1] * square_length

    def draw(self, wn):
        pygame.draw.rect(wn, (40, 60, 235), (self.x + 1, self.y + 1, square_length - 1, square_length - 1))


class Pellet(object):
    def __init__(self, position):
        self.position = position
        self.x = position[0] * square_length + square_length // 2
        self.y = position[1] * square_length + square_length // 2

    def draw(self, wn):
        # pygame.draw.rect(wn, (240, 255, 0), (self.x - square_length // 2 + 1, self.y - square_length // 2 + 1, square_length - 1, square_length - 1))
        pygame.draw.circle(wn, (240, 255, 0), (self.x, self.y), 2)


def draw_grid():
    for i in range(0, s_height, square_length):
        pygame.draw.line(wn, (255, 0, 0), (0, i), (s_width, i))

    for i in range(0, s_width, square_length):
        pygame.draw.line(wn, (255, 0, 0), (i, 0), (i, s_height))


def draw_window():
    wn.fill((0, 0, 0))

    if display_grid == True:
        draw_grid()

    for i in blocks:
        i.draw(wn)
    blocks.clear()

    for i in pellets:
        i.draw(wn)
    pellets.clear()

    marker_pos = font.render("Position: " + str(state_x) + ", " + str(state_y), 1, (0, 255, 0))
    wn.blit(marker_pos, (5, 5))

    pygame.draw.rect(wn, (0, 255, 0),
                    ((s_width // len(grid[0])) * state_x, (s_height // len(grid)) * state_y,
                    s_width // len(grid[0]), (s_height // len(grid))), 2)

    pygame.display.update()


grid = []
for q in range(0, s_height//square_length):
    grid.append([])
    for t in range(0, s_width//square_length):
        grid[q].append(0)


for i in grid_blocks:
    x = i["coor"][0]
    y = i["coor"][1]
    grid[y][x] = 1

for i in grid_pellets:
    x = i["pellet"][0]
    y = i["pellet"][1]
    grid[y][x] = 2

blocks = []
pellets = []
delay_count = 0
font = pygame.font.SysFont("comicsans", 30, True)
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("map.json", "w") as f:
                json.dump(data, f)
            run = False

    with open("map.json") as f:
        data = json.load(f)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and state_x < (len(grid[0]) - 1):
        state_x += 1
    if keys[pygame.K_LEFT] and state_x > 0:
        state_x -= 1
    if keys[pygame.K_DOWN] and state_y < (len(grid) - 1):
        state_y += 1
    if keys[pygame.K_UP] and state_y > 0:
        state_y -= 1

    if keys[pygame.K_SPACE] and grid[state_y][state_x] != 2:
        if grid[state_y][state_x] == 0:
            grid[state_y][state_x] = 1
            data["blocks"].append({"coor": [state_x, state_y]})
        else:
            grid[state_y][state_x] = 0
            data["blocks"].remove({"coor": [state_x, state_y]})

    elif keys[pygame.K_e] and grid[state_y][state_x] != 1:
        if grid[state_y][state_x] == 0:
            grid[state_y][state_x] = 2
            data["pellets"].append({"pellet": [state_x, state_y]})
        else:
            grid[state_y][state_x] = 0
            data["pellets"].remove({"pellet": [state_x, state_y]})

    if keys[pygame.K_g]:
        if display_grid == True:
            display_grid = False
        else:
            display_grid = True

    with open("map.json", "w") as f:
        json.dump(data, f)

    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == 1:
                blocks.append(Block((x, y)))
            elif grid[y][x] == 2:
                pellets.append(Pellet((x, y)))

    draw_window()