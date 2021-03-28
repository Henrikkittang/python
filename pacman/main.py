from layout.layout import Layout
from pacman.pacman import Pacman
from ghost.ghost import Blinky
import pygame
pygame.init()


if __name__ == '__main__':
    clock = pygame.time.Clock()
    layout = Layout()
    window = pygame.display.set_mode((layout.getWidth(), layout.getHeight()))
    pacman = Pacman(125, 100, layout.getSql())
    blinky = Blinky(350, 250, layout.getSql())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        window.fill((0, 0, 0))
        dt = clock.tick() / 1000

        layout.draw(window)
        
        pacman.move(layout, dt)
        pacman.checkColliding(layout)
        pacman.draw(window)

        blinky.move(layout, (pacman.x, pacman.y), dt)
        blinky.draw(window)
        

        pygame.display.update()
