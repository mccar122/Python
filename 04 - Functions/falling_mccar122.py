"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 04.1 - Falling
Date: 9/24/2022

Description:
    Are you falling or is the world around you elevating...#grind never stops

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
def falling_dist(x): #sub function calculating values
    d = (1/2) * 8.87 * x**2
    return(d)

def main(): #main fucnction with while loops to iterate
    print(f"Time (s)  Distance (m)")
    print(f"----------------------")
    i=5
    while i <= 50:
        p = falling_dist(i)
        print(f"{i:8}{p:14.1f}")
        i = i + 5



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
