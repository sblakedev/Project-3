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

list_of_words = SHEET.worksheet('words').get_all_values()
word = random.choice(list_of_words)
word_letters = set(word)
lives = 7

def play_game():
    for letter in word:
        secret_word = "_"*len(letter)
        print(secret_word)
        
    
    
play_game()