"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 05.4 - Mississippi Turtles
Date: 10/17/2022

Description:
    This code writes the word mississippi turtles using the basic functions in import turtles. This was fun n hard to write.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
from turtle import *

"""Write new functions below this line (starting with unit 4)."""
x = 0

def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    color("purple")
    speed(0)


def draw_e(): #draws e
    penup()
    setheading(0)
    forward(70)
    setheading(90)
    forward(10)
    pendown()
    setheading(40)
    circle(30, -300)
    setheading(180)
    forward(58)
    penup()
    setheading(-90)
    forward(35)
    setheading(0)
    forward(60)


def draw_i(): #draws i
    penup()
    setheading(0)
    forward(20)
    setheading(90)
    forward(50)
    setheading(-90)
    pendown()
    forward(50)
    penup()
    setheading(90)
    forward(70)
    setheading(0)
    pendown()
    circle(2, 360)
    penup()
    setheading(-90)
    forward(70)


def draw_l(): #draws l
    penup()
    setheading(0)
    forward(20)
    setheading(90)
    forward(120)
    pendown()
    setheading(-90)
    forward(120)



def draw_M(): #draws m
    penup()
    goto(-290, 120)
    pendown()
    goto(-290, 40)
    penup()
    goto(-290, 120)
    pendown()
    setheading(-90)
    circle(15, -180)
    setheading(-90)
    circle(15, -180)
    penup()
    goto(-260, 120)
    pendown()
    goto(-260, 40)
    penup()
    goto(-230, 120)
    pendown()
    goto(-230, 40)


def draw_p(): #draws p
    penup()
    setheading(0)
    forward(22)
    setheading(-90)
    forward(60)
    pendown()
    setheading(90)
    forward(110)
    setheading(-90)
    forward(30)
    circle(25, 360)
    penup()
    setheading(-90)
    forward(20)
    setheading(0)
    forward(50)


def draw_r(): #draws r
    penup()
    setheading(0)
    forward(20)
    pendown()
    setheading(90)
    forward(60)
    setheading(-90)
    forward(30)
    circle(30, -90)
    penup()
    setheading(-90)
    forward(60)


def draw_s(): #draws s
    penup()
    setheading(0)
    forward(20)
    pendown()
    forward(20)
    circle(15, 180)
    setheading(180)
    forward(15)
    circle(-15, 180)
    forward(20)
    penup()
    setheading(-90)
    forward(60)


def draw_t(): #draws t 
    global x
    penup()
    if x == 0:
        setheading(180)
        forward(400)
        setheading(-90)
        forward(80)
        x = 1
    else:
        setheading(0)
        forward(60)
        x = 1
        setheading(90)
        forward(120)
        setheading(-90)
        pendown()
        forward(120)
        setheading(90)
        penup()
        forward(120)
        setheading(-90)
        pendown()
        forward(40)
        setheading(180)
        forward(40)
        setheading(0)
        forward(80)
        penup()
        setheading(-90)
        forward(80)
        return()
    pendown()
    forward(120)
    setheading(90)
    penup()
    forward(120)
    setheading(-90)
    pendown()
    forward(40)
    setheading(180)
    forward(40)
    setheading(0)
    forward(80)
    penup()
    setheading(-90)
    forward(80)

def draw_u(): #draws u
    penup()
    setheading(0)
    forward(20)
    setheading(90)
    forward(60)
    pendown()
    setheading(-90)
    forward(30)
    circle(30, 180)
    setheading(90)
    forward(30)
    setheading(-90)
    forward(60)


def main():
    draw_M()
    draw_i()
    draw_s()
    draw_s()
    draw_i()
    draw_s()
    draw_s()
    draw_i()
    draw_p()
    draw_p()
    draw_i()

    #Next Line
    draw_t()
    draw_u()
    draw_r()
    draw_t()
    draw_l()
    draw_e()
    draw_s()


"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
