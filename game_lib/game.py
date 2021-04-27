import cProfile
import pstats
import pygame
pygame.init()

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

