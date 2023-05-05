"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 10/01/2022

Description:
     function should calculate and return the sum of the “lucky numbers” which are all of the numbers from
     the smallest argument to the largest argument that are not divisible by 3.

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
def lucky_sum(x,y):
    counter = min(x,y) #figures out which value is less
    sum = 0
    if x < y:
        while counter <= y:
            if counter % 3 != 0:
                sum += counter
            counter += 1
    else:
        while counter <= x:
            if counter % 3 != 0:
                sum += counter
            counter += 1
    return(sum)


def main():
    num1 = int(input("Enter the first integer: ")) #gets input from user
    num2 = int(input("Enter the second integer: ")) #gets input from user
    result = lucky_sum(num1, num2) #calls sub function
    print(f"The sum of the lucky numbers is {result:,}.") #returns result


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
