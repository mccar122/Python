"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 01.1 - Road Trip
Date: 08/29/2022

Description:
    This program calculates the cost of the road trip based on distance, fuel effeciency, and fuel cost.

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
    print("Road trip fuel cost estimator:")
    distance = float(input("  How far away is your destination (miles)? ")) #variable for distance for a single leg of trip
    fuel_cost = float(input("  What is the average price of gas (dollars per gallon)? ")) #variable for cost of fuel per gallom
    MPG = float(input("  What is the fuel efficiency of your vehicle (mpg)? ")) #variable for cars fuel efficiancy 

    cost = int((2 * distance) * (fuel_cost / MPG)) #calculates total cost

    print(f"\nThe fuel cost for this trip is approximately ${cost}.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
