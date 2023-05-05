"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 10.2 - Gas Prices
Date: MM/DD/YYYY

Description:
    This code imports Gas Prices from a TXT file and then returns a plot to show average price by week.

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
import matplotlib.pyplot


"""Write new functions below this line (starting with unit 4)."""


def main():
    #imports data
    data = open("2008_Weekly_Gas_Averages.txt", "r")
    #sets and fills price values
    prices =[]
    for line in data:
        prices.append(float(line.strip()))
    data.close()
    #sets and fills week count
    weeks = []
    i = 1
    while i < 53:
        weeks.append(i)
        i = i + 1
    #initializes and then plots values needed
    fig, ax = matplotlib.pyplot.subplots()
    ax.margins = 0
    ax.set_title("2008 Weekly Gas Prices")
    ax.set_xlabel("Weeks (by number)")
    ax.set_ylabel("Average Price (dollars/gallon)")
    ax.set_ylim(1.5, 4.25)
    ax.set_xlim(1, 52)
    ax.grid()
    ax.plot(weeks, prices)
    matplotlib.pyplot.show()
        




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
