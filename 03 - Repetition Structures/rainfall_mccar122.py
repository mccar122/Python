"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 03.3 - Rainfall
Date: 09/16/2022

Description:
    This program collects data and calculates
    the average rainfall over a period of years

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
    years = int(input("Enter the number of years: ")) #Gets input from User
    i = 0
    years1 = years
    sum = 0
    average = 0
    if years1 == 0:
        print(f"Invalid input; years must be greater than 0.") #checks if year is 0
    while years > 0: #massive while statement to run
        i = i + 1
        print(f"  For year No. {i}")
        Jan = float(input("    Enter the rainfall for Jan.: "))
        while Jan < 0:
            print(f"    Invalid input; rainfall cannot be negative.")
            Jan = float(input("    Enter the rainfall for Jan.: "))
        Feb = float(input("    Enter the rainfall for Feb.: "))
        while Feb < 0:
            print(f"    Invalid input; rainfall cannot be negative.")
            Feb = float(input("    Enter the rainfall for Feb.: "))
        Mar = float(input("    Enter the rainfall for Mar.: "))
        while Mar < 0:
            print(f"    Invalid input; rainfall cannot be negative.")
            Mar = float(input("    Enter the rainfall for Mar.: "))
        Apr = float(input("    Enter the rainfall for Apr.: "))
        while Apr < 0:
            print(f"    Invalid input; rainfall cannot be negative.")
            Apr = float(input("    Enter the rainfall for Apr.: "))
        May = float(input("    Enter the rainfall for May.: "))
        while May < 0:
            print(f"    Invalid input; rainfall cannot be negative.")
            May = float(input("    Enter the rainfall for May.: "))
        Jun = float(input("    Enter the rainfall for Jun.: "))
        while Jun < 0:
            print(f"    Invalid input; rainfall cannot be negative.")
            Jun = float(input("    Enter the rainfall for Jun.: "))
        Jul = float(input("    Enter the rainfall for Jul.: "))
        while Jul < 0:
            print(f"    Invalid input; rainfall cannot be negative.")
            Jul = float(input("    Enter the rainfall for Jul.: "))
        Aug = float(input("    Enter the rainfall for Aug.: "))
        while Aug < 0:
            print(f"    Invalid input; rainfall cannot be negative.")
            Aug = float(input("    Enter the rainfall for Aug.: "))
        Sep = float(input("    Enter the rainfall for Sep.: "))
        while Sep < 0:
            print(f"    Invalid input; rainfall cannot be negative.")
            Sep = float(input("    Enter the rainfall for Sep.: "))
        Oct = float(input("    Enter the rainfall for Oct.: "))
        while Oct < 0:
            print(f"    Invalid input; rainfall cannot be negative.")
            Oct = float(input("    Enter the rainfall for Oct.: "))
        Nov = float(input("    Enter the rainfall for Nov.: "))
        while Nov < 0:
            print(f"    Invalid input; rainfall cannot be negative.")
            Nov = float(input("    Enter the rainfall for Nov.: "))
        Dec = float(input("    Enter the rainfall for Dec.: "))
        while Dec < 0:
            print(f"    Invalid input; rainfall cannot be negative.")
            Dec = float(input("    Enter the rainfall for Dec.: "))
        sum += Jan + Feb + Mar + Apr + May + Jun + Jul + Aug + Sep + Oct + Nov + Dec
        years = years - 1
    if years1 !=0:
        avg = sum / (years1 * 12)
        print(f"There are {years1 * 12} months.")
        print(f"The total rainfall was {sum:.2f} inches.")
        print(f"The monthly average rainfall was {avg:.2f} inches.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
