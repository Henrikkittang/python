import pygame
import math
import random

pygame.init()

wn = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Space invaders 3")

clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 12
        self.health = 3

    def draw(self, wn):
        # pygame.draw.rect(wn, (255, 0, 0), (self.x, self.y, 40, 40))
        wn.blit(pygame.image.load("player.gif"), (self.x, self.y))

        health_string = font.render("Health: ", 1, (255, 0, 0))
        wn.blit(health_string, (500, 5))

        if self.health > 0:
            for i in range(0, self.health):
                pygame.draw.rect(wn, (0, 255, 0), (600 + 25*i, 5, 18, 18))

        else:
            quit()


class invader(object):
    def __init__(self, x, y, row):
        self.x = x
        self.y = y
        self.speed = 25
        self.timer = 0
        self.row = row

    def draw(self, wn):
        wn.blit(pygame.image.load("invader.gif"), (self.x, self.y))
        self.move()

    def move(self):
        if self.timer < 25:
            self.timer += 1
        if self.timer == 25:
            self.x += self.speed
            self.timer = 0


class square(object):
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self, wn):
        pygame.draw.rect(wn, (0, 255, 0), (self.x, self.y, self.height, self.width))


class projectile(object):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.speed = 15 * direction

    def draw(self, wn):
        wn.blit(pygame.image.load("lazer.gif"), (self.x - 15, self.y))
        self.move()

    def move(self):
        self.y -= self.speed


def collision(o1, o2, threshold):
    distance = math.sqrt(math.pow(o1.x - o2.x, 2) + math.pow(o1.y - o2.y, 2))
    if distance < threshold:
        return True
    else:
        return False


def make_base():
    # pygame.draw.rect(wn, (255, 0, 0), (30, 450, 150, 70))
    # pygame.draw.rect(wn, (255, 0, 0), (275, 450, 150, 70))
    # pygame.draw.rect(wn, (255, 0, 0), (520, 450, 150, 70))
    for y in range(450, 520, 10):
        for x in range(30, 180, 10):
            blocks.append(square(x, y, 10, 10))
        for x in range(275, 425, 10):
            blocks.append(square(x, y, 10, 10))
        for x in range(520, 670, 10):
            blocks.append(square(x, y, 10, 10))


def make_invaders():
    for y in range(50, 300, 50):
        for x in range(50, 500, 50):
            invaders.append(invader(x, y, x // 50))
            pygame.time.delay(20)


def draw_window():
    wn.fill((0, 0, 0))
    text = font.render("Score: " + str(score), 1, (255, 0, 0))
    wn.blit(text, (5, 5))

    man.draw(wn)
    for index in bullets:
        index.draw(wn)

    for index in blocks:
        index.draw(wn)

    for index in invaders:
        index.draw(wn)

    for index in invader_bullets:
        index.draw(wn)

    # pygame.draw.rect(wn, (0, 0, 255), (50, 50, 450, 250))
    # pygame.draw.rect(wn, (255, 0, 0), (50, 50, 50, 50))

    pygame.display.update()


font = pygame.font.SysFont("comicsans", 30, True)
man = player(350, 550)

invader_bullets = []
bullets = []
blocks = []
invaders = []
rows = []

bullet_delay = 0
invader_bullet_delay = 0
score = 0

make_base()
make_invaders()

global loop
loop = True
while loop:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    if bullet_delay < 15:
        bullet_delay += 1

    if invader_bullet_delay < 15:
        invader_bullet_delay += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    keys = pygame.key.get_pressed()

    """Player controls"""
    if keys[pygame.K_RIGHT] and man.x < 650:
        man.x += man.speed
    if keys[pygame.K_LEFT] and man.x > 2:
        man.x -= man.speed
    if keys[pygame.K_SPACE] and len(bullets) < 1 and bullet_delay == 15:
        bullets.append(projectile(man.x + 15, man.y, 1))
        bullet_delay = 0

    if keys[pygame.K_f]:
        invaders.pop()

    """Invader movement"""
    for index in invaders:
        if index.x <= 0 or index.x >= 650:
            for invader in invaders:
                invader.y += 20
                invader.speed *= -1
                invader.x += invader.speed

    """Bullet and base collision"""
    for bullet in bullets:
        for block in blocks:
            if collision(block, bullet, 10) == True:
                blocks.remove(block)
                try:
                    bullets.remove(bullet)
                except ValueError:
                    print("Bug!")
        if bullet.y < 0 or bullet.y > 600:
            bullets.remove(bullet)

    """Invader_bullet and base collision"""
    for bullet in invader_bullets:
        if bullet.y < 0 or bullet.y > 600:
            invader_bullets.remove(bullet)
        for block in blocks:
            if collision(block, bullet, 10) == True:
                blocks.remove(block)
                try:
                    invader_bullets.remove(bullet)
                except ValueError:
                    print("Value error!")

    """Bullet and invader collision"""
    for bullet in bullets:
        for invader in invaders:
            if collision(invader, bullet, 30) == True:
                invaders.remove(invader)
                try:
                    bullets.remove(bullet)
                except ValueError:
                    print("Value error!")

                score += 10

    """Invader_bullet and player collision"""
    for index in invader_bullets:
        if collision(index, man, 30) == True:
            man.health -= 1
            invader_bullets.remove(index)

    """Invader bullet"""
    if invader_bullet_delay == 15:
        row = random.randint(1, 9)
        pick = True
        while pick:
            for invader in invaders:
                if invader.row == row:
                    rows.append(invader)

            if len(rows) > 0:
                invader_bullets.append(projectile(rows[-1].x + 15, rows[-1].y + 31, -1))
                pick = False
            elif len(rows) == 0:
                row = random.randint(1, 9)

        invader_bullet_delay = 0

    rows.clear()

    draw_window()
