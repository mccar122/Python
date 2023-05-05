"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: MM/DD/YYYY

Description:
    Aquires sales data from the user and returns a pie chart of the sales data.

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
    #Gets inputs for sales in a year on monthly basis as floats 
    Jan = float(input("Enter the sales for January: "))
    Feb = float(input("Enter the sales for February: "))
    Mar = float(input("Enter the sales for March: "))
    Apr = float(input("Enter the sales for April: "))
    May = float(input("Enter the sales for May: "))
    Jun = float(input("Enter the sales for June: "))
    Jul = float(input("Enter the sales for July: "))
    Aug = float(input("Enter the sales for August: "))
    Sep = float(input("Enter the sales for September: "))
    Oct = float(input("Enter the sales for October: "))
    Nov = float(input("Enter the sales for November: "))
    Dec = float(input("Enter the sales for December: "))
    #sets pie chart colours
    colours = ["#4D4038", "#BAA892", "#5B6870", "#6E99B4", "#A3D6D7", "#085C11", "#849E2A", "#C3BE0B", "#E9E45B", "#6B4536", "#B46012", "#FF9B1A"]
    #Combines sales data
    sales = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec ]
    #initiates plot by calling library
    fig, ax = matplotlib.pyplot.subplots()
    #this creates the plot that prints pie chart
    ax.pie(sales, 
    colors = colours, 
    labels = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"))
    ax.set_title("Monthly Sales Values")
    matplotlib.pyplot.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
