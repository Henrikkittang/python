import turtle
import math
import random


# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space invaders")
wn.bgpic("background.gif")

# Register the shapes
wn.register_shape("invader.gif")
wn.register_shape("player.gif")
wn.register_shape("lazer.gif")


# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set the score
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("White")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Areal", 14, "normal"))

# Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -200)
player.setheading(90)

player_speed = 15


# Choose a number of enemies
number_of_enemies = 5
# Create a empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(-100, 250)
    enemy.setposition(x, y)

enemy_speed = 3

# Create the players bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("lazer.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# Define bullet state
# Ready - ready to fire
# Fire - bullet is firing
bulletstate = "ready"

# Move player left and right
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    """Declare bulletstate as a global because it needs to change"""
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move the bullet just above the player
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y + 10)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 18:
        return True
    else:
        return False


# Create keyboard bindings
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "space")

# Main game loop
game_loop = True
while game_loop:

    for enemy in enemies:
        # Move enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Move enemy back and down
        if enemy.xcor() > 280:
            # Make all the enemies move down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change the direction on the enemies
            enemy_speed *= -1

        if enemy.xcor() < -280:
            # Make all the enemies move down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change the direction on the enemies
            enemy_speed *= -1

        # Check for collision between bullet and enemy
        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(-100, 250)
            enemy.setposition(x, y)
            # Update the Score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Areal", 14, "normal"))

        if isCollision(player, enemy):
            print("Game over")
            game_loop = False
            break

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
