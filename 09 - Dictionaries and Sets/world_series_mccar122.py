"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 09.2 - World Series
Date: MM/DD/2022

Description:
    This program will tell you the world series champion in a given year. Houston Astros are a bunch of cheaters

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
def load_winners_data(): #creates 2 dictionaries to reference later on
    winners = {} 
    yearly = {}
    start = 1903
    end = 2021
    champs = open("WorldSeriesWinners.txt", "r")
    for line in champs:
        if start == 1904 or start == 1994:
            start = start + 1
        yearly[start] = line.strip()
        start = start + 1
        if line.strip() not in winners:
            winners[line.strip()] = 1
        else:
            winners[line.strip()] = winners[line.strip()] + 1
    champs.close()
    return(winners, yearly)

def main():
    year = int(input("Enter a year in the range 1903 -- 2021: ")) #gets user input
    winners, yearly = load_winners_data()
    if year == 1904 or year == 1994: #runs 2 test cases to make sure yr valid then fetches info 
        print(f"  The World Series wasn't played in the year {year}.")
    elif year < 1903 or year > 2021:
        print(f"  Data for the year {year} is not included in this system.")
    else:
        count = yearly[year]
        winner = winners[count]
        print(f"  The {count} won the World Series in {year}.")
        print(f"  They have won the World Series {winner} times.")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
