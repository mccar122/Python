"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/07/2022

Description:
    Asks the user to enter the number of packages purchased.
    The program should then display the amount of the discount (if any) and the total amount of
    the purchase after the discount.

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


from random import sample


def main():
    amount = int(input("How many packages will be purchased: ")) #gets inputted amount from user
    if amount < 0: #makes sure its a possible amount
        print(f"  Invalid Input!")
    elif amount < 4: #logical checks based on the amount
        pct = 0 
        price = amount * 880 #raw sales amount
        discount = price * pct #awarded discoutn
        final = price - discount #final sales value
        print(f"  No discount applied.")
        print(f"  The total price to purchase {amount} packages is ${final:,.2f}.")
    elif amount >= 4 and amount <= 39:
        pct = 0.1
        price = amount * 880 
        discount = price * pct 
        final = price - discount 
        print(f"  {pct*100:.0f}% discount applied.")
        print(f"  The total price to purchase {amount} packages is ${final:,.2f}.")
    elif amount >= 40 and amount <= 199:
        pct = 0.15
        price = amount * 880 
        discount = price * pct 
        final = price - discount 
        print(f"  {pct*100:.0f}% discount applied.")
        print(f"  The total price to purchase {amount} packages is ${final:,.2f}.")
    elif amount >= 200 and amount <= 999:
        pct = 0.3
        price = amount * 880 
        discount = price * pct 
        final = price - discount 
        print(f"  {pct*100:.0f}% discount applied.")
        print(f"  The total price to purchase {amount} packages is ${final:,.2f}.")
    else:
        pct = 0.42
        price = amount * 880 
        discount = price * pct 
        final = price - discount 
        print(f"  {pct*100:.0f}% discount applied.")
        print(f"  The total price to purchase {amount} packages is ${final:10,.2f}.")
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
