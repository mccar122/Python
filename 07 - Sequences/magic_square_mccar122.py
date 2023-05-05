"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 07.4 - Magic Square
Date: MM/DD/YYYY

Description:
    This determines which of the three squares is a lucky square. NO TRIANGLES!!!!

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
import numpy


"""Write new functions below this line (starting with unit 4)."""
def print_square(x): #prints square to be seen by avg puddy enjoyers
    r1 = x[0][:]
    r2 = x[1][:]
    r3 = x[2][:]
    for i in x: 
        print(" ", end = "")
        y = 1
        for j in i:
            while y < 2:
                #print(f"{j}", end = "")
                y = y +10000000
            if y != 1:
                print(f" {j}", end = "")
        print("")
    return()
        

def is_magic(x): #determines if it fits criteria 
    rows = numpy.sum(x, axis = 0) #immported function to sum rows
    cols = numpy.sum(x, axis = 1) #immported function to sum cols
    #print(f"{rows} and {cols}")
    diag = x[0][0] + x[1][1]+ x[2][2]
    diag2 = x[0][2] + x[1][1]+ x[2][0]
    #print(f"{diag} and {diag2}")
    c1 = x[0][0] == x[1][1]
    r = 1
    c = 1
    for i in rows:
        if i != 15:
            r = 0
    for i in cols:
        if i != 15:
            c = 0
    if r == 1 and c == 1 and diag == 15 and diag2 == 15 and c1 == 0:
        return(True)
    else:
        return(False)
def printing(x):
    if x == True:
        print(f"It is a Lo Shu magic square!\n")
    elif x == False:
        print(f"It is not a Lo Shu magic square.\n")


def main():
    x1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
    x2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    x3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    print(f"Your square is:")
    p1 = print_square(x1)
    test = is_magic(x1)
    printing(test)
    print(f"Your square is:")
    p2 = print_square(x2)
    test2 = is_magic(x2)
    printing(test2)
    print(f"Your square is:")
    p3 = print_square(x3)
    test3 = is_magic(x3)
    printing(test3)


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
