from turtle import *
import os
os.environ['TK_SILENCE-DEPRECATION']='1'
import tkinter

screen=Screen()



screen.title("Write your name")
screen.bgcolor("teal")
screen.setup(width=1000,height=400)

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
for i in range(180):
    a.forward(5)
    a.right(5)

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


# echo 'export TK_SILENCE_DEPRECATION=1'>> ~/.bash_profile

# echo 'export TK_SILENCE_DEPRECATION=1'>> ~/.zshrc
echo 'export TK_SILENCE_DEPRECATION=1'>> ~/.