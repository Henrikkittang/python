import json
import pygame
pygame.init()


class MapEditor(object):
    def __init__(self, filename, contentType):
        self._filename = filename
                
        self._config = self._readJsonFile()['config']
        self._width  = self._config['screen_w']
        self._height = self._config['screen_h']
        self._sql    = self._config['square_length']

        self._font   = pygame.font.SysFont(" ", 30, True)
        self._contentType = contentType
        self._content = self._readJsonFile()[contentType]

    def getWidth(self): return self._width
    def getHeight(self): return self._height
    def getSql(self): return self._sql
    def getFont(self): return self._font

    def _readJsonFile(self):
        with open('layout/' + self._filename + '.json') as f:
            data = json.load(f)
            f.close()
        return data

    def _writeJsonFile(self, data):
        with open('layout/' + self._filename + '.json', 'w') as f:
            json.dump(data, f)
            f.close()
        
        
    def displayGrid(self, wn):
        """Draws the lines representing the grid"""
    
        for i in range(self._sql, self._width, self._sql):
            pygame.draw.line(wn, (255, 0, 0), (i, 0), (i, self._height))
    
        for i in range(self._sql, self._height, self._sql):
            pygame.draw.line(wn, (255, 0, 0), (0, i), (self._width, i), 1)


    def toggleContent(self, row, column):
        for idx, i in enumerate(self._content):
            if [row, column] == i:
                self._content.pop(idx)
                return
        self._content.append([row, column])
    
    def draw(self, wn):

        if self._contentType == 'wallLayout':
            color = (40, 60, 235)
            for pos in self._content:
                pygame.draw.rect(wn, color, (pos[0]*self._sql, pos[1]*self._sql, self._sql, self._sql))

        elif self._contentType == 'pelletLayout':
            color = (255,255,0)
            for pos in self._content:
                pygame.draw.circle(wn, color,(pos[0]*self._sql + self._sql//2, pos[1]*self._sql + self._sql//2) ,3)
            
        elif self._contentType == 'powerPelletLayout':
            color = (180,180,255)
            for pos in self._content:
                pygame.draw.circle(wn, color,(pos[0]*self._sql + self._sql//2, pos[1]*self._sql + self._sql//2) , 6)
                

    def saveLayout(self):
        data = self._readJsonFile()
        data[self._contentType] = self._content
        self._writeJsonFile(data)

class Marker():
    def __init__(self, sql):
        self.sql = sql
        self.x = 0
        self.y = 0
        self.color = (0, 255, 0)

    def draw(self, wn, font):
        drawPosX, drawPosY = self.getPixelPos()

        pygame.draw.line(wn, self.color, (drawPosX, drawPosY), (drawPosX +  self.sql, drawPosY))
        pygame.draw.line(wn, self.color, (drawPosX +  self.sql, drawPosY), (drawPosX +  self.sql, drawPosY +  self.sql))
        pygame.draw.line(wn, self.color, (drawPosX +  self.sql, drawPosY +  self.sql), (drawPosX, drawPosY +  self.sql))
        pygame.draw.line(wn, self.color, (drawPosX, drawPosY +  self.sql), (drawPosX, drawPosY))

        pygame.draw.rect(wn, self.color, (self.x* self.sql, self.y* self.sql,  self.sql,  self.sql), 3)

        coor = font.render(str(drawPosX) + ', ' + str(drawPosY), 1, (240, 255, 0))
        wn.blit(coor, (5, 5))

    def getPixelPos(self) -> list:
        return (self.x* self.sql, self.y* self.sql)

    def getInput(self, wallEditor, pelletEditor, powerPelletEditor):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += 1
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= 1
        if keys[pygame.K_DOWN]:
            self.y += 1
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= 1

        if keys[pygame.K_1]:
            wallEditor.toggleContent(self.x, self.y)
            wallEditor.saveLayout()
        elif keys[pygame.K_2]:
            pelletEditor.toggleContent(self.x, self.y)
            pelletEditor.saveLayout()
        elif keys[pygame.K_SPACE]:
            powerPelletEditor.toggleContent(self.x, self.y)
            powerPelletEditor.saveLayout()
 
if __name__ == '__main__':    
    wallEditor = MapEditor('map', 'wallLayout') 
    pelletEditor = MapEditor('map', 'pelletLayout') 
    powerPelletEditor = MapEditor('map', 'powerPelletLayout') 

    marker = Marker(wallEditor.getSql())

    wn = pygame.display.set_mode(( wallEditor.getWidth(),  wallEditor.getHeight()))

    
    while True:
        wn.fill((0, 0, 0))
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        wallEditor.draw(wn)
        powerPelletEditor.draw(wn)
        pelletEditor.draw(wn)

        marker.draw(wn, wallEditor.getFont())
        marker.getInput(wallEditor, pelletEditor, powerPelletEditor)

        pygame.display.update()



