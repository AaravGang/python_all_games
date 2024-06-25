# import stuff
import turtle
import random
import math
import time


# window
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(7)


# player
player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.speed(0)
player.penup()
player.goto(-200, -200)

speed = 1


# goals
maxgoals = 2
goals = []

for count in range(maxgoals):
    goals.append(turtle.Turtle())
    goals[count].shape("circle")
    goals[count].color("lightblue")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].goto(random.randint(-300, 300), random.randint(-300, 300))
    goals[count].right(random.randint(0, 360))
    # score variable
    score = 0


# border bouncing

pen = turtle.Turtle()
pen.color("lightgreen")
pen.penup()
pen.goto(-300, -300)
pen.pendown()
pen.pensize(4)
for side in range(4):
    pen.forward(600)
    pen.left(90)
pen.hideturtle()


# def functions
def player_right():
    player.right(35)


def player_left():
    player.left(35)


def increase():
    global speed
    speed += 1


def decrease():
    global speed
    if speed >= 1:
        speed -= 1


def iscollision(t1, t2):
    d = math.sqrt(
        math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2)
    )
    if d <= 20:
        return True
    else:
        return False


# keyboard
wn.listen()
wn.onkey(player_right, "Right")
wn.onkey(player_left, "Left")
wn.onkey(decrease, "Down")
wn.onkey(increase, "Up")


while True:
    player.forward(speed)

    # playerboundrydash
    if player.xcor() > 290 or player.xcor() < -290:
        player.left(180)

    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)

    # goalmove
    for count in range(maxgoals):
        goals[count].forward(2)

        # goal boundry dash
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].left(180)

        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)

        # player goal collision
        if iscollision(player, goals[count]):

            goals[count].setposition(
                random.randint(-300, 300), random.randint(-300, 300)
            )
            goals[count].right(random.randint(0, 360))
            score += 1

            # score
            pen.undo()
            pen.color("gray")
            pen.penup()
            pen.hideturtle()
            pen.goto(-325, 325)
            scorestring = "Score %s" % score
            pen.write(scorestring, align="left", font=("Algerian", 20, "normal"))

            # end
            if score == 10:
                wn.clear()
                wn.bgcolor("gold")
                pen.clear()
                pen.color("red")

                pen.penup()
                pen.hideturtle()
                pen.goto(-325, 0)
                pen.write(
                    "Congrats! You completed the Game!",
                    align="left",
                    font=("Algerian", 40, "normal"),
                )
                time.sleep(3)
                exit()

