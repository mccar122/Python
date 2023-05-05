"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 10/01/2022

Description:
    This gets you the prime numbers. It would be cooler if it was optimous prime but its alright i guess.

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
def is_prime(num): #this determines whether its a prime number 
    if num == 0 or num == 1:
        return bool(False)
    for i in range(2, int((pow(num, 0.5)+1))):
        if (num % i) == 0:
            return(bool(False))
    return(bool(True))


def main():
    num = 0 #intializes the array
    while num != -1:
        num = int(input("Enter a positive integer (-1 to quit): ")) #user input section 
        if num != -1: 
            prime = is_prime(num) #calls sub function to check if it is a prime number lol
            if prime == True:
                print(f"  {num} is prime!")
            else:
                print(f"  {num} is not prime.")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
