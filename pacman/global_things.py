import json
import pygame
pygame.init()

def readJsonFile(filename):
    with open(filename + '.json') as f:
        data = json.load(f)
        f.close()
    return data

def writeJsonFile(filename, data):
    with open(filename + '.json', 'w') as f:
        json.dump(data, f)
        f.close()

g_config = readJsonFile('map')['config']
g_width = g_config['screen_w']
g_height = g_config['screen_w']
g_sql = g_config['square_length']
g_font = pygame.font.SysFont(" ", 30, True)

   
def displayGrid(wn):
    """Draws the lines representing the grid"""
   
    for i in range(g_sql, g_width, g_sql):
        pygame.draw.line(wn, (255, 0, 0), (i, 0), (i, g_height))
   
    for i in range(g_sql, g_height, g_sql):
        pygame.draw.line(wn, (255, 0, 0), (0, i), (g_width, i), 1)

def drawWall(wn, wallPos):
    color = (40, 60, 235)
    # print(wn, color, (wallPos[0]*g_sql, wallPos[1]*g_sql, g_sql, g_sql))
    pygame.draw.rect(wn, color, (wallPos[0]*g_sql, wallPos[1]*g_sql, g_sql, g_sql))


