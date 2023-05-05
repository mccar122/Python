"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 06.3 - Random Vowels
Date: MM/DD/YYYY

Description:
    This function will import the turtle drawings from vowels and randomly draw some of them

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

"""Import modules below this line (starting with unit 6)."""
from turtle import *
import random
import vowels



"""Write new functions below this line (starting with unit 4)."""


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
    array= [1, 2, 3, 4, 5] #making arrawy    
    ranArray = random.sample(array, 5) #filling empty array with ran values
    for i in ranArray: #loop to draw
        if  i == 1:
            vowels.draw_a()
        elif i == 2:
            vowels.draw_e()
        elif i == 3:
            vowels.draw_i()
        elif i == 4:
            vowels.draw_o()
        elif i == 5:
            vowels.draw_u()    

    


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
