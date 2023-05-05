"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 10.3 - Covid 19 Cases
Date: MM/DD/YYYY

Description:
    This program takes COVID 19 data from a txt file and returns a informative plot for the user to use.

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
import matplotlib.pyplot
import datetime

"""Write new functions below this line (starting with unit 4)."""


def main():
    #Lines 38-52 opens txt file and pulls & formats data to be used for plotting
    data = open("indiana_covid-19_data_fall_2022.txt", "r")
    cases = []
    date = []
    total_cases = 0
    for line in data:
            count = 0
            for val in line.split():
                if count == 2: 
                    total_cases = total_cases + (float(val.strip()) / 1000)
                    cases.append(total_cases)
                if count == 0:
                    x, y, z = (val.strip()).split("-")
                    new_date = datetime.date(int(x), int(y), int(z))
                    date.append(new_date)
                count = count + 1
    data.close() #closes file
    ticks = [] #needed for plotting 
    x = 0
    while x < 2252: #makes list for y plot
        ticks.append(x)
        x = x + 250

    #This plots the data into a usable graph for the user
    fig, ax = matplotlib.pyplot.subplots()
    matplotlib.pyplot.bar(date, height = cases, width = 7)
    ax.set_ylim()
    ax.set_xlim()
    ax.set_title("Weekly Positive COVID-19 Cases in Indiana")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Cases (in thousands)")
    matplotlib.pyplot.yticks(ticks)
    matplotlib.pyplot.show()






"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
