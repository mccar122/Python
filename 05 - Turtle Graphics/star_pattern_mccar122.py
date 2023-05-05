"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 05.3 - Star Pattern
Date: MM/DD/YYYY

Description:
    Here this program will draw a star based on how many points you give it.

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


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()


def main():
    s = int(input("How many points are on your star? ")) #inout statement by the user for num of points
    A = 360/s
    B = 2 * A
    i = 0
    
    color('black', 'pink') #line color and fill color
    begin_fill()
    right((180 - B) / 2)
    while i < (2 * s): #while loop to exectue the commands
        forward(60)
        i = i +1
        if i % 2 == 0:
            right(180 - B)
        else:
            left(180 - A)
        
    end_fill()


"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
