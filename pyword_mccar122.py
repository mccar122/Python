"""
Author: Conor McCarthy, mccar122@purdue.edu
Assignment: 12.1 - Pyword
Date: MM/DD/YYYY

Description:
    Create a variation of the game Jotto (a predecessor to the hit game Wordle published in 1955). Present a menu with three options:
    Play New Game, View LeaderBoard, Quit Program

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
def pick_game_words(): 
    #This function gets a random 5 letter word to be the word guessed by player
    #print("Picking Words")
    list = open("words.txt", "r") #imports the txt file of possible words
    words =[] #list of possible words to chose from later
    for line in list:
        words.append((line.strip()))
    list.close()
    #randomly selects word
    secret_word = random.choice(words)
    #print(secret_word)
    return

def new_game():
    #This function creates a new game for the user to play 
    #print("New Game Selected")
    max_turns = 10
    current_turn = 1
    secret_word1 = pick_game_words()
    secret_word2 = pick_game_words()
    secret_word3 = pick_game_words()
    secret_word4 = pick_game_words()
    secret_word5 = pick_game_words()
    return

def home_menu(): 
    #prints the home menu for the user to interact with
    print(f"----- Main Menu -----")
    print(f"1. New Game")
    print(f"2. See Hall of Fame")
    print(f"3. Quit")
    choice = input("\nWhat would you like to do? ")
    return(choice)

def quitter():
    print(f"Goodbye.")

def view_league(): 
    #hall of fame leagues standings 
    print(f"\n--- Hall of Fame ---")
    print(f" ## : Score : Player\n")

    return

def main():
    #Main function to facilitate the subfunctions needed for program to work
    print(f"Welcome to PyWord.\n")
    input = home_menu()
    i = 0 #variable to be used to determine whether or not the user has quit the program
    while i == 0: #while option 3 hasnt been chosen
        if input != "1" and input != "2" and input != "3": #ensuring a valid input
            print(f"\nInvalid choice. Please try again.\n")
            input = home_menu() #repromts intro statement 
        if input == "1": #puts the user into a new game
            new_game()
            input = home_menu()
        elif input == "2": #shows the user the leaderboard
            view_league()
            input = home_menu()
        elif input == "3": #quits the user from the program
            quitter()
            i = 1 #change control varaible to break the loop 





"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
