#import additional functions
import gspread
from google.oauth2.service_account import Credentials
import random
from IPython.display import clear_output

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman')


def welcome():
    """
    Welcomes user to the game.
    Explains how to play the game. 
    Asks user to enter their name
    """
    print("Welcome to Hangman!")
    print("To play, guess the letters in a random 5 letter word.")
    print("You will have 7 lives.")
    print("If your letter is correct, your points will increase by one.")
    print("If your letter is incorrect, you will lose a life.")

    name = input("Please enter your name:\n")
    if name.isalpha():
        print(f"Hello {name}. Let's play Hangman!")
    else:
        print("Your name can only use letters. Please try again.")
        return name
  

def play_game():
    """
    Retrieves a random word from the list of words document.
    Gets user input and validates input.
    If guess is correct, increase score by 1.
    If guess is incorrect, decrease lives by 1.
    """
    list_of_words = SHEET.worksheet('words').get_all_values()
    secret_word = random.choice(list_of_words)
    print(secret_word)  # test
    lives = 7
    wrong_guesses = 0
    guessed = 0
    guessed_letters = []
    game_over = False

    guesses = "_ " * len(secret_word)
    print(guesses)  # test
    
    print(secret_word)  # test

    guess = input("Please guess a letter:\n").lower()

    while guess in guessed_letters:
        print("You've already guessed that letter", guess)
        guess = input("Please guess a letter:\n").lower()

    guessed_letters.append(guess)

    if guess in secret_word:
        print(f"Correct! {guess} is in the word!")

    new_guesses = ""
    for letter in range(len(secret_word)):
        if guess == secret_word[letter]:
            new_guesses += guess
        else:
            new_guesses += 



    while not game_over:
        #output game information
        secret_word = "".join(guesses)
        print("Word to guess: {}".format(secret_word))
        print("Lives: {}".format(lives))
        guess = input("Type quit or guess a letter:\n").lower()
        if guess == "quit":
            print("Thanks for playing!")
            game_over = True


    for letter in range(len(secret_word)):
        if letter in str(secret_word):
            print(f"Correct! {guess} is in the word!")
        else:
            print(f"Sorry! You lose a life. {guess} is not in the word.")
    

def main():
    """
    Run all program functions
    """
    welcome()
    play_game()    


main()


"""start_game

guess_letter

check_letter

draw_hangman

lose_life

guess_all_letters

play_again"""

