"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 09/11/2022

Description:
    sks the user to choose a pocket number, and then displays the color of that pocket (either green, red, or black)

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


"""Write new functions below this line (starting with unit 4)."""


def main():
    num = int(input("Please choose a pocket number: ")) #user input line
    if num < 0: # sequence of logical checks 
        print(f"  Invalid Input!")
    elif num == 0:
        print(f"  Pocket number {num} is green.")
    elif num >= 1 and num <= 10:
        if num % 2 == 1:
            print(f"  Pocket number {num} is red.")
        else:
            print(f"  Pocket number {num} is black.")
    elif num >= 11 and num <= 18:
        if num % 2 == 1:
            print(f"  Pocket number {num} is black.")
        else:
            print(f"  Pocket number {num} is red.")
    elif num >= 19 and num <= 28:
        if num % 2 == 1:
            print(f"  Pocket number {num} is red.")
        else:
            print(f"  Pocket number {num} is black.")
    elif num >= 29 and num <= 36:
        if num % 2 == 1:
            print(f"  Pocket number {num} is black.")
        else:
            print(f"  Pocket number {num} is red.")
    else:
        print(f"  Invalid Input!")




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
