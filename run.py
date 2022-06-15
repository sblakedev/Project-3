# import additional functions

import gspread
from google.oauth2.service_account import Credentials
import random
import os
import string
from time import sleep

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman')


def get_word():
    """
    Gets a random word from the google doc
    """
    list_of_words = SHEET.worksheet("words").get_all_values()
    list_word = random.choice(list_of_words)
    secret_word = " ".join(list_word)
    return secret_word


def welcome():
    """
    Welcomes user and explains the rules
    """
    print("Welcome to Hangman!\n")
    print("To play, guess the letters in a random 5 letter word.\n")
    print("You will have 7 lives.")
    print("If your letter is correct, your score will increase by one.")
    print("If your letter is incorrect, you will lose a life.\n")

    play = input("If you'd like to play, please press y\n")
    while True:
        if play == "y":
            main()
        else:
            print("Invalid character. Please enter y if you'd like to play.\n")

            # Clear terminal code from Scaler
            sleep(2)

            os.system('cls')
            os.system('clear')

            break
    welcome()


def get_name():
    """
    Gets the user to input their name
    """
    while True:
        name = input("Please enter your name:\n")
        if name.isalpha():
            print("Hello ", name, ". Let's play Hangman!\n")
            break
        else:
            print("Your name can only use letters. Please try again.\n")

    sleep(2)

    os.system('cls')
    os.system('clear')

    return name


def hangman():
    """
    Gets user input for guessing a letter
    Checks if the letter is in the word
    """
    secret_word = get_word()
    used_letters = set()  # user's guessed letters
    word_letters = set(secret_word)  # letters in the word
    alphabet = set(string.ascii_lowercase)
    lives = 7
    score = 0
    # Code from Kylie Ying YouTube tutorial
    while len(word_letters) > 0 and lives > 0:
        print("Your score is:", score)
        print("You have", lives, "lives left.\n")
        print("You have used these letters: ", " ".join(used_letters), "\n")
        word_list = [
            letter if letter in used_letters else "_" for letter in
            secret_word]
        print("Your word is: ", " ".join(word_list), "\n")
        guess = input("Please guess a letter:\n").lower()

        sleep(1)

        os.system('cls')
        os.system('clear')

        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                print("Correct!", guess, "is in the word!\n")
                word_letters.remove(guess)
                score = score + 1

            else:
                print("Sorry!", guess, "is not in the word.\n")
                print("You lose a life.\n")
                lives = lives - 1

        elif guess in used_letters:
            print("You have already guessed that letter. Please try again.\n")

        else:
            print("Invalid character. Please enter a letter.\n")

    if lives == 0:
        print("You have lost all of your lives.\n")
        print("The word was", secret_word, "\n")
    else:
        print("Congratulations! You guessed the word", secret_word, "!\n")


def play_again(name):
    """
    Asks user if they want to play again or not
    """
    while True:
        replay = input(f"Would you like to play again {name}?\n[y]es / [n]o\n")
        if replay == "y":
            sleep(1)

            os.system('cls')
            os.system('clear')

            get_word()
            hangman()

        elif replay == "n":
            sleep(1)

            os.system('cls')
            os.system('clear')

            print("Thank you for playing", name)

            sleep(1)

            os.system('cls')
            os.system('clear')

            welcome()

        else:
            print("Invalid character. Please enter y or n.\n")


def main():
    """
    Runs all functions
    """
    get_word()
    name = get_name()
    hangman()
    play_again(name)


welcome()
main()
