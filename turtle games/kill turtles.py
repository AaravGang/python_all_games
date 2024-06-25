import turtle

import math
import random
import time
turtle.register_shape("gun.gif")

#time limit
"""global timestarting
timestarting = time.time()
time.time()"""
#score
score=0
health = 1
turtle.colormode(255)
#ammo variable
global bc
bc = 0



#screen
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Invader Turtles-Level 1")
wn.setup(800,800)
#border turtle
penborder = turtle.Turtle()
penborder.speed(0)
penborder.hideturtle()
penborder.penup()
penborder.goto(0,200)

penborder.write("NOTE: Repeated pausing can get the turtles lower....",align="center",font=("algerian",25,"normal"))
time.sleep(3)

penborder.clear()
wn.setup(1000,1000)
penborder.write("NOTE: Click on the pause symbol to pause...To Unpause click anyehere on the screen...",align="center",font=("algerian",25,"normal"))
time.sleep(5)
wn.setup(800,800)

penborder.clear()
penborder.penup()
penborder.goto(-300,300)
penborder.pendown()
penborder.pensize(10)
#timewriter
"""timewriter = turtle.Turtle()
timewriter.hideturtle()
timewriter.penup()
timewriter.goto(0,370)
timewriter.pendown()"""
#ammowriter
ammowriter = turtle.Turtle()
ammowriter.hideturtle()
ammowriter.penup()
ammowriter.goto(340,350)
ammowriter.pendown()


ammowriter.pencolor("black")

ammowriter.clear()
ammowriter.write("Ammo Left: "+str(13-bc),font=("algerian",25,"normal"),align=("right"))

#border
for i in range(4):
    penborder.forward(600)
    penborder.right(90)
#player
player = turtle.Turtle()
player.shape("gun.gif")
player.color("blue")
player.penup()
player.setheading(90)
player.speed(0)
player.goto(0,-250)
player.shapesize(2,2)
playerspeed = 20
#enemy
count = 3
enemies = []
for i in range(count):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.shape("turtle")
    enemy.shapesize(2,2)
    enemy.penup()


    enemy.goto(random.randint(-250,200),250)
    enemy.color("brown")
enemyspeed = 10
#bullet
bullet = turtle.Turtle()
bullet.penup()
bullet.speed(0)
bullet.shape("circle")
bullet.shapesize(1,0.5)
bullet.color("black")
bullet.hideturtle()
bulletspeed = 100
bullet.goto(6000,6000)
bulletstate = "ready"
# score turtle
scorekeeper = turtle.Turtle()
scorekeeper.hideturtle()
scorekeeper.penup()
scorekeeper.setposition(-350, 350)
scorekeeper.pencolor("black")
scorekeeper.clear()
scorekeeper.write(("Your Score Is:" + str(score)), font=("algerian", 25, "normal"))
#pausing turtle
pausing = turtle.Turtle()
pausing .hideturtle()
pausing.speed(0)
pausing.penup()
pausing.goto(350,350)
pausing.pencolor("black")
pausing.shape("square")
pausing.shapesize(2,0.25)
pausing.showturtle()
#pausing2turtle
pausing2 = turtle.Turtle()
pausing2 .hideturtle()
pausing2.speed(0)
pausing2.penup()
pausing2.goto(370,350)
pausing2.pencolor("black")
pausing2.shape("square")
pausing2.shapesize(2,0.25)
pausing2.showturtle()



#player movements
def player_right():
    x = player.xcor()
    x+=playerspeed
    if x <-280:
        x = -280
    player.setx(x)
def player_left():
    x = player.xcor()
    x-=playerspeed
    if x >280:
        x = 280
    player.setx(x)
def fire():
    global bulletstate
    global bc
    if bulletstate == "ready":
        x = player.xcor()+40
        z = player.ycor()+20
        bullet.setpos(x,z)
        bullet.showturtle()
        
        
        
        bulletstate = "fire"
        bc+=1
        
        
