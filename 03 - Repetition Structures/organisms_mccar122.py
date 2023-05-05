"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 03.4 - Organisms
Date: 09/24/2022

Description:
    predicts the approximate size of a population of organisms but honestly idk anymore my life is a joke.

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
    P0 = float(input("Starting population, in thousands: ")) #user input
    delta = float(input("Average daily increase, in percent: ")) #user input
    days = int(input("Number of days to multiply: ")) #user input
    i = 0
    delta = delta / 100
    pop = P0
    print(f"Day   Approx. Pop")
    while i <= days: #while loop for calcs
        print(f"{i:3}{pop:14,.3f}")
        pop += pop * delta
        i = i +1





"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
