"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 08/29/2022

Description:
    Based on the input of how many cookies you want to make the program will tell you how much butter, sugar, and flour you'll need.

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
    num = int(input("How many cookies do you want to make? ")) # inputs number of desired cookies
    butter = num * (1.25/48) #calculates necessary ingredients based on ratio
    sugar = num * (1.5/48) #calculates necessary ingredients based on ratio
    flour = num * (2.5/48) #calculates necessary ingredients based on ratio
    #butter = "{:,.2f}".format(butter) #formatting line
    #sugar = "{:,.2f}".format(sugar) #formatting line
    #flour = "{:,.2f}".format(flour) #formatting line
    num = "{:,}".format(num) #formatting line
    print(f"To make {num} cookies, you will need:")
    print(f"{butter:10,.2f} cups of butter")
    print(f"{sugar:10,.2f} cups of sugar")
    print(f"{flour:10,.2f} cups of flour")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
