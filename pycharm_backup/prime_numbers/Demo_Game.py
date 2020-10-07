import turtle

# set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("My man")
wn.bgpic("Sunset.gif")

# Register the shapes

# set up border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300, -300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()

# Set up the exit box
line = turtle.Turtle()
line.speed(0)
line.color("blue")
line.penup()
line.setposition(230, 230)
line.pendown()
line.pensize(1)
for side_2 in range(4):
    line.fd(40)
    line.lt(90)
line.hideturtle()

# Set up the obstacle
obstacle = turtle.Turtle()
obstacle.speed(0)
obstacle.color("white")
obstacle.penup()
obstacle.setposition(-100, -100)
obstacle.pendown()
for side_3 in range(4):
    obstacle.fd(200)
    obstacle.lt(90)
obstacle.hideturtle()

# Create the player
player = turtle.Turtle()
player.speed(0)
player.color("blue")
player.shape("triangle")
player.penup()
player.setposition(0, 200)

player_speed = 15

# Set up enemy
enemy = turtle.Turtle()
enemy.speed(0)
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.shapesize(1)
xPos = 0
yPos = -200
enemy.setposition(xPos, yPos)

enemySpeed_x = 5
enemySpeed_y = 5


def move_right():
    x_right = player.xcor()
    x_right += player_speed
    if x_right > 280:
        x_right = 280
    player.setx(x_right)
    player.setheading(0)

def move_left():
    x_left = player.xcor()
    x_left -= player_speed
    if x_left < -280:
        x_left = -280
    player.setx(x_left)
    player.setheading(180)

def move_up():
    y_up = player.ycor()
    y_up += player_speed
    if y_up > 280:
        y_up = 280
    player.sety(y_up)
    player.setheading(90)


def move_down():
    y_down = player.ycor()
    y_down -= player_speed
    if y_down < - 280:
        y_down = -280
    player.sety(y_down)
    player.setheading(270)

def run():
    global player_speed
    if (player_speed == 15):
        player_speed += 30
    elif (player_speed == 45):
        player_speed -= 30


def collision():
    if (player.ycor() > 230 and player.ycor() < 270 and player.xcor() > 230 and player.xcor() < 270):
        print("Hai ")


# Keyboard bindings
wn.listen()
wn.onkey(move_right, "Right")
wn.onkey(move_left, "Left")
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")
wn.onkey(run, "space")

game_running = True

while game_running:

    # Make the enemy move/bounce
    xPos += enemySpeed_x
    if (xPos > 300 or xPos < -300):
        enemySpeed_x *= -1

    yPos += enemySpeed_y
    if(yPos > 300 or yPos < -300):
        enemySpeed_y *= -1

    if (enemy.xcor() > -100 and enemy.xcor() < 100 and enemy.ycor() > -100 and enemy.ycor() < 100):
        enemySpeed_x *= -1
        enemySpeed_y *= -1

    enemy.setposition(xPos, yPos)

    # Set the exit box boundaries
    if player.xcor() > 225 < 275 and player.ycor() > 225 < 275:
        game_running = False

    # Set the obstacle box boundaries
    if (player.xcor() > -100 and player.xcor() < 100 and player.ycor() > -100 and player.ycor() < 100):
        player.backward(10)

