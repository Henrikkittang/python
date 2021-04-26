from layout.layout import Layout
from pacman.pacman import Pacman
from ghost.ghostWrapper import GhostWrapper
import pygame
pygame.init()

if __name__ == '__main__':
    clock = pygame.time.Clock()
    layout = Layout()

    window = pygame.display.set_mode((layout.width, layout.height))
    pacman = Pacman(200, 300, layout.sql)
    ghostWrapper = GhostWrapper((351, 251), layout.sql)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        window.fill((0, 0, 0))
        dt = round(clock.tick() / 1000, 4)

        layout.draw(window)
        
        pacman.move(layout, dt)
        pacman.checkColliding(layout)
        pacman.eat(layout)
        pacman.eatPowerPellet(layout, ghostWrapper)
        pacman.eatGhost(layout, ghostWrapper)
        pacman.draw(window, dt)

        
        ghostWrapper.move(layout, pacman, dt)
        ghostWrapper.draw(window, dt)


        pygame.display.update()



