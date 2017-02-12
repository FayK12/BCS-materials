#this code was written using PyCharm
#guide the turtle across the board to the finish line

import turtle
import random

loadWindow = turtle.Screen()
loadWindow.colormode(255)

jay = turtle.Pen()
jay.ht()
jay.penup()
jay.setpos(-250,245)
jay.pencolor("red")
jay.write("Turtle Crossing", False, align="left", font=("Times New Roman",15, "normal"))
fred = turtle.Pen()
fred.pu()
fred.goto(-250,-250)
fred.speed(0)
loadWindow.title("Turtle Crossing")
fred.pd()


for i in range (1,101):
    a = random.randint(133,255)
    b = random.randint(200,255)
    c = random.randint(139,255)
    #a=[139,250,0,238,255]
    #b=[188,233,255,0,240]
    #c=[0,255,250,130,233]
    #x = random.randint(0,4)
    #y = random.randint(0,4)
    #z = random.randint(0,4)
    fred.begin_fill()
    for x in range (4):
        fred.fd(45)
        fred.left(90)
    fred.write(i, False, align="left", font=("Arial Bold", 7, "normal"))
    #fred.color(a[x],b[y],c[z])
    fred.color(a,b,c)
    fred.end_fill()
    fred.pencolor("black")
    fred.fd(45)
    if (i%10==0):
        #fred.speed(2)
        fred.pu()
        y=(-250+45*(i/10))
        fred.goto(-250,y)
        fred.pd()
        #fred.left(90)
        #fred.fd(45)
mike = fred.clone()
mike.pu()
mike.speed(1)
mike.goto(-250,-255)
mike.ht()
mike.backward(50)
mike.write("START", False, align="left", font=("Arial Bold",10, "normal"))
fred.fd(450)
fred.write("FINISH", False, align="left", font=("Arial Bold",10, "normal"))
fred.pu()
jay.setpos(-250,225)
jay.pencolor("black")
jay.write("Use the arrow keys to help Mike to the finish line. Mike must meet fellow turtle Fay before finishing.", False, align="left", font=("Arial",8, "normal"))
jay.setpos(-250,215)
jay.write("Watch out for the moving obstacles! Click the X on the screen to exit anytime", False, align="left", font=("Arial",8, "normal"))
jay.setpos(-250,-270)
jay.write("Up,Down - forward, backward", False, align="left", font=("Arial Bold",8, "normal"))
jay.setpos(0,-270)
jay.write("Left,Right - turn left/right", False, align="left", font=("Arial Bold",8, "normal"))
#fred.shape("turtle")
#fred.color("blue")
#fred.pu()
#fred.speed(2)
#fred.seth(260)
#fred.goto(0,0)
#fred.stamp()
mike.setpos(-270,-230)
mike.st()
mike.shape("turtle")
mike.color("purple")
mike.turtlesize(1,1,2)
#mike.goto(100,50)
#mike.tilt(45)
mike.stamp()
mike.pu()

def up():
    mike.fd(45) #use for onkeypress
    #if mike.pos()== (180.00,-230.00):
    #    mike.fd(0)
def down():
    mike.bk(45)
def left():
    mike.left(90)
def right():
    mike.right(90)



'''if mike.setpos(250,250) ==True:
    fred.fd(50)
    fred.write("You did it!", False, align="left", font=("Calibri Bold",10, "normal"))'''

#loadWindow.ontimer(move(mike),25)

jay.home()
jay.showturtle()
jay.shape("circle")
jay.speed(1)
jeff = jay.clone()
jeff.shape("square")

loadWindow.onkeypress(up,"Up")
loadWindow.onkeypress(down,"Down")
loadWindow.onkeypress(left,"Left")
loadWindow.onkeypress(right,"Right")
loadWindow.listen()



'''player = mike.pos()
player_y = mike.ycor()
while player == (-270,-230): #and (player_y!=200):
    xcor = random.randint(-250, 200)
    ycor = random.randint(-180, 180)
    jay.goto(xcor, 0)
    jay.goto(0, ycor)
    jeff.goto(-150, xcor)
    jeff.goto(-150,-245)
    #player = mike.pos()

def end():
    loadWindow.exitonclick()

loadWindow.ontimer(end,250)'''

#timer = int(loadWindow.numinput("Timer","How long will it take you to cross? Enter a number in milliseconds?"))
#for i in range(timer):
#player = mike.pos()
#V = mike.Vec2D(225.00,175.00)
#print(player)
john = jeff.clone()
may = jay.clone()
fay = mike.clone()
fay.color("orange")
fay.pu()
fay.speed(1)
while True: #player == (-270,-230): #and (player_y!=200)
    xcor = random.randint(-250, 200)
    ycor = random.randint(-180, 180)
    jay.goto(xcor, 0)
    jay.goto(0, ycor)
    may.goto(xcor,ycor)
    may.goto(ycor,xcor)
    jeff.goto(-150, xcor)
    jeff.goto(-150,-245)
    john.goto(160,xcor)
    john.goto(160,ycor)
    fay.ht()
    fay.st()
    fay.goto(xcor,ycor)
    #player = mike.pos()
    #print(player)
    #if player == V:
    #    break
loadWindow.exitonclick()

#loadWindow.mainloop()