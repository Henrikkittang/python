from random import randint
import pygame
pygame.init()

s_width = 400
s_height = 400
square_length = 20
num_mines = 80
wn = pygame.display.set_mode((s_width, s_height))

flag_img = pygame.image.load("flag.png")
mine_img = pygame.image.load("mine.png")


class Tile(object):
    def __init__(self, grid_pos, tile_type):
        self.grid_pos = grid_pos
        self.x = grid_pos[0] * square_length
        self.y = grid_pos[1] * square_length
        self.tile_type = tile_type

    def draw(self, wn):
        if self.tile_type == "block":
            pygame.draw.rect(wn, (208, 214, 227), (self.x + 2, self.y + 2, square_length - 2, square_length - 2))
        elif self.tile_type == "flag":
            pygame.draw.rect(wn, (208, 214, 227), (self.x + 2, self.y + 2, square_length - 2, square_length - 2))
            wn.blit(flag_img, (self.x + 1, self.y + 1))
        elif self.tile_type == "mine":
            wn.blit(mine_img, (self.x + 1, self.y + 1))


def find_open(start_pos):
    """Finds the blank tiles around a open tile"""
    def calc_children(parent_pos):
        children_pos = []
        for t in range(-1, 2):
            for q in range(-1, 2):
                if abs(t) == abs(q):
                    continue

                if not (t == 0 and q == 0):
                    try:
                        if mines[parent_pos[1] + t][parent_pos[0] + q] == 0:
                            pos = (parent_pos[0] + q, parent_pos[1] + t)
                            children_pos.append(pos)
                    except IndexError:
                        pass
        return children_pos

    open_pos = []
    closed_pos = []
    free_pos = []
    open_pos.append(start_pos)
    loop = True
    while loop:
        try:
            cur_pos = open_pos[0]
            children = calc_children(cur_pos)
        except:
            loop = False
            break

        if len(children) == 0:
            loop = False

        closed_pos.append(cur_pos)
        open_pos.remove(cur_pos)

        for child in children:
            cont = False
            for i in closed_pos:
                if child == i:
                    cont = True
                    break
            if cont == True:
                continue


            for i in open_pos:
                if child == i:
                    cont = True
                    break
            if cont == True:
                continue

            open_pos.append(child)
            free_pos.append(child)

    return free_pos


def draw_grid():
    """Draws the lines representing the grid"""
    for i in range(0, s_height, square_length):
        pygame.draw.line(wn, (255, 255, 255), (0, i), (s_width, i), 2)

    for i in range(0, s_width, square_length):
        pygame.draw.line(wn, (255, 255, 255), (i, 0), (i, s_height), 2)


def draw_window():
    wn.fill((100, 100, 120))

    draw_grid()

    # Draws the letters
    for key, val in mine_count_pos.items():
        if val != 0:
            pos = ((key[0] * square_length) + 5, (key[1] * square_length) + 5)
            text = font.render(str(val), 1, colors[val])
            wn.blit(text, pos)

    # Draws the mines
    for i in mine_obj:
        i.draw(wn)

    for i in tiles:
        i.draw(wn)
    tiles.clear()

    pygame.display.update()


def calc_mine_count(cur_pos):
    """Counts the amount of mine mines around a tile. Imagine minecraft crafting table"""
    mine_count = 0
    if mines[cur_pos[1]][cur_pos[0]] == -1:
        return None
    for t in range(-1, 2):
        for q in range(-1, 2):

            if not (t == 0 and q == 0):
                try:
                    if mines[cur_pos[1] + t][cur_pos[0] + q] == -1:
                        mine_count += 1
                except IndexError:
                    pass

    return mine_count


"""Instead of randomizing the state of each tile, then randomize the mines position and while loop until a free 
cell is found. This mines that the grid will always have the same amounts of mines"""

# Makes the main and mine
mines = []
main_grid = []
for q in range(0, s_height//square_length):
    main_grid.append([])
    mines.append([])
    for t in range(0, s_width//square_length):
        mines[q].append(0)
        main_grid[q].append(1)

# Sets random positions for each mine. If the position is already taken, then randomize a new one
for i in range(0, num_mines):
    pos = (randint(0, (s_width // square_length) - 1), randint(0, (s_height // square_length) - 1))
    while mines[pos[1]][pos[0]] == -1:
        pos = (randint(1, (s_width//square_length) - 1), randint(1, (s_height//square_length) - 1))
    mines[pos[1]][pos[0]] = -1

# Adds the mines to the draw list (mine_obj) and the numbers list (mine_count_pos)
mine_count_pos = {}
mine_obj = []
for y in range(0, len(mines)):
    for x in range(0, len(mines[y])):
        if calc_mine_count((x, y)) != None:
            mine_count_pos[(x, y)] = calc_mine_count((x, y))
        else:
            mine_obj.append(Tile((x, y), "mine"))

# Adds the number of mines in the in each tile of the mine grid. Note: I don't know why i did this
for key, val in mine_count_pos.items():
    mines[key[1]][key[0]] = val


tiles = []
font = pygame.font.SysFont("comicsans", 23, True)
colors = {1: (0, 164, 255), 2: (0, 255, 0), 3: (255, 0, 0), 4:  (0, 0, 255), 5: (246, 124, 124), 6: (0, 255, 191)}
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(0, len(main_grid)):
        for q in range(0, len(main_grid[i])):
            if main_grid[i][q] == 1:
                tiles.append(Tile((q, i), "block"))
            if main_grid[i][q] == 2:
                tiles.append(Tile((q, i), "flag"))

    # Right click
    if pygame.mouse.get_pressed() == (1, 0, 0):
        # Finds the grid position of the mouse
        cur_pos = pygame.mouse.get_pos()
        cur_pos = (cur_pos[0]//square_length, cur_pos[1]//square_length)

        # If the chosen tile dosent have a flag, then open it
        if main_grid[cur_pos[1]][cur_pos[0]] != 2:
            main_grid[cur_pos[1]][cur_pos[0]] = 0

        # Opens all the blank tiles
        open_tiles = find_open(cur_pos)
        for pos in open_tiles:
            for cur_block in tiles:
                if pos == cur_block.grid_pos and cur_block.tile_type == "block":
                    main_grid[pos[1]][pos[0]] = 0

        # Checks if the chosen tile is a bomb
        for i in mine_obj:
            if cur_pos == i.grid_pos:
                print("oooouf")

    # Left click
    elif pygame.mouse.get_pressed() == (0, 0, 1):
        # Finds the grid position of the mouse
        cur_pos = pygame.mouse.get_pos()
        cur_pos = (cur_pos[0] // square_length, cur_pos[1] // square_length)

        # Places/removes flag
        if main_grid[cur_pos[1]][cur_pos[0]] == 1:
            main_grid[cur_pos[1]][cur_pos[0]] = 2
        elif main_grid[cur_pos[1]][cur_pos[0]] == 2:
            main_grid[cur_pos[1]][cur_pos[0]] = 1
        pygame.time.delay(55)

    draw_window()
