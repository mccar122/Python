"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 01.2 - Interest
Date: 08/29/2022

Description:
    Calculate Loan Amounts based on principle, rate, year, and compounding amount. Man I wish the banking system was this simple but
    this is a good model for Algebra 2 students to understand rates. This program is scalable. 

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
    print("Enter the following parameters.")
    P = float(input("  The initial deposit? ")) #initial amount in account
    R = float(input("  The annual interest rate in percent? "))#interest rate
    T = float(input("  The number of years the account earn interest? "))#number of years 
    N = float(input("  The number of times interest is compounded each year: "))#number of times compounded a year

    FV = P * (1 + ((R/100) / N)) ** (N*T) #calc new value
    FV = "{:,.2f}".format(FV) #format new value
    print(f"The balance of this account will be ${FV} after {T} years.")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
