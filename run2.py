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


def get_valid_word(words):
    list_of_words = SHEET.worksheet('words').get_all_values()
    secret_word = random.choice(list_of_words)  # randomly chooses something from the list
    while '-' in secret_word or ' ' in secret_word:
        secret_word = random.choice(list_of_words)

    return secret_word()

def hangman():
    list_of_words = SHEET.worksheet('words').get_all_values()
    secret_word = random.choice(list_of_words)
    secret_letters = set(secret_word) # letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set() # what the user has guessed
    lives = 7
    
    # getting user input
    while len(secret_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left')
        print('You have used these letters: ', ' '.join(used_letters))
        
        # what current word is (ie w - r d)
        word_list = [letter if letter in used_letters else '-' for letter in secret_word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in secret_letters:
                secret_letters.remove(user_letter)
                print('')
                
            else:
                lives -= 1 # takes away a life if wrong
                print('Letter is not in word')

        elif user_letter in used_letters:
            print('You have already guessed that letter. Please try another letter.')
            
        else:
            print('Invalid character. Please enter a letter.')
            
            
    if lives == 0:
        print('You died! The word was', secret_word)
    else:
        print('You guessed the word', secret_word, '!')

   
if __name__ == '__main__':
    hangman()