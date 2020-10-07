import a_star
import pygame
pygame.init()

s_width = 600
s_height = 600
scl = 20
wn = pygame.display.set_mode((s_width, s_height))

def make_grid():
    l_g_grid = []
    for i in range(0, s_height // scl):
        l_g_grid.append([])
        for j in range(0, s_width // scl):
            l_g_grid[i].append(0)
    return l_g_grid

def draw_lists(opens, closed):
    for node in opens:
        pos = node.position
        pygame.draw.rect(wn, (0, 255, 0), (pos[0]*scl, pos[1]*scl, scl, scl))
        f_value = font.render(str(node.f), 1, (0, 0, 0))
        wn.blit(f_value, (pos[0]*scl, pos[1]*scl))

    for pos in closed:
        pygame.draw.rect(wn, (255, 0, 0), (pos[0]*scl, pos[1]*scl, scl, scl))

def draw_lines():
    """Draws the lines representing the g_grid"""
    for i in range(0, s_height, scl):
        pygame.draw.line(wn, (255, 255, 255), (0, i), (s_width, i), 1)

    for i in range(0, s_width, scl):
        pygame.draw.line(wn, (255, 255, 255), (i, 0), (i, s_height))

def draw_grid():
    for i in range(len(g_grid)):
        for j in range(len(g_grid[i])):
            if g_grid[i][j] == 1:
                pygame.draw.rect(wn, (255, 255, 255), (j*scl, i*scl, scl, scl))

def draw_path():
    if path:
        for pos in path:
            pygame.draw.rect(wn, (60, 60, 255), (pos[0]*scl, pos[1]*scl, scl, scl))


g_grid = make_grid()
path = []
anmat = False
loop = True

op = [] # heap
os = set() # set
cs = set() # set
funcs = (op, os, cs)

font = pygame.font.SysFont(" ", 15, True)
update_time = 0
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    pygame.time.delay(update_time)

    wn.fill((0, 0, 0))

     # Right click
    if pygame.mouse.get_pressed() == (1, 0, 0):
        # Finds the g_grid position of the mouse
        cur_pos = pygame.mouse.get_pos()
        cur_pos = (cur_pos[0]//scl, cur_pos[1]//scl)

        if g_grid[cur_pos[1]][cur_pos[0]] == 0:
            g_grid[cur_pos[1]][cur_pos[0]] = 1
       
    if pygame.mouse.get_pressed() == (0, 0, 1):
        # Finds the g_grid position of the mouse
        cur_pos = pygame.mouse.get_pos()
        cur_pos = (cur_pos[0]//scl, cur_pos[1]//scl)

        if g_grid[cur_pos[1]][cur_pos[0]] == 1:
            g_grid[cur_pos[1]][cur_pos[0]] = 0
       

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        path = []
        (op, os, cs) = [[], set(),  set()] 
        anmat = True
        update_time = 50

    result = a_star.find_path(g_grid, (1, 1), (28, 28), (op, os, cs), anmat)

    if len(result) > 3 and anmat == True:
        path = result
        anmat = False
        (op, os, cs) = ([], set(), set())
        update_time  = 0
    elif len(result) == 3:
        # print(result[0])
        (op, os, cs) = result
   

    draw_lists(op, cs)
    draw_grid()
    draw_lines()
    draw_path()


    pygame.display.update()
