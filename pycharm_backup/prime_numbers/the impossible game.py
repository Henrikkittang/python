import pygame
pygame.init()

wn = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Game")

clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.isJump = False
        self.jumpCount = 7
        self.floor = self.y - self.height

    def draw(self, wn):
        pygame.draw.rect(wn, (0, 255, 0), (self.x, self.y, self.width, self.height))

    def jump(self):
        if self.jumpCount >= -7:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            self.y -= (self.jumpCount ** 2) * 0.5 * neg
            self.jumpCount -= 1
        else:
            self.isJump = False
            self.jumpCount = 7


class block(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.speed = 20

    def draw(self, wn):
        pygame.draw.rect(wn, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def move(self):
        self.x -= self.speed


def draw_grid():
    """Vertical grid"""
    for index in range(40, 800, 40):
        pygame.draw.line(wn, (255, 255, 0), (index, 0), (index, 400), 1)

    """Horizontal grid"""
    for index in range(40, 400, 40):
        pygame.draw.line(wn, (255, 255, 0), (0, index), (800, index), 1)


def draw_game_window():
    wn.fill((0, 0, 0))
    man.draw(wn)
    blk.draw(wn)

    pygame.draw.rect(wn, (255, 0, 0), (0, 360, 800, 40))
    draw_grid()
    man_y = font.render(str(man.y), 1, (255, 0, 0))
    wn.blit(man_y, (5, 5))
    pygame.display.update()


font = pygame.font.SysFont("comicsans", 30, True)
man = player(120, 320)
# spikes = [spike(700, 320, 40, 40), spike(740, 320, 40, 40)]
blk = block(800, 320)
game_loop = True
while game_loop:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    keys = pygame.key.get_pressed()

    blk.move()

    if blk.x < 0:
        blk.x = 800

    if keys[pygame.K_SPACE]:
        man.isJump = True

    if man.isJump == True:
        man.jump()

    if man.y + man.height <= blk.y and man.x + man.width <= blk.x or man.y + man.height <= blk.y and man.x > blk.x + blk.width:
        man.floor = blk.y
    else:
        man.floor = man.y - man.height


    draw_game_window()
    print(man.floor)