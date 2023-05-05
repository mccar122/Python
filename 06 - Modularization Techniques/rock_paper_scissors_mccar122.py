"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 10/12/2022

Description:
    Rock Paper Scissor Spock minus the spock. Also its childish to think we can outgame a computer. But yes this is a rock paper scissors game.

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
def get_computer_choice(): #this function gets computers random input
    comp_val = random.randint(1,3)
    if comp_val == 1:
        return "rock"
    elif comp_val == 2:
        return "paper"
    elif comp_val == 3:
        return "scissors"

def get_player_choice(): #this gets the players input
    x = 1
    while (x==1):
        player_input = input("Choose rock, paper, or scissors: ")
        if player_input == "rock" or player_input == "paper" or player_input == "scissors":
            x = 0
        else:
            print(f"You made an invalid choice. Please try again.")
    return player_input

def get_winner(comp, player): #logical function to determine result
    if(comp == "rock" and player == "paper"):
        print(f"  paper beats rock")
        return "player"
    elif(comp == "paper" and player == "rock"):
        print(f"  paper beats rock")
        return "computer"
    elif(comp == "paper" and player == "scissors"):
        print(f"  scissors beats paper")
        return "player"
    elif(comp == "scissors" and player == "paper"):
        print(f"  scissors beats paper")
        return "computer"
    elif(comp == "scissors" and player == "rock"):
        print(f"  rock beats scissors")
        return "player"
    elif(comp == "rock" and player == "scissors"):
        print(f"  rock beats scissors")
        return 'computer'
    else:
        return 'tie'

def main(): #calls all functions and returns results
    c = 1
    while (c == 1):
        comp = get_computer_choice()
        player = get_player_choice()
        print(f"  The computer chose {comp}, and you chose {player}.")
        dub = get_winner(comp, player)
        if dub == "computer":
            print(f"  You lost.  Better luck next time.")
            print(f"Thanks for playing.")
            c = 69
        elif dub == "player":
            print(f"  You won the game!")
            print(f"Thanks for playing.")
            c = 420
        else:
            print(f"  It's a tie. Starting over.\n")

        


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
