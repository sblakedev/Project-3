# import additional functions
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
list_of_words = SHEET.worksheet("words").get_all_values()
list_word = random.choice(list_of_words)
secret_word = " ".join(list_word)
used_letters = set()  # user's guessed letters
    
# test
print(secret_word)


def hangman():
    """
    Gets user input for guessing a letter
    Checks if the letter is in the word
    """
    guess = input("Please guess a letter:\n").lower()
    used_letters.add(guess)
    
    if guess in secret_word:
        print("Correct!", guess, "is in the word!\n")
    else:
        print("Sorry!", guess, "is not in the word.")
        print("You lose a life.")

hangman()