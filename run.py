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
alphabet = set(string.ascii_lowercase)
score = 0
lives = 7
    
# test
print(secret_word)


def hangman():
    """
    Welcomes user and asks for user name
    Gets user input for guessing a letter
    Checks if the letter is in the word
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
    
    global lives
    global score
    
    # Code from Kylie Ying YouTube tutorial
    while len(word_letters) > 0 and lives > 0:
        print("Your score is:", score)
        print("You have", lives, "lives left.")
        print("You have used these letters: ", " ".join(used_letters))
        word_list = [
            letter if letter in used_letters else "_" for letter in
            secret_word]
        print("Your word is: ", " ".join(word_list))
        guess = input("Please guess a letter:\n").lower()
        
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                print("Correct!", guess, "is in the word!\n")
                word_letters.remove(guess)
                score = score + 1
            else:
                print("Sorry!", guess, "is not in the word.\n")
                print("You lose a life.")
                lives = lives - 1
            
        elif guess in used_letters:
            print('You have already guessed that letter. Please try again.')
            
        else:
            print('Invalid character. Please enter a letter.')
            
    if lives == 0:
        print("You have lost all of your lives.")
        print("The word was", secret_word)
    else:
        print("Congratulations! You guessed the word", secret_word, "!")

hangman()