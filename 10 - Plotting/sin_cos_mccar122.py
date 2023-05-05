"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 10.4 - Sin Cos
Date: MM/DD/YYYY

Description:
    This program prints sin and cosine on a graph for the user to see. Thats it

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
import numpy

"""Write new functions below this line (starting with unit 4)."""


def main():
    #gets basic sine / cosine range
    range = numpy.arange(0 , 2 * numpy.pi, 0.1)
    #makes sine and cosine variables generated to be printed
    sin = numpy.sin(range)
    cos = numpy.cos(range)
    #plotting and formatting of plots to get correct graph
    fig, ax = matplotlib.pyplot.subplots()
    ax.plot(range, cos, color= 'red')
    ax.plot(range, sin, color= 'blue')
    matplotlib.pyplot.xticks((0.5 * numpy.pi, numpy.pi, 1.5 * numpy.pi, 2 * numpy.pi), ('$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$'))
    matplotlib.pyplot.yticks((-1, 1))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    matplotlib.pyplot.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
