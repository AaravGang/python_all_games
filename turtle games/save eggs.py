import turtle
import time
import math
import random

global eggspeed
global starttime

countfordrop = 0


score = 0
turtle.register_shape("hen.gif")
turtle.register_shape("hen_inverted.gif")


# checking when the game starts
starttime = time.time()

# making screen
wn = turtle.Screen()
wn.setup(800, 800)
wn.title("Catch The Eggs")
# wn.bgcolor("black")
wn.bgpic("farmhouse.gif")


# making score writer turtle
scorer = turtle.Turtle()
scorer.penup()
scorer.hideturtle()
scorer.speed(0)
scorer.goto(-330, 330)
scorer.pensize(5)
scorer.pencolor("black")
scorer.pendown()
scorer.clear()
scorer.write(
    ("Your Score Is:" + str(score)), align="left", font=("algerian", 20, "normal")
)
# making lives left turtle
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.pensize(5)
writer.pencolor("black")
writer.goto(330, 330)
writer.pendown()
writer.clear()
writer.write(
    ("You Will Lose After " + str(20 - countfordrop) + " Drops"),
    align="right",
    font=("algerian", 20, "normal"),
)


# making many egggiver tutrles
turtles = []
# turtlegoto = [(-250, -100), (250, 0), (-150, 50), (150, 150)]
turtlegoto = [(-250, -100), (250, 40), (-150, 100), (150, 190)]
eggigiverpic = [
    "hen.gif",
    "hen_inverted.gif",
    "hen.gif",
    "hen_inverted.gif",
]
count = 4
egggivercount = 0
for i in range(count):
    turtles.append(turtle.Turtle())
for egggiver in turtles:
    egggiver.speed(0)
    egggiver.penup()
    turtlerandom = turtlegoto[0]

    egggiver.goto(turtlerandom)
    turtlegoto.pop(0)
    egggiver.shape(eggigiverpic[0])
    egggiver.color("brown")
    egggiver.shapesize(3, 3)
    eggigiverpic.pop(0)


# making eggs
countforeggs = 3
eggs = []
# egggoto = [(-250, -120), (250, -20), (-150, 30), (150, 130)]
egggoto = [(-250, -120), (250, 20), (-150, 80), (150, 170)]
for i in range(countforeggs):
    eggs.append(turtle.Turtle())
for egg in eggs:
    egg.speed(0)
    egg.penup()
    egg.shape("circle")
    egg.color("yellow")
    egg.shapesize(1, 0.5)
    eggrandom = random.choice(egggoto)
    egg.goto(eggrandom)
    egggoto.remove(eggrandom)

    eggspeed = 5

# making player
player = turtle.Turtle()
player.speed(-1)
player.penup()
player.shape("turtle")
player.shapesize(2, 2)
player.color("brown")
player.goto(0, -250)
player.setheading(90)
playerspeed = 50
# pausing turtle
pausing = turtle.Turtle()
pausing.hideturtle()
pausing.speed(0)
pausing.penup()
pausing.goto(350, 350)
pausing.pencolor("black")
pausing.shape("square")
pausing.shapesize(2, 0.25)
pausing.showturtle()
# pausing2turtle
pausing2 = turtle.Turtle()
pausing2.hideturtle()
pausing2.speed(0)
pausing2.penup()
pausing2.goto(370, 350)
pausing2.pencolor("black")
pausing2.shape("square")
pausing2.shapesize(2, 0.25)
pausing2.showturtle()
global aarav
aarav = True

# defining
# defining moving eggs down
def move_egg():

    for egg in eggs:

        global eggspeed

        ycorofegg = egg.ycor()
        ycorofegg -= eggspeed
        egg.sety(ycorofegg)
        if egg.ycor() <= -270:

            global countfordrop
            countfordrop += 1
            egggoto = [(-250, -120), (250, 20), (-150, 80), (150, 170)]
            eggrandom = random.choice(egggoto)
            egg.goto(eggrandom)
            egggoto.remove(eggrandom)

            writer.clear()
            writer.write(
                ("You Will Lose After " + str(20 - countfordrop) + " Drops"),
                align="right",
                font=("algerian", 20, "normal"),
            )


