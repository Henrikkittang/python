import pygame
pygame.init()


clock = pygame.time.Clock()
wn = pygame.display.set_mode((700, 450))


class ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 4
        self.speed_y = 4

    def draw(self, wn):
        pygame.draw.circle(wn, (255, 255, 255), (self.x, self.y), 10)

    def move(self):
        global wall_1_score, wall_1_length, wall_2_score, wall_2_length

        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0:
            wall_2.score += 1
            wall_2.length -= 10
            self.x = 350
            self.y = 225
            self.speed_x *= -1

        elif self.x > 700:
            wall_1.score += 1
            wall_1.length -= 10
            self.x = 350
            self.y = 225
            self.speed_x *= -1

        if self.y < 0 or self.y > 450:
            self.speed_y *= -1

        if self.x - 10 < wall_1.x + 12 and self.x - 10 < wall_1.x and self.y - 10 > wall_1.y and self.y + 10 < wall_1.y + wall_1.length:
            self.speed_x *= -1
        elif self.x + 10 < wall_2.x and self.x + 10 > wall_2.x - 10 and self.y - 10 > wall_2.y and self.y + 10 < wall_2.y + wall_2.length:
            self.speed_x *= -1


class wall(object):
    def __init__(self, x, y, length, score):
        self.x = x
        self.y = y
        self.length = length
        self.score = score

    def draw(self):
        pygame.draw.rect(wn, (255, 255, 255), (self.x, self.y, 10, self.length))


def draw_window():
    wn.fill((0, 0, 0))

    b.draw(wn)

    score_1 = font.render(str(wall_1.score), 1, (255, 255, 255))
    wn.blit(score_1, (10, 10))

    score_2 = font.render(str(wall_2.score), 1, (255, 255, 255))
    wn.blit(score_2, (650, 10))

    wall_1.draw()
    wall_2.draw()

    pygame.display.update()


wall_1 = wall(20, 5, 150, 0)
wall_2 = wall(670, 5, 150, 0)


b = ball(100, 100)
font = pygame.font.SysFont("comicsans", 50, True)
run = True
while run:
    clock.tick(80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and wall_1.y > 0:
        wall_1.y -= 5
    elif keys[pygame.K_s] and wall_1.y + wall_1.length < 450:
        wall_1.y += 5

    if keys[pygame.K_UP] and wall_2.y > 0:
        wall_2.y -= 5
    elif keys[pygame.K_DOWN] and wall_2.y + wall_2.length < 450:
        wall_2.y += 5

    b.move()
    draw_window()
