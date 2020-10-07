import pygame
import math
import random

pygame.init()

wn = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Space invader in pygame")

clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 15

    def draw(self, wn):
        # pygame.draw.rect(wn, (255, 0, 0), (self.x, self.y, 40, 40))
        wn.blit(pygame.image.load("player.gif"), (self.x, self.y))


class locked_invader(object):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.health = 1

    def draw(self, wn):
        # pygame.draw.rect(wn, (255, 0, 0), (self.x, self.y, 35, 35))
        wn.blit(pygame.image.load("space_invader_red.gif"), (self.x, self.y))
        self.move()

    def move(self):
        self.x += self.speed


class free_invader(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.health = 2

    def draw(self, wn):
        wn.blit(pygame.image.load("invader.gif"), (self.x, self.y))
        self.move()

    def move(self):
        if self.x >= 550 or self.x <= 0:
            self.speed *= -1
            self.y += 40

        self.x += self.speed


class super_invader(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8
        self.health = 50

    def draw(self, wn):
        wn.blit(pygame.image.load("super_invader.gif"), (self.x, self.y))

        pygame.draw.rect(wn, (255, 0, 0), (self.x, self.y - 8, 50, 5))
        pygame.draw.rect(wn, (0, 255, 0), (self.x, self.y - 8, 50 - (50 - self.health), 5))

        self.move()

    def move(self):
        if self.x >= 550 or self.x <= 0:
            self.speed *= -1
            self.y += 40

        self.x += self.speed


class projectile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 30
        self.firing = False

    def draw(self, wn):
        wn.blit(pygame.image.load("lazer.gif"), (self.x, self.y))
        if self.firing == True:
            self.move()
        else:
            self.x = man.x + 2
            self.y = man.y + 5

    def move(self):
        if self.y < 0:
            self.firing = False
        self.y -= self.speed


def collision(o1, o2):
    distance = math.sqrt(math.pow(o1.x - o2.x, 2) + math.pow(o1.y - o2.y, 2))
    if distance < 30:
        return True
    else:
        return False


def select_difficulty():
    global number_of_super_invader, number_of_free_invaders, number_of_locked_invaders
    select = 1
    selected = False
    while not selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                selected = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and select != 1:
            select -= 1
        if keys[pygame.K_DOWN] and select != 3:
            select += 1

        if select == 1:
            easy = font.render("Easy", 1, (255, 0, 0))
            medium = font.render("Medium", 1, (0, 255, 0))
            hard = font.render("Hard", 1, (0, 255, 0))
            if keys[pygame.K_SPACE]:
                number_of_super_invader = 2
                number_of_free_invaders = 2
                number_of_locked_invaders = 3
                selected = True

        elif select == 2:
            easy = font.render("Easy", 1, (0, 255, 0))
            medium = font.render("Medium", 1, (255, 0, 0))
            hard = font.render("Hard", 1, (0, 255, 0))
            if keys[pygame.K_SPACE]:
                number_of_super_invader = 4
                number_of_free_invaders = 4
                number_of_locked_invaders = 5
                selected = True

        elif select == 3:
            easy = font.render("Easy", 1, (0, 255, 0))
            medium = font.render("Medium", 1, (0, 255, 0))
            hard = font.render("Hard", 1, (255, 0, 0))
            if keys[pygame.K_SPACE]:
                number_of_super_invader = 6
                number_of_free_invaders = 6
                number_of_locked_invaders = 7
                selected = True


        wn.fill((0, 0, 0))
        wn.blit(easy, (300, 300))
        wn.blit(medium, (300, 330))
        wn.blit(hard, (300, 360))

        text = font.render(str(select), 1, (0, 0, 255))
        wn.blit(text, (5, 5))

        pygame.display.update()
        pygame.time.delay(100)


def draw_window():
    wn.blit(pygame.image.load("background.gif"), (0, 0))
    text = font.render("Score: " + str(score), 1, (0, 255, 0))
    wn.blit(text, (5, 5))
    man.draw(wn)
    bullet.draw(wn)
    for invader in locked_invaders:
        invader.draw(wn)

    for invader in free_invaders:
        invader.draw(wn)

    for invader in super_invaders:
        invader.draw(wn)

    pygame.display.update()


font = pygame.font.SysFont("comicsans", 30, True)

select_difficulty()

man = player(300, 500)
bullet = projectile(man.x, man.y)

locked_invaders = []
for index in range(0, number_of_locked_invaders):
    locked_invader_y = random.randint(5, 380)
    locked_invaders.append(locked_invader(random.randint(5, 540), locked_invader_y, 5))


free_invaders = []
for index in range(0, number_of_free_invaders):
    free_invaders.append(free_invader(random.randint(5, 550), random.randint(5, 380)))


super_invaders = []
for index in range(0, number_of_super_invader):
    super_invaders.append(super_invader(random.randint(5, 550), random.randint(5, 380)))

types = [locked_invaders, free_invaders, super_invaders]

score = 0
game_loop = True

while game_loop:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    keys = pygame.key.get_pressed()

    """Player controls"""
    if keys[pygame.K_RIGHT]:
        man.x += man.speed
    if keys[pygame.K_LEFT]:
        man.x -= man.speed
    if keys[pygame.K_SPACE]:
        bullet.firing = True

    """Locked invaders"""
    for invader in locked_invaders:
        if invader.x >= 550 or invader.x <= 0:
            for invader_2 in locked_invaders:
                invader_2.speed *= -1
                invader_2.y += 40

    for invader in locked_invaders:
        if collision(man, invader) == True:
            game_loop = False

    for invader in locked_invaders:
        if collision(bullet, invader) == True:
            locked_invaders.remove(invader)
            locked_invaders.append(locked_invader(random.randint(5, 540), random.randint(5, 380), invader.speed))
            bullet.firing = False
            score += 10
            print("hit")

    """Free invaders"""
    for invader in free_invaders:
        if collision(man, invader) == True:
            game_loop = False

    for invader in free_invaders:
        if collision(bullet, invader) == True:
            free_invaders.remove(invader)
            free_invaders.append(free_invader(random.randint(5, 550), random.randint(5, 380)))
            bullet.firing = False
            score += 10
            print("hit")

    """Super invader"""
    for invader in super_invaders:
        if collision(man, invader) == True:
            game_loop = False

    for invader in super_invaders:
        if collision(bullet, invader) == True:
            invader.health -= 25
            if invader.health <= 0:
                super_invaders.remove(invader)
                super_invaders.append(super_invader(random.randint(5, 550), random.randint(5, 380)))
                score += 20
            bullet.firing = False
            score += 10
            print("hit")

    draw_window()
