"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 09/11/2012

Description:
    The user to enter a number of seconds and then displays the total
    time entered in days, hours, minutes and seconds.

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


def main():
    num = int(input("Please enter a time in seconds: ")) #user input statement followed by a series of logical checks to return accurate amount of time
    if num < 60:
        print(f"  {num} seconds is less than one minute.") #event that it is exactly one minute 
    elif num == 60:
        print(f"  {num} seconds equals 1 minute(s).")
    elif num > 60 and num < 3600: 
        min = num // 60
        sec = num % 60
        if min != 0 and sec != 0:
            print(f"  {num:,} seconds equals {min} minute(s) and {sec} second(s).")
        else:
            print(f"  {num} equals {min} minute(s).")
    elif num >= 3600 and num < 86400:
        hr = num // 3600
        min = (num % 3600) // 60
        sec = (num % 3600) % 60
        if min != 0 and sec != 0:
             print(f"  {num:,} seconds equals {hr} hour(s), {min} minute(s) and {sec} second(s).")
        elif (hr != 0 and min != 0) and sec == 0:
            print(f"  {num:,} seconds equals {hr} hour(s) and {min} minute(s).")
        elif (hr != 0 and sec != 0) and min == 0:
            print(f"  {num:,} seconds equals {hr} hour(s) and {sec} second(s).")
        elif min == 0 and sec == 0:
            print(f"  {num:,} seconds equals {hr} hour(s).")
        else:
            print(f"  {num} equals {hr} hour(s).")
    else:
        days = num // 86400
        hr = (num % 86400) // 3600
        min = (num % 3600) // 60
        sec = (num % 3600) % 60
        if (hr != 0 and min != 0) and sec != 0:
            print(f"  {num:,} seconds equals {days} day(s), {hr} hour(s), {min} minute(s) and {sec} second(s).")
        elif (hr != 0 and min != 0) and sec == 0:
            print(f"  {num:,} seconds equals {days} day(s), {hr} hour(s) and {min} minute(s).")
        elif (hr != 0 and sec != 0) and min == 0:
            print(f"  {num:,} seconds equals {days} day(s), {hr} hour(s) and {sec} second(s).")
        elif (sec != 0 and min != 0) and hr == 0:
            print(f"  {num:,} seconds equals {days} day(s), {min} minute(s) and {sec} second(s).")
        elif hr != 0 and (sec == 0 and min == 0):
            print(f"  {num:,} seconds equals {days} day(s) and {hr} hour(s).")
        elif min != 0 and (sec == 0 and hr == 0):
            print(f"  {num:,} seconds equals {days} day(s) and {min} minute(s).")
        elif sec != 0 and (min == 0 and hr == 0):
            print(f"  {num:,} seconds equals {days} day(s) and {sec} second(s).")
        else:
            print(f"  {num:,} seconds equals {days} day(s).")
        
            

    



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
