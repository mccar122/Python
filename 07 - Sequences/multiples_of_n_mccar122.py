"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 07.1 - Multiples of N
Date: MM/DD/YYYY

Description:
    Takes a list of numbers and returns the numbers evenly divisible by user inputter number

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

def multiples_of(x, array): #function to find multiples of num in array
    temp = []
    y = 0
    for i in range(len(array)):
        if array[i] % x == 0:
            temp.append(array[i])
    return(temp)

def main():
    tstarr = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406] #initialized array given
    num = 13 #initial num given
    rslt = multiples_of(num, tstarr) #function call
    print(f"Original list of numbers:\n  {tstarr}")
    print(f"Numbers in the list that are multiples of {num}:\n  {rslt}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
