"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/07/2022

Description:
    Determine if the year given is a leap year and then returning number of days in february.

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
    year = int(input("Enter a year: ")) #input by user giving year converted to int
    if year % 4 == 0 and year % 100 != 0: #first possible condition
        print(f"The year {year} is a leap year.") #printed result
        print(f"February of {year} has 29 days.") #printed result
    elif year % 4 == 0 and year % 400 == 0: #second possible condition
        print(f"The year {year} is a leap year.") #printed result
        print(f"February of {year} has 29 days.") #printed result
    else: #if not a leap year
        print(f"The year {year} is not a leap year.") #printed result
        print(f"February of {year} has 28 days.") #printed result


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
