from layout.layout import Layout
from pacman.pacman import Pacman
from ghost.ghost import Blinky, Pinky, Inky,Clyde
import pygame
pygame.init()


if __name__ == '__main__':
    clock = pygame.time.Clock()

    layout = Layout()

    window = pygame.display.set_mode((layout.getWidth(), layout.getHeight()))

    pacman = Pacman(200, 300, layout.getSql())


    ghosts = [
        Pinky ((350, 250), (25 , 25 ), layout.getSql()),
        Blinky((351, 251), (525, 25 ), layout.getSql()),
        Inky  ((150, 275), (525, 525), layout.getSql()),
        Clyde ((351, 251), (25 , 525), layout.getSql()),    
    ]

    pinky  = Pinky ((350, 250), (25 , 25 ), layout.getSql())
    blinky = Blinky((351, 251), (525, 25 ), layout.getSql())
    inky   = Inky  ((150, 275), (525, 525), layout.getSql())
    clyde  = Clyde ((351, 251), (25 , 525), layout.getSql())

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
        pacman.draw(window, dt)

        for ghost in ghosts:
            if isinstance(ghost, Inky):
                ghost.setBlinkyPosition(blinky.getGridPos(blinky.x, blinky.y, layout.getSql()))
            ghost.move(layout, pacman, dt)
            ghost.draw(window)


        pygame.display.update()

