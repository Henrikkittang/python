import cProfile
import pstats
import pygame
pygame.init()

from layout.layout import Layout
from pacman.pacman import Pacman
from ghost.ghost import Blinky, Pinky, Inky,Clyde



class Game(object):
    def __init__(self):
        self._window = None
        self._clock = pygame.time.Clock()

        self._isInitialized = False

    def setup(self) -> None:
        raise NotImplementedError() 

    def update(self, dt: float) -> None:
        raise NotImplementedError()

    def makeWindow(self, width: int, height: int) -> None:
        self._window = pygame.display.set_mode((width, height))

    def init(self) -> None:
        self.setup()
        self._isInitialized = True

    def start(self) -> None:
        if not self._isInitialized:
            raise Exception('Game not initialized')
        if self._window == None:
            raise Exception('Window variable needs to be set')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self._window.fill((0, 0, 0))
            dt = self._clock.tick() / 1000

            self.update(dt)

            pygame.display.update()

    def _profile(self, functionName: str, maxLineNumber: int) -> None:
        filename = 'profile-'  + functionName[5:-2]
        cProfile.runctx(functionName, globals(), locals(), filename)

        with open(filename + '.txt', 'w') as file:
            profile = pstats.Stats('./' + filename, stream=file)
            profile.sort_stats('cumulative') 
            profile.print_stats(maxLineNumber)
            file.close()
        
    def profileSetup(self, maxLineNumber: int) -> None:
        self._profile('self.setup()', maxLineNumber)

    def profileUpdate(self, maxLineNumber: int) -> None:
        self._profile('self.start()', maxLineNumber)




class PacmanGame(Game):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.layout = Layout()

        self.makeWindow(self.layout.width, self.layout.height)
        self.pacman = Pacman(200, 300, self.layout.sql)
        self.ghosts = [
            Blinky((351, 251), (525,  25), self.layout.sql),
            Pinky ((350, 250), ( 25,  25), self.layout.sql),
            Inky  ((150, 275), (525, 525), self.layout.sql),
            Clyde ((351, 251), ( 25, 525), self.layout.sql),    
        ]

    def update(self, dt):
        self.layout.draw(self._window)
        self.pacman.move(self.layout, dt)
        self.pacman.checkColliding(self.layout)
        self.pacman.eat(self.layout)
        self.pacman.draw(self._window, dt)

        for ghost in self.ghosts:
            if isinstance(ghost, Inky):
                ghost.setBlinkyPosition(self.ghosts[0].getGridPos(self.ghosts[0].x, self.ghosts[0].y, self.layout.sql))
            ghost.move(self.layout, self.pacman, dt)
            ghost.draw(self._window, dt)



if __name__ == '__main__':
   

    pacman = PacmanGame()
    pacman.init()
    pacman.start()



