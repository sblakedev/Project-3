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
word_letters = set(secret_word)  # letters in the word
alphabet = set(string.ascii_uppercase)
score = 0
lives = 7
    
# test
print(secret_word)


def hangman():
    """
    Gets user input for guessing a letter
    Checks if the letter is in the word
    """
    guess = input("Please guess a letter:\n").lower()
    used_letters.add(guess)
    
    # Code from Kylie Ying YouTube tutorial
    while lives > 0 and len(word_letters) > 0:
        print("You have", lives, "lives left.")
        print("You have used these letters: ", " ".join(used_letters))
        word_list = [
            letter if letter in used_letters else "_" for letter in
            secret_word]
        print("Your word is: ", " ".join(word_list))
        if guess in secret_word:
            print("Correct!", guess, "is in the word!\n")
        else:
            print("Sorry!", guess, "is not in the word.")
            print("You lose a life.")

hangman()