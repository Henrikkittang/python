from random import randint
import pygame
pygame.init()

screen_width = 540
screen_height = 640
wn = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game")
 
player_image = pygame.image.load("player_car.png")
car_image = pygame.image.load("other_cars.png")

clock = pygame.time.Clock()

man_x = 200
man_y = 450
man_speed = 20
man_hit = False
man_health = 3

def man(x, y):
    global man_health, man_hit, loop, game_over

    text = font.render("Health: ", 1, (0,0,0))
    
    wn.blit(player_image, (x, y))

    if man_hit == True:
        if man_health > 0:
            man_health -= 1
        man_hit = False

    if man_health <= 0:
        loop = False
        game_over = True

    wn.blit(text, (screen_width - 185, 7))
    if man_health == 3:
        pygame.draw.rect(wn, (255, 0, 0), (screen_width - 90, 10, 15, 15))
        pygame.draw.rect(wn, (255, 0, 0), (screen_width - 60, 10, 15, 15))
        pygame.draw.rect(wn, (255, 0, 0), (screen_width - 30, 10, 15, 15))

    elif man_health == 2:
        pygame.draw.rect(wn, (255, 0, 0), (screen_width - 90, 10, 15, 15))
        pygame.draw.rect(wn, (255, 0, 0), (screen_width - 60, 10, 15, 15))

    elif man_health == 1:
        pygame.draw.rect(wn, (255, 0, 0), (screen_width - 90, 10, 15, 15))


class car(object):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 100
        self.height = 120

    def draw(self, wn):
        wn.blit(car_image, (self.x, self.y))

def draw_window():
    wn.fill((255, 255, 255))
    text = font.render("Points: " + str(points), 1, (0,0,0))
    wn.blit(text, (5, 5))

    for i in cars:
        i.draw(wn)

    man(man_x, man_y)
    pygame.draw.line(wn, (255, 0, 0), (180, 0), (180, 640))
    pygame.draw.line(wn, (255, 0, 0), (360, 0), (360, 640))

    pygame.display.update()


font = pygame.font.SysFont("comicsans", 30, True)
game_over = False
tick_speed = 20
points = 0
delay = 30
cars = []
loop = True
while loop:
    clock.tick(tick_speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man_x > 0:
        man_x -= man_speed
    if keys[pygame.K_RIGHT] and man_x + 100 < screen_width:
        man_x += man_speed

    if delay > 30:
        if len(cars) < 3:
            lane = randint(1, 3)

            if lane == 1:
                cars.append(car(40, -120, 10))

            elif lane == 2:
                cars.append(car(220, -120, 10))

            elif lane == 3:
                cars.append(car(400, -120, 10))

        points += 5
        tick_speed += 0.2
        delay = 0

    for i in cars:
        i.y += i.speed

        if man_y < i.y + i.height and man_y + 120 > i.y and man_x + 100 > i.x and man_x < i.x + 100:
            man_hit = True
            cars.remove(i)
            
        if i.y > screen_height:
            cars.remove(i)

    delay += 1
    draw_window()


graph_data = open('highscore.txt', 'r').read()
if points > int(graph_data):
    open("highscore.txt", "w").write(str(points))
    graph_data = points


if game_over == True:
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        wn.fill((0, 0, 0))

        text = font.render("Game over", 1, (255, 0, 0))
        wn.blit(text, (100, 280))

        score = font.render("Your Highscore: " + str(points), 1, (255, 0, 0))
        wn.blit(score, (100, 320))

        highscore = font.render("Best Highscore: " + str(graph_data), 1, (255, 0, 0))
        wn.blit(highscore, (100, 340))

        pygame.display.update()

quit()

