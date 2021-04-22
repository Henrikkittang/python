from layout.layout import Layout
from pacman.pacman import Pacman
from ghost.ghost import Blinky, Pinky, Inky,Clyde
import pygame
pygame.init()

if __name__ == '__main__':
    clock = pygame.time.Clock()
    layout = Layout()

    window = pygame.display.set_mode((layout.width, layout.height))
    pacman = Pacman(200, 300, layout.sql)
    ghosts = [
        Blinky((351, 251), (525, 25 ), layout.sql),
        Pinky ((350, 250), (25 , 25 ), layout.sql),
        Inky  ((150, 275), (525, 525), layout.sql),
        Clyde ((351, 251), (25 , 525), layout.sql),    
    ]

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        window.fill((0, 0, 0))
        dt = clock.tick() / 1000

        layout.draw(window)
        
        pacman.move(layout, dt)
        pacman.checkColliding(layout)
        pacman.eat(layout)
        if pacman.eatPowerPellet(layout):
            [ghost.setModeFrightend() for ghost in ghosts]
        [pacman.eatGhost(ghost, layout) for ghost in ghosts]        
        pacman.draw(window, dt)

        for ghost in ghosts:
            if isinstance(ghost, Inky):
                ghost.setBlinkyPosition(ghosts[0].getGridPos(ghosts[0].x, ghosts[0].y, layout.sql))
            ghost.move(layout, pacman, dt)
            ghost.draw(window, dt)


        pygame.display.update()



