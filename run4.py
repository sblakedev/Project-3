#import additional functions
import gspread
from google.oauth2.service_account import Credentials
import random
from IPython.display import clear_output
import string

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman')

list_of_words = SHEET.worksheet('words').get_all_values()
word = random.choice(list_of_words)
word_letters = set(word)
alphabet = set(string.ascii_uppercase)
lives = 7
score = 0
used_letters = set()

def play_game():
    """
    Welcomes user to the game.
    Explains how to play the game. 
    Asks user to enter their name.
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
    
    # Print dashes instead of letters for secret word
    for letter in word:
        secret_word = "_"*len(letter)
        print("Your word is", secret_word)
    
    # Ask user for guess    
    guess = input("Please guess a letter:\n").lower()
    
    if guess in word:
        used_letters.add(guess)
        print("Correct!", guess "is in the word!")
        score += 1
    
    print(used_letters)
        
        
    
    
play_game()