def collision(t1,t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if d<50:
        return True
    else:
        return False
#pause

def Pause(x,y):
    if x>=345 and x<=380 and y>=330 and y<=380:
        global enemyspeed
        global enemyspeedalias
        enemyspeedalias=enemyspeed
        enemyspeed = 0
        global playerspeed
        playerspeed = 0
        global bulletspeed
        bulletspeed = 0
        pausing.hideturtle()
        pausing2.hideturtle()
        pausing.shape("triangle")
        pausing.shapesize(2,2)
        pausing.showturtle()
        for enemy in enemies:
            if enemy.xcor()>=280:
                xcor = enemy.xcor()
                xcor=270
                enemy.setx(xcor)
            if enemy.xcor()<=-280:
                xcor = enemy.xcor()
                xcor=-270
                enemy.setx(xcor)
    #unpause
    else:
        if enemyspeedalias>0:
            enemyspeed=10
        else:
            enemyspeed=-10
        
        
        playerspeed = 20
        
        bulletspeed = 100
        pausing.hideturtle()
        pausing.shape("square")
        pausing.shapesize(2,0.25)
        pausing.showturtle()
        pausing2.showturtle()






def level2():
    #reseting ammo
    global bc  
    bc=0
    #ammo part
    ammowriter.clear()
    ammowriter.write("Ammo Left: "+str(60-bc),font=("algerian",25,"normal"),align=("right"))

    #startime = time.time()
    
    while True:
        global bulletstate
        global bulletspeed
        
        global playerspeed
        global enemyspeed
        global health
        global score
        
        
       
        
        
        #time part
        #timewriter.clear()
        #timewriter.write("Your Time Left Is "+str(int(110-(time.time()-startime)))+" Sceonds",font=("algerian",25,"normal"),align="center")
       
        
        """if (time.time()-startime)>110:
            wn.clear()
            time.sleep(1)
            penborder.goto(0,0)
            penborder.pendown()
            penborder.pencolor("black")
            penborder.write("You Have Lost", align = "center",font=("algerian", 25, "normal"))
            time.sleep(5)
            exit()
            """
        
        

        # bullet firing


        if bulletstate == "fire":
            
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)
            
            #ammo part
            ammowriter.clear()
            ammowriter.write("Ammo Left: "+str(60-bc),font=("algerian",25,"normal"),align=("right"))
            
            if bc>=60:
                wn.clear()
                timewriter.penup()
                timewriter.goto(0,0)
                timewriter.pendown()
                timewriter.pencolor("black")
                timewriter.write("You Have Lost",align="center",font=("algerian",25,"normal"))

                time.sleep(5)
                exit()

            
            
            
        

        if bullet.ycor() >= 280:
            bullet.hideturtle()
            bulletstate = "ready" 

        #player boundry
        if player.xcor()>280 or player.xcor()<=-280:
            playerspeed *= -1
        #moving enemy
        for enemy in enemies:
            


            x = enemy.xcor()
            x+=enemyspeed
            enemy.setx(x)
            if enemy.xcor()>=280:
                enemy.setx(280)
                if bulletstate=="fire":
                    pass
                else:
                    enemy.right(90)
                    enemy.right(90)

                    enemyspeed *= -1
                    y = enemy.ycor()
                    y -=100
                    enemy.sety(y)
            elif enemy.xcor() <= -280 :
                enemy.setx(-280)
                if bulletstate=="fire":
                    pass
                else:
                    enemy.left(90)
                    enemy.left(90)

                    enemyspeed *= -1
                    y = enemy.ycor()
                    y -= 100
                    enemy.sety(y)
            if enemy.ycor()>150:
                enemy.shapesize(2,2)
                # collision enemy  and bullet
                if collision(bullet, enemy):
                    bullet.speed(0)
                    bullet.hideturtle()
                    bulletstate = "ready"
                    bullet.goto(-400, -400)
                    enemy.color("red")
                    score += 1
                    enemy.hideturtle()
                    enemy.shapesize(2, 2)
                    health = 1
                    enemy.goto(random.randint(-250, 250), 250)
                    enemy.showturtle()
                    scorekeeper.clear()
                    scorekeeper.write(("Your Score Is:" + str(score)), font=("algerian", 25, "normal"))
                    enemy.color("brown")

            if enemy.ycor()<=150 and enemy.ycor()>=50:
                enemy.shapesize(2.5, 2.5)
                # collision enemy  and bullet
                if collision(bullet, enemy):

                    health-=1
                    bullet.speed(0)
                    bullet.hideturtle()
                    bulletstate = "ready"
                    bullet.goto(-400, -400)
                    if health == -1:

                        enemy.color("red")
                        score += 1
                        enemy.hideturtle()
                        enemy.shapesize(2,2)
                        health = 1
                        enemy.goto(random.randint(-250, 250), 250)
                        enemy.showturtle()
                        scorekeeper.clear()
                        scorekeeper.write(("Your Score Is:" + str(score)), font=("algerian", 25, "normal"))
                        enemy.color("brown")
            if enemy.ycor()<50:

                enemy.shapesize(3,3)
                # collision enemy  and bullet
                if collision(bullet, enemy):
                    health-=1
                    bullet.speed(0)
                    bullet.hideturtle()
                    bulletstate = "ready"
                    bullet.goto(-400, -400)
                    if health==-2:
                        enemy.color("red")
                        score += 1
                        enemy.hideturtle()
                        enemy.shapesize(2,2)
                        health = 1
                        enemy.goto(random.randint(-250, 250), 250)
                        enemy.showturtle()
                        scorekeeper.clear()
                        scorekeeper.write(("Your Score Is:" + str(score)), font=("algerian", 25, "normal"))
                        enemy.color("brown")

            if enemyspeed>0:
                if bulletstate=="fire":
                    pass
                else:
                    enemy.setheading(0)
            elif enemyspeed<0:
                if bulletstate=="fire":
                    pass
                else:
                    enemy.setheading(180)






            # collision enemy and player
            if collision(player, enemy) or enemy.ycor() <= player.ycor():
                wn.clear()
                penborder.goto(0,0)
                penborder.pensize(10)
                penborder.pendown()
                penborder.write("You Have Lost",align="center",font=("algerian",20,"normal"))
                time.sleep(3)
                exit()
        #win
        if score>=30:
            wn.clear()
            penborder.penup()
            penborder.goto(0,0)
            penborder.pendown()
            penborder.write("You Have Won",align="center",font=("algerian",20,"normal"))
            time.sleep(3)
            exit()
        




        wn.update()
