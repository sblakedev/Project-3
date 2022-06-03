import gspread
from google.oauth2.service_account import Credentials
import random

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
    
    while True:
        name = input("Please enter your name:\n")
        if name.isalpha():
            print(f"Hello {name}. Let's play Hangman!")
            break
        else:
            print("Your name can only use letters. Please try again.")
  

def random_word_selector():
    """
    Retrieves a random word from the list of words document
    """
    list_of_words = SHEET.worksheet('words')
    secret_word = random.choice(list_of_words)
    print("Your 5 letter word is: _____")
    return secret_word

def main():
    """
    Run all program functions
    """
    welcome()

main()


"""start_game

guess_letter

check_letter

draw_hangman

lose_life

guess_all_letters

play_again"""

