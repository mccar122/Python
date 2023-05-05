"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: MM/DD/2022

Description:
    This program odwnlaods a txt file of states and caps and tests the user on their 5th grade knowledge.

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
def get_state_data():
    caps ={}
    states = open("state_capitals.txt", "r") #grabs txt file from folder
    for line in states:
        #line.strip()
        caps1 = ((line.strip()).split(", "))
        caps[caps1[1]] = caps1[0]
    states.close()
    return(caps) ##returns a modified dictionary to main

def main():
    capital = get_state_data() #gets dictionary information
    x = 1 #control variable
    correct = 0 #correct answer counter
    count = 0 #iteration counter

    while x == 1:
        state, cap = random.choice(list(capital.items()))
        question = input("What is the capital of " +state+ " (enter 0 to quit)? ")
        if question == "0":
            break
        elif cap.lower() == question.lower():
            print(f"  That is correct!")
            correct = correct + 1
        elif cap.lower() != question.lower():
            print(f"  That is incorrect.")
            print(f"  The capital of {state} is {cap}.")
        count = count + 1
        if count >= 10:
            x = 69
    print(f"You answered {correct} out of {count} questions correctly.")    
    







"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
