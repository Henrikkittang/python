from math import sqrt
import pygame
import json
pygame.init()


with open("maze_layout.json") as f:
    data = json.load(f)

screen = data["screen"]

s_width = screen["width"]
s_height = screen["height"]
square_length = screen["square_length"]


wn = pygame.display.set_mode((s_width, s_height))
grid_config = data["blocks"]


class Block(object):
    def __init__(self, grid_pos, state):
        self.grid_pos = grid_pos
        self.x = grid_pos[0] * square_length
        self.y = grid_pos[1] * square_length
        self.state = state

    def draw(self, wn):
        color = (0, 0, 255)
        if self.state == "open":
            color = (0, 255, 0)
        elif self.state == "closed":
            color = (255, 0, 0)
        elif self.state == "wall":
            color = (255, 255, 0)
        elif self.state == "start" or self.state == "end":
            color = (0, 0, 255)
        pygame.draw.rect(wn, color, (self.x + 1, self.y + 1, square_length - 1, square_length - 1))


def draw_grid():
    for i in range(0, s_height, square_length):
        pygame.draw.line(wn, (255, 255, 255), (0, i), (s_width, i))

    for i in range(0, s_width, square_length):
        pygame.draw.line(wn, (255, 255, 255), (i, 0), (i, s_height))


positions = []


def draw_graphics(open_nodes, closed_nodes):
    wn.fill((0, 0, 0))
    blocks = []
    for i in open_nodes:
        blocks.append(Block(i.position, "open"))

    for i in closed_nodes:
        blocks.append(Block(i.position, "closed"))

    for block in blocks:
        block.draw(wn)

    for wall in walls:
        wall.draw(wn)

    for i in positions:
        i.draw(wn)

    start_node.draw(wn)
    end_node.draw(wn)

    draw_grid()

    pygame.display.update()


class Node(object):
    def __init__(self, position=None, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # distance from the starting node
        self.h = 0  # distance from end node
        self.f = 0  # h_cost + g_cost


def find_path(grid, start_pos, end_pos, diagonal=True):
    def calc_children(node):
        cur_pos = node.position
        children_pos = []
        for t in range(-1, 2):
            for q in range(-1, 2):
                if diagonal == False:
                    if abs(t) == abs(q):
                        continue

                if not (t == 0 and q == 0):
                    if grid[cur_pos[1] + t][cur_pos[0] + q] != 1:
                        pos = (cur_pos[0] + q, cur_pos[1] + t)
                        children_pos.append(pos)
        return children_pos

    open_nodes = []
    closed_nodes = []
    cur_node = Node(start_pos)
    end_node = Node(end_pos)
    open_nodes.append(cur_node)

    while cur_node.position != end_node.position:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Finds the open node with the lowest f-cost
        lowest_f = 1000
        for n in open_nodes:
            if n.f < lowest_f:
                cur_node = n
                lowest_f = n.f

        # if there aren't any paths, then exit and return none
        if len(open_nodes) == 0:
            return None

        # Finds the children of the current_node. Removes current_node from open and adds it to the closed
        children = calc_children(cur_node)
        open_nodes.remove(cur_node)
        closed_nodes.append(cur_node)

        # Loops over the current node`s children
        for pos in children:

            # if the child is in the closed list, then continue to the next child
            break_loop = False
            for closed_node in closed_nodes:
                if pos == closed_node.position:
                    break_loop = True
                    break
            if break_loop == True:
                continue

            child = Node(pos)

            # Sets the costs and the parent for the child
            child.g = cur_node.g + 1
            child.h = sqrt((end_node.position[0] - child.position[0])**2 + (end_node.position[1] - child.position[1])**2)
            child.f = child.g + child.h
            child.parent = cur_node

            # if the child is already in the open list, then continue to the next child
            break_loop = False
            for open_node in open_nodes:
                if child.position == open_node.position:
                    break_loop = True
                    break
            if break_loop == True:
                continue

            open_nodes.append(child)

        draw_graphics(open_nodes, closed_nodes)

        pygame.time.delay(0)

    print(cur_node.g)

    while cur_node != None:
        positions.append(Block(cur_node.position, "start"))
        cur_node = cur_node.parent

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_graphics(open_nodes, closed_nodes)


walls = []
main_grid = []
for q in range(0, s_height//square_length):
    main_grid.append([])
    for t in range(0, s_width//square_length):
        main_grid[q].append(0)

for i in grid_config:
    x = i["coor"][0]
    y = i["coor"][1]
    main_grid[y][x] = 1
    walls.append(Block((x, y), "wall"))

start_node = Block(data["node"]["start_node"], "start")
end_node = Block(tuple(data["node"]["end_node"]), "end")

find_path(main_grid, start_node.grid_pos, end_node.grid_pos, True)
