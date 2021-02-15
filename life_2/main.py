from random import randint
import time
import pygame
pygame.init()

pygame.display.set_caption("Game of life")
clock = pygame.time.Clock()

WIDTH = 800
HEIGTH = 600
SCL = 5


class Grid():
    def __init__(self):
        self.world = set( )
        self.shader = 0

    def letsGetStarted(self):
        for y in range(HEIGTH // SCL):
            for x in  range(WIDTH // SCL):
                if not randint(0,1):
                    self.world.add( (x, y)  )
                
    def next_gen(self):
        to_consider = []
        for pos in self.world:
            to_consider.append((pos[0]-1, pos[1]))
            to_consider.append((pos[0]+1, pos[1]))
            to_consider.append((pos[0], pos[1]-1))
            to_consider.append((pos[0], pos[1]+1))
            to_consider.append((pos[0], pos[1]))
            to_consider.append((pos[0]-1, pos[1]-1))
            to_consider.append((pos[0]-1, pos[1]+1))
            to_consider.append((pos[0]+1, pos[1]-1))
            to_consider.append((pos[0]+1, pos[1]+1))

        nexster = set()
        for pos in to_consider:
            neighbour_pos = [ 
                (pos[0]-1, pos[1]),
                (pos[0]+1, pos[1]),
                (pos[0], pos[1]-1),
                (pos[0], pos[1]+1),
                (pos[0]-1, pos[1]-1),
                (pos[0]-1, pos[1]+1),
                (pos[0]+1, pos[1]-1),
                (pos[0]+1, pos[1]+1)
            ]

            if(pos[0] < 0 or pos[0] > (WIDTH//SCL) or pos[1] < 0 or pos[1] > (HEIGTH//SCL)):
                continue

            neighbour_count = 0
            for neighbour in neighbour_pos:
                if neighbour in self.world:
                    neighbour_count += 1

            if pos in self.world and neighbour_count == 2:
                nexster.add(pos)
            if pos in self.world and neighbour_count == 3:
                nexster.add(pos)
            if pos not in self.world and neighbour_count == 3:
                nexster.add(pos)
                
        self.world = nexster


    def draw(self, wn):

        color = (0, 0, 0)
        if self.shader < 255:
            color = (self.shader, 0, 255 - self.shader)
        elif self.shader > 255 and self.shader < 510:
            color = (510-self.shader, self.shader-256, 0)
        elif self.shader > 510:
            color = (0, 768-self.shader, self.shader - 510)

        self.shader += 1;
        self.shader %= 768
        for pos in self.world:
            pygame.draw.rect(wn, color, (pos[0]*SCL, pos[1]*SCL, SCL, SCL))


def main():
    wn = pygame.display.set_mode((WIDTH, HEIGTH))

    mapster = Grid()
    mapster.letsGetStarted()

    while True:
        # clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        wn.fill((0, 0, 0))

        mapster.draw(wn)
        mapster.next_gen()

        pygame.display.update()
        # time.sleep(0.5)

main()
