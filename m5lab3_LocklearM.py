#Mitchell Locklear
#M5Lab3 - Snowflake
#CTI-110
#10/14/2017

import turtle
import random
 
wn = turtle.Screen()
wn.bgcolor("grey")
 
# assign a name to your turtle
mitch = turtle.Turtle()
mitch.speed(20)
 
# create a list of colours
sfcolor = ["white", "blue", "pink", "purple", "magenta"]
 
# create a function to create different size snowflakes
def snowflake(size):
 
    # move the pen into starting position
    mitch.penup()
    mitch.forward(10*size)
    mitch.left(45)
    mitch.pendown()
    mitch.color(random.choice(sfcolor))
 
    # draw branch 8 times to make a snowflake
    for i in range(8):
        branch(size)   
        mitch.left(45)
     
 
# create one branch of the snowflake
def branch(size):
    for i in range(3):
        for i in range(3):
            mitch.forward(10.0*size/3)
            mitch.backward(10.0*size/3)
            mitch.right(45)
        mitch.left(90)
        mitch.backward(10.0*size/3)
        mitch.left(45)
    mitch.right(90) 
    mitch.forward(10.0*size)
 
# loop to create 20 different sized snowflakes 
# with different starting co-ordinates
for i in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    sf_size = random.randint(1, 4)
    mitch.penup()
    mitch.goto(x, y)
    mitch.pendown()
    snowflake(sf_size)
 
wn.exitonclick()  

