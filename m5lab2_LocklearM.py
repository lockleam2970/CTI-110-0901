#CTI-110
#M5T1 Initials
#Mitchell Locklear
#10/14/2017


import turtle

turtle.shape("circle")
turtle.color("blue")
turtle.pensize("10")
for M in [0,1]:
    
    turtle.left(90)
    turtle.forward(40)
    turtle.right(45)
    turtle.back(40)
    
    
turtle.penup()
turtle.goto(50,0)
turtle.pendown()

for L in [0,1]:
    turtle.forward (40)
    turtle.back (40)
    turtle.right (90)
#period between initials    
turtle.penup()
turtle.goto(30,0)
turtle.pendown()
turtle.forward (1)
#period at end of initials
turtle.penup()
turtle.goto(120,0)
turtle.pendown()
turtle.forward(1)
turtle.hideturtle()

turtle.exitonclick()