# player movements
def playergoto1():
    if aarav == True:
        player.goto(-250, -170)


def playergoto2():
    if aarav == True:
        player.goto(250, -50)


def playergoto3():
    if aarav == True:
        player.goto(-150, 10)


def playergoto4():
    if aarav == True:
        player.goto(150, 95)


# defining collision
def collision(t1, t2):
    d = math.sqrt(
        math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2)
    )
    if d < 50:
        return True
    else:
        return False


# pause


def Pause(x, y):

    global aarav
    global countfordrop

    if x >= 345 and x <= 380 and y >= 330 and y <= 380:

        aarav = False
        pausing.hideturtle()
        pausing2.hideturtle()
        pausing.shape("triangle")
        pausing.shapesize(2, 2)
        pausing.showturtle()

    # unpause
    else:

        aarav = True
        pausing.hideturtle()
        pausing.shape("square")
        pausing.shapesize(2, 0.25)
        pausing.showturtle()
        pausing2.showturtle()


# onkey calling
wn.listen()
wn.onkey(playergoto1, "a")
wn.onkey(playergoto2, "'")
wn.onkey(playergoto3, "s")
wn.onkey(playergoto4, ";")
wn.onscreenclick(Pause, 1)


def game():
    global score
    global scorer
    global eggspeed

    global countfordrop
    # main and while loop
    while True:

        # calling moving egg
        if aarav == True:
            move_egg()
        # calling moving clouds
        # moveclouds()
        # collision btwn egg and player
        for egg in eggs:
            if collision(player, egg):

                egg.hideturtle()
                egg.showturtle()
                egggoto = [(-250, -120), (250, 20), (-150, 80), (150, 170)]
                eggrandom = random.choice(egggoto)
                egg.goto(eggrandom)
                egggoto.remove(eggrandom)
                score += 1
                scorer.clear()
                scorer.write(
                    ("Your Score Is:" + str(score)),
                    align="left",
                    font=("algerian", 20, "normal"),
                )
        # PLAYER BORDERS
        if player.xcor() >= 270:
            player.setx(270)
        if player.xcor() <= -270:
            player.setx(-270)
        if player.ycor() >= 270:
            player.sety(270)
        if player.ycor() <= -270:
            player.sety(-270)
        # what will happen when score increases
        if score >= 100 and score <= 300:
            for egg in eggs:
                eggspeed = 7
            """countfordrop = 0
            writer.clear()
            writer.write(("You Will Lose After " + str(20 - countfordrop) + " Drops"),align="right",font=("algerian", 20, "normal"))"""

        elif score >= 300 and score <= 600:
            for egg in eggs:
                eggspeed = 10
            """countfordrop = 0
            writer.clear()
            writer.write(("You Will Lose After " + str(20 - countfordrop) + " Drops"),align="right",font=("algerian", 20, "normal"))"""

        elif score >= 600 and score <= 1000:
            for egg in eggs:
                eggspeed = 12
            """countfordrop = 0
            writer.clear()
            writer.write(("You Will Lose After " + str(20 - countfordrop) + " Drops"),align="right",font=("algerian", 20, "normal"))"""
        elif score % 1000 == 0 and score != 0:
            eggspeed += 3
        wn.update()
        # what will happen when countfordrop increases
        if countfordrop >= 20:

            # checking at what time the game ends
            endtime = time.time()
            wn.clear()
            scorer = turtle.Turtle()
            scorer.pendown()
            scorer.hideturtle()
            scorer.pencolor("white")
            scorer.pensize(10)

            scorer.write(
                "You Have Lost", align="center", font=("algerian", 30, "normal")
            )
            time.sleep(3)
            scorer.clear()

            scorer.write(
                "You Saved "
                + str(score)
                + " Eggs In "
                + str(int(endtime - starttime))
                + " Seconds",
                align="center",
                font=("algerian", 30, "normal"),
            )
            time.sleep(3)
            exit()

        """if score >= 1000:
            wn.clear()
            score = turtle.Turtle()
            score.pendown()
            score.hideturtle()
            score.pensize(10)

            score.write("You Have Won", align="center", font=("algerian", 30, "normal"))
            time.sleep(3)
            exit()"""


game()
