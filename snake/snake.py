from random import randint
import pygame
pygame.init()

s_width = 500
s_height = 500
square_length = 25
wn = pygame.display.set_mode((s_width, s_height))

main_grid = []
for q in range(0, s_height//square_length):
    main_grid.append([])
    for t in range(0, s_width//square_length):
        main_grid[q].append(0)


class Snake(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xSpeed = 1
        self.ySpeed = 0
        self.body = [[self.x, self.y] ]

    def draw(self, wn):
        for pos in self.body:
            xPixel = pos[0] * square_length
            yPixel = pos[1] * square_length
            pygame.draw.rect(wn, (255, 0, 0), (xPixel, yPixel, square_length, square_length))

    def getInput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and player.ySpeed != 1:
            self.xSpeed = 0
            self.ySpeed = -1
        elif keys[pygame.K_DOWN] and player.ySpeed != -1:
            self.xSpeed = 0
            self.ySpeed = 1
        elif keys[pygame.K_LEFT] and player.xSpeed != 1:
            self.xSpeed = -1
            self.ySpeed = 0
        elif keys[pygame.K_RIGHT] and player.xSpeed != -1:
            self.xSpeed = 1
            self.ySpeed = 0

    def collision(self):
        for idx1, pos1 in enumerate(self.body):
            for idx2, pos2 in enumerate(self.body):
                if pos1 == pos2 and idx1 != idx2:
                    print(pos1, pos2)
                    self.body = [[self.x, self.y]]

        if (self.x, self.y) == (food.x, food.y):
            self.body.insert(0, [self.x, self.y])
            food.new_pos()

        if (self.x or self.y) < 0 or self.x > (s_width // square_length) or self.y > (s_height // square_length):
            quit()

    def move(self):
        self.collision()

        self.x += self.xSpeed
        self.y += self.ySpeed

        self.body.pop(0)
        self.body.append([self.x, self.y])

class Apple(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def draw(self, wn):
        xPixel = self.x * square_length
        yPixel = self.y * square_length
        pygame.draw.rect(wn, (0, 255, 0), (xPixel, yPixel, square_length, square_length))

    def new_pos(self):
        self.x = randint(0, s_width//square_length - 1)
        self.y = randint(0, s_height//square_length - 1)

def draw_grid():
    """Draws the lines representing the grid"""
    for i in range(0, s_height, square_length):
        pygame.draw.line(wn, (255, 0, 0), (0, i), (s_width, i), 1)

    for i in range(0, s_width, square_length):
        pygame.draw.line(wn, (255, 0, 0), (i, 0), (i, s_height))


def draw_window():
    wn.fill((0, 0, 0))

    draw_grid()

    player.draw(wn)
    food.draw(wn)

    score = font.render("Score: " + str(len(player.body) - 3), 1, (240, 255, 0))
    wn.blit(score, (5, 5))

    pygame.display.update()


x_pos = 400
y_pos = 300
player = Snake(10, 10)
food = Apple(10, 13)
font = pygame.font.SysFont(" ", 30, True)
run = True
while run:
    pygame.time.delay(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.getInput()
    player.move()

    draw_window()