#onkey calling
wn.listen()
wn.onkey(player_right,"Right")
wn.onkey(player_left,"Left")
wn.onkey(fire, "Up")
wn.onscreenclick(Pause,1)
#wn.onscreenclick(unpause,1)












    
while True:
    
    
    
    
    #time part
    #timewriter.clear()
    #timewriter.write("Your Time Left Is "+str(int(30-(time.time()-timestarting)))+" Seconds",font=("algerian",25,"normal"),align="center")
    
    """ if (time.time()-timestarting)>30:
        wn.clear()
        time.sleep(1)
        penborder.goto(0,0)
        penborder.pendown()
        penborder.pencolor("black")
        penborder.write("You Have Lost", align = "center",font=("algerian", 25, "normal"))
        time.sleep(5)
        exit()"""
    # bullet firing
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
        #ammo part
        ammowriter.clear()
        ammowriter.write("Ammo Left: "+str(13-bc),font=("algerian",25,"normal"),align="right")
        if bc>=13:
            wn.clear()
            timewriter.penup()
            timewriter.goto(0,0)
            timewriter.pendown()
            timewriter.pencolor("black")
            timewriter.write("You Have Lost",align="center",font=("algerian",25,"normal"))

            time.sleep(5)
            exit()

    if bullet.ycor() >= 280:
        bullet.hideturtle()
        bulletstate = "ready"

    #player boundry
    if player.xcor()>280 or player.xcor()<=-280:
        playerspeed *= -1
    #moving enemy
    for enemy in enemies:

        x = enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)
        if enemy.xcor()>=280:
            enemy.setx(280)
            if bulletstate=="fire":
                pass
            else:
                enemy.right(90)
                enemy.right(90)

                enemyspeed *= -1
                y = enemy.ycor()
                y -=100
                enemy.sety(y)
        elif enemy.xcor() <= -280 :
            enemy.setx(-280)
            if bulletstate=="fire":
                pass
            else:
                enemy.left(90)
                enemy.left(90)

                enemyspeed *= -1
                y = enemy.ycor()
                y -= 100
                enemy.sety(y)
        if enemyspeed>0:
            if bulletstate=="fire":
                pass
            else:
                enemy.setheading(0)
        elif enemyspeed<0:
            if bulletstate=="fire":
                pass
            else:
                enemy.setheading(180)



        # collision enemy  and bullet
        if collision(bullet, enemy):
            enemy.color("red")
            bullet.speed(0)
            bullet.goto(-400,-400)
            score+=1

            bullet.hideturtle()
            bulletstate = "ready"

            enemy.hideturtle()
            enemy.goto(random.randint(-250,250),250)
            enemy.showturtle()
            scorekeeper.clear()
            scorekeeper.write(("Your Score Is:" + str(score)), font=("algerian", 25, "normal"))
            enemy.color("brown")
        # collision enemy and player
        if collision(player, enemy) or enemy.ycor() <= player.ycor():
            wn.clear()
            penborder.goto(0,0)
            penborder.pensize(10)
            penborder.pendown()
            penborder.write("You Have Lost",align="center",font=("algerian",20,"normal"))
            time.sleep(3)
            exit()
    #win
    if score>=10:

        penborde = turtle.Turtle()
        penborde.penup()
        penborde.hideturtle()
        penborde.speed(0)

        penborde.goto(0, 0)
        penborde.pensize(10)
        penborde.pendown()
        penborde.write("Do U Want To Play Level2?", align="center", font=("algerian", 20, "normal"))
        penborde.penup()
        scorekeepe = turtle.Turtle()
        scorekeepe.penup()
        penborde.goto(0,-150)
        penborde.shape("triangle")
        penborde.shapesize(2,2)
        penborde.showturtle()

        scorekeepe.hideturtle()
        scorekeepe.goto(0,-100)
        scorekeepe.setheading(180)
        scorekeepe.pendown()
        scorekeepe.pensize(15)
        scorekeepe.pencolor("black")
        scorekeepe.circle(50)
        time.sleep(3)
        scorekeepe.clear()
        penborde.clear()
        penborde.hideturtle()
        score = 0
        scorekeeper.clear()
        scorekeeper.write(("Your Score Is:" + str(score)), font=("algerian", 25, "normal"))
        wn.title(" Invaders Turtle-Level 2")
        for enemy in enemies:
            enemy.shape("turtle")
            enemy.shapesize(2, 2)
            enemy.penup()

            enemy.goto(random.randint(-250, 200), 250)
            enemy.color("brown")
        level2()


    wn.update()




