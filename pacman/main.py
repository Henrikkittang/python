from layout.layout import Layout
from pacman.pacman import Pacman
from ghost.ghost import Blinky
import pygame
pygame.init()


def main():
    layout = Layout()
    window = pygame.display.set_mode((layout.width, layout.height))
    pacman = Pacman(125, 100, layout.sql)
    blinky = Blinky(350, 250, layout.sql)

   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        window.fill((0, 0, 0))
        
        layout.draw(window)
        
        pacman.move(layout)
        pacman.draw(window)

        blinky.move(layout, (pacman.x, pacman.y))
        blinky.draw(window)
        

        pygame.display.update()
main()