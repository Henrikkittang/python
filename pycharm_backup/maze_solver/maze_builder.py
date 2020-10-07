import json
import pygame
pygame.init()

with open("maze_layout.json") as f:
    data = json.load(f)

grid_blocks = data["blocks"]

s_height = 600
s_width = 600
square_length = 20

data["screen"]["height"] = s_height
data["screen"]["width"] = s_width
data["screen"]["square_length"] = square_length

with open("maze_layout.json", "w") as f:
    json.dump(data, f)

wn = pygame.display.set_mode((s_width, s_height))

print()
print("Place block: SPACE")
print("Toggle grid: G")
print("Place start node: S")
print("Place end node: e")

state_x = 0
state_y = 0

display_grid = True


class Node(object):
    def __init__(self, grid_pos, state):
        self.grid_pos = grid_pos
        self.x = grid_pos[0] * square_length
        self.y = grid_pos[1] * square_length
        self.state = state

    def draw(self, wn):
        if self.state == "start":
            pygame.draw.rect(wn, (0, 255, 0), (self.x + 1, self.y + 1, square_length - 1, square_length - 1))
        elif self.state == "end":
            pygame.draw.rect(wn, (255, 0, 0), (self.x + 1, self.y + 1, square_length - 1, square_length - 1))


class Block(object):
    def __init__(self, grid_pos):
        self.grid_pos = grid_pos
        self.x = grid_pos[0] * square_length
        self.y = grid_pos[1] * square_length

    def draw(self, wn):
        pygame.draw.rect(wn, (40, 60, 235), (self.x + 1, self.y + 1, square_length - 1, square_length - 1))


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

    marker_pos = font.render("Position: " + str(state_x) + ", " + str(state_y), 1, (0, 255, 0))
    wn.blit(marker_pos, (5, 5))

    pygame.draw.rect(wn, (0, 255, 0),
                    ((s_width // len(grid[0])) * state_x, (s_height // len(grid)) * state_y,
                    s_width // len(grid[0]), (s_height // len(grid))), 2)

    start_node.draw(wn)
    end_node.draw(wn)

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


start_node = Node(data["node"]["start_node"], "start")
end_node = Node(data["node"]["end_node"], "end")

blocks = []
pellets = []
delay_count = 0
font = pygame.font.SysFont("comicsans", 30, True)
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("maze_layout.json", "w") as f:
                json.dump(data, f)
            run = False

    with open("maze_layout.json") as f:
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

    if keys[pygame.K_s]:
        data["node"]["start_node"] = [state_x, state_y]
    if keys[pygame.K_e]:
        data["node"]["end_node"] = [state_x, state_y]

    start_node = Node(data["node"]["start_node"], "start")
    end_node = Node(data["node"]["end_node"], "end")

    if keys[pygame.K_g]:
        if display_grid == True:
            display_grid = False
        else:
            display_grid = True

    with open("maze_layout.json", "w") as f:
        json.dump(data, f)

    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == 1:
                blocks.append(Block((x, y)))

    draw_window()