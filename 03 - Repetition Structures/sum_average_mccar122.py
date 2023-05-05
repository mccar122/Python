"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 03.2 - Sum Average
Date: 09/13/2022

Description:
    Asks the user to enter a series of non-negative numbers 
    (positive numbers or zero). The user should enter a 
    negative number to signal the end of the series. After 
    all the non-negative numbers have been entered, the 
    program should display their sum and average.

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


from itertools import count


def main():
    num = 0
    a = []
    sum = 0
    count = 0
    ticker = 0

    while num >= 0:
        num = float(input("Enter a non-negative number (negative to quit): ")) #gets input from user
        if num < 0 and len(a) == 0: #edge case user
            print(f"  You didn't enter any numbers.")
        elif num >= 0: #regular updates 
            a.append(num)
            ticker = ticker +1
    if len(a) != 0: #summation and average calculations
        for i in a:
            sum = sum + i
            count = count + 1
        avg = sum / count
        print(f"  You entered {ticker} numbers.")
        print(f"  Their sum is {sum:.3f} and their average is {avg:.3f}.")
    
        


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
