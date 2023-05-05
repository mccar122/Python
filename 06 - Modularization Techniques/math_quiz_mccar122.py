"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 10/12/2022

Description:
    a program that gives the user a simple math quiz. The program should display a random two digit number and a random three digit number.

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
import random

"""Write new functions below this line (starting with unit 4)."""
def random_number(val):
    int = random.randint(10**(val-1),(10**val)-1) #generates a random number to dependent on input val 
    return int

def main():
    x = random_number(2) #2digit number call
    y = random_number(3) #3 digit number call
    print(f"   {x}")
    print(f"+ {y}")
    print(f"-----")
    z = int(input("= ")) #asks for user input
    if z == x+y:
        print(f"Correct -- Good Work!")
    else:
        print(f"Incorrect. The correct answer is {x+y}.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
