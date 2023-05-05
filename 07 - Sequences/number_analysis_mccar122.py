"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 07.2 - Number Analysis
Date: MM/DD/YYYY

Description:
    Asks user for 10 values then returns statistics based on them. Avg, min, max, sum

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
def get_number_list(): #gets user inputted array values
    array= []
    for i in range(1,11):
        x = float(input(f"  number {i:2.0f} of 10: "))
        array.append(x)
    return(array)
    

def main():
    print(f"Enter 10 numbers:")
    x = get_number_list() #calls input array function
    total = sum(x)
    avg = sum(x) / len(x) #lines 44-47 get basic stats of array
    minum = min(x)
    maxi = max(x)

    print(f"Highest number: {maxi:.2f}")
    print(f"Lowest number: {minum:.2f}")
    print(f"Total: {total:.2f}")
    print(f"Average: {avg:.2f}")
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
