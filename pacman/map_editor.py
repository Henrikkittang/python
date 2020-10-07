from global_things import *
import json
import pygame
pygame.init()


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




