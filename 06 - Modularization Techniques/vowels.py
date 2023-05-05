"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 06.3 - Random Vowels
Date: MM/DD/YYYY

Description:
    Describe your program here.

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


def draw_a():
    penup()
    setheading(0)
    #forward(70)
    penup()
    forward(60)
    pendown()
    circle(30)
    penup()
    setheading(0)
    forward(30)
    setheading(90)
    forward(60)
    pendown()
    setheading(-90)
    forward(60)

def draw_e():
    penup()
    setheading(0)
    forward(70)
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

def draw_i():
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

def draw_o():
    penup()
    setheading(0)
    forward(50)
    pendown()
    circle(30)
    penup()
    setheading(0)
    forward(30)

def draw_u():
    penup()
    setheading(0)
    forward(50)
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

def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """You can use this function for your own testing. It will not be checked
    by the auto-grader."""
    draw_a()
    draw_e()
    draw_i()
    draw_o()
    draw_u()
    pass


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
