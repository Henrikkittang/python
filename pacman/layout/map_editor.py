import json
import pygame
pygame.init()

def readJsonFile(filename):
    with open('layout/' + filename + '.json') as f:
        data = json.load(f)
        f.close()
    return data

def writeJsonFile(filename, data):
    with open('layout/' + filename + '.json', 'w') as f:
        json.dump(data, f)
        f.close()

g_config = readJsonFile('map')['config']
g_width = g_config['screen_w']
g_height = g_config['screen_h']
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


def saveLayout(wallLayout):
    data = readJsonFile('map')
    data['wallLayout'] = wallLayout

    writeJsonFile('map', data)

class Marker():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 255, 0)

    def draw(self, wn):
        drawPosX = self.x * g_sql
        drawPosY = self.y * g_sql
        pygame.draw.line(wn, self.color, (drawPosX, drawPosY), (drawPosX + g_sql, drawPosY))
        pygame.draw.line(wn, self.color, (drawPosX + g_sql, drawPosY), (drawPosX + g_sql, drawPosY + g_sql))
        pygame.draw.line(wn, self.color, (drawPosX + g_sql, drawPosY + g_sql), (drawPosX, drawPosY + g_sql))
        pygame.draw.line(wn, self.color, (drawPosX, drawPosY + g_sql), (drawPosX, drawPosY))

        pygame.draw.rect(wn, self.color, (self.x*g_sql, self.y*g_sql, g_sql, g_sql), 3)

        coor = g_font.render(str(drawPosX) + ', ' + str(drawPosY), 1, (240, 255, 0))
        wn.blit(coor, (5, 5))

    def getInput(self, wallLayout):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += 1
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= 1
        if keys[pygame.K_DOWN]:
            self.y += 1
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= 1

        if keys[pygame.K_SPACE]:
            for idx, i in  enumerate(wallLayout):
                if [self.x, self.y] == i:
                    wallLayout.pop(idx)
                    return
            wallLayout.append([self.x, self.y])


def main():
    
    wn = pygame.display.set_mode((g_width, g_height))
    wallLayout = readJsonFile('map')['wallLayout']

    
    marker = Marker(2, 2)
    while True:
        wn.fill((0, 0, 0))
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        for wall in wallLayout:
            drawWall(wn,wall)

        marker.getInput(wallLayout)
        marker.draw(wn)

        saveLayout(wallLayout)

        pygame.display.update()


main()




