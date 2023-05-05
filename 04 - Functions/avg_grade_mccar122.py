"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 10/01/2022

Description:
     program should display a letter grade after each score is 
     entered. After all the scores are entered, it should 
     display the average of the scores and the letter grade 
     corresponding to that average

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
from statistics import mean


def get_valid_score(): #this gets the score form the user
    score = float(input("Enter a score: "))
    while score < 0.00 or score > 100.00:
        print("  Invalid Input. Please try again.")
        score = float(input("Enter a score: "))
    return(score)

def calc_average(score): #calcs the average grade
    avg = float(mean(score))
    return(avg)

def determine_grade(x): #this function determines the grade of everyone
    if x >= 92:
        return("A")
    elif x >= 82:
        return("B")
    elif x >= 73:
        return("C")
    elif x >= 64:
        return("D")
    else:
        return("F")

def main():#this function calls all fucntions to get the results also this code annoys the crap outta me cause it doesnt add up
    score = []
    for i in range(5):
        score.append(get_valid_score())
        grade = determine_grade(score[i])
        print(f"  The letter grade for {score[i]:.1f} is {grade}.")
    endscore = calc_average(score)
    alpha = determine_grade(endscore)
    print(f"\nResults:")
    print(f"  The average score is {endscore:.2f}.")
    print(f"  The letter grade for {endscore:.2f} is {alpha}.")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
