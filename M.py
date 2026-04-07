import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
from turtle import *
screen=Screen()
screen.tracer(0)



screen.title("Write your name")
screen.bgcolor("#008080")
screen.setup(width=1000,height=400)
screen.getcanvas().winfo_toplevel().wm_attributes("-topmost", 1)
# yertle=Turtle()

# yertle.color("turquoise")
# yertle.shape("turtle")



# """"
# Movement 
# """
# # for j in range(4):
# #     for i in range(5):
# #         yertle.forward(10)
# #         yertle.penup()
# #         yertle.forward(10)
# #         yertle.pendown()
# #     yertle.left(90)




# # while True:
# #     angle=int(input("What heading would you yertle to face?"))
# #     yertle.setheading(angle)


# """
# Movement - Coordinates
# """
# bess=Turtle()
# bess.pu()
# bess.color("red")
# bess.goto(100,-100)



# yertle.pu()
# yertle.goto(-100,100)
# yertle.pd()
# yertle.sety(100)
# yertle.setx(100)
# yertle.goto(bess.position())
# yertle.goto(-100,-100)
# yertle.home()

#for i in range(180):
#      yertle.forward(1)
#     yertle.right(1)
# # yertle.circle(-50,180)

a=Turtle()

a.color("turquoise")
a.shape("turtle")


b=Turtle()

b.color("turquoise")
b.shape("turtle")

c=Turtle()

c.color("turquoise")
c.shape("turtle")

d=Turtle()

d.color("turquoise")
d.shape("turtle")

e=Turtle()

e.color("turquoise")
e.shape("turtle")
a.penup()
a.goto(-250, -50)
a.pendown()
a.color("magenta")
a.pensize(4)
a.setheading(90)
a.forward(100)
a.right(135)
a.forward(70)
a.left(90)
a.forward(70)
a.right(135)
a.forward(100)

b.penup()
b.goto(-100, 50)
b.pendown()
b.color("pink")
b.pensize(4)
b.goto(-100, -50)
b.penup()
b.goto(-120, 50)
b.pendown()
b.goto(-80, 50)
b.penup()
b.goto(-120, -50)
b.pendown()
b.goto(-80, -50)

c.penup()
c.goto(20, 50)
c.pendown()
c.color("yellow")
c.pensize(4)
c.setheading(180)
c.circle(50, 180)

d.penup()
d.goto(80, -50)
d.pendown()
d.color("lime")
d.pensize(4)
d.goto(120, 50)
d.goto(160, -50)
d.penup()
d.goto(100, 0)
d.pendown()
d.goto(140, 0)

e.penup()
e.goto(200, 50)
e.pendown()
e.color("white")
e.pensize(4)
e.goto(200, -50)
e.penup()
e.goto(200, 0)
e.pendown()
e.goto(280, 0)
e.penup()
e.goto(280, 50)
e.pendown()
e.goto(280, -50)



# for i in range(180):
#     a.forward(5)
#     a.right(5)
time.sleep(0.5)
screen.update()
screen.exitonclick()