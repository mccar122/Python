"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 09/11/2022

Description:
    velocity of the water flowing through a pipe (V ), for the pipe’s diameter (d), and to select the water’s temperature (T ) 
    from 5 ◦C, 20 ◦C, and 50 ◦C. Your program should then calculate the Reynolds number based on the input values.

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
    t = float(input("Enter the temperature in °C as 5, 20, or 50: ")) #user inputted temperature
    v = float(input("Enter the velocity of water in the pipe (m/s): ")) #user inputted velocity of water
    d = float(input("Enter the pipe's diameter (m): ")) #user inputted diameter of tube

    if t == 5:
        Re = (v * d) / (1.52 * pow(10, -6))
    if t == 20:
        Re = (v * d) / (1.00 * pow(10, -6))
    if t == 50:
        Re = (v * d) / (5.54 * pow(10, -7))
    print(f"At {t}°C, the Reynolds number for flow at {v} m/s in a {d} m diameter pipe is {Re:.2e}.")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
