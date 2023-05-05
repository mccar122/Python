"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: MM/DD/YYYY

Description:
    This program shows the probability of getting a certain sum of 2 dice. 

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
import random

"""Write new functions below this line (starting with unit 4)."""
def roll_d6(): #gets value of single roll
    num = random.randint(1,6)
    return(num)

def get_2d6_rolls(val): #gets sum of 2 rolls up to 1000000
    array = []
    for i in range(val):
        n1 = roll_d6()
        n2 = roll_d6()
        sum = n1 + n2
        array.append(sum)
    return(array)

def main():
    n = 1000000 #num of rolls
    sums = []
    kek = get_2d6_rolls(n)
    for i in range(1, 13):
        sums.append(kek.count(i+1) /n * 100) #counts every instance in array kek
    print(f"Roll  Frequency")
    
    for i in range(11): #print for loop
        print(f" {i+2:2.0f}   {sums[i]:6.2f}%")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
