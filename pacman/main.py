from layout.layout import Layout
from pacman.pacman import Pacman
from ghost.ghost import Blinky, Pinky, Clyde
import pygame
pygame.init()


if __name__ == '__main__':
    clock = pygame.time.Clock()

    layout = Layout()

    window = pygame.display.set_mode((layout.getWidth(), layout.getHeight()))

    pacman = Pacman(200, 300, layout.getSql())

    pinky = Pinky(350, 250, layout.getSql())
    blinky = Blinky(351, 251, layout.getSql())
    clyde = Clyde(351, 251, layout.getSql())

    clyde.corner = clyde.getGridPos(clyde.x, clyde.y, layout.getSql())

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

        # blinky.move(layout, pacman, dt)
        # blinky.draw(window)
        # pinky.move(layout, pacman, dt)
        # pinky.draw(window)
        # clyde.move(layout, pacman, dt)
        # clyde.draw(window)

        pygame.display.update()
