## Hangman Game

This is a Hangman game created in Python. It runs in the Code Institute mock terminal on Heroku. 

---

### Table of Contents


---

### Responsive MockUp


---

### User Experience
#### User Stories
* User Goals
    1. As a User, I want to understand the main purpose of the site.
    2. As a User, I want to be given an option to play the game or not.
    3. As a User, I want to understand the rules of the game.
    4. As a User, I want to be able to guess a letter and know that the game recognises my choice.
    5. As a User, I want to be able to see how many guesses I have made and see my current score.
    6. As a User, when the game ends, I want to see what the word was.
    7. As a User, when the game is finished, I want to be able to choose to play again or exit the game.

---

### Features


---

### Technologies Used
#### Languages Used
* Python

#### Frameworks, Libraries & Progrmas Used
1. 
2. 
3. 
4. GitHub - This was used to store the projects code after being pushed from Git.
5. Git - This was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

---

### Testing
#### Validator Testing


#### User Stories Testing
1. As a User, I want to understand the main purpose of the site.
  * I understand that this site it a Hangman game as the first line of text says "Welcome to Hangman"
2. As a User, I want to be given an option to play the game or not.
  * There is the option to enter "y" if I want to play the game. If I type "n" or any other character, I'm brought back to the welcome page.
3. As a User, I want to understand the rules of the game.
  * The rules of the game are displayed on the welcome page.
4. As a User, I want to be able to guess a letter and know that the game recognises my choice.
  * When I enter a guess, the letter I chose is displayed. If it's right, it appears in a dashed word. If it's not, I get a message to say that the letter is not in the word.
5. As a User, I want to be able to see how many guesses I have made and see my current score.
  * At the start, my score and how many lives I have are displayed on screen. After each guess, they are updated and displayed on screen.
6. As a User, when the game ends, I want to see what the word was.
  * If I win or lose, the word to be guessed is displayed in full.
7. As a User, when the game is finished, I want to be able to choose to play again or exit the game.
  * When I finish the game I'm given the option to play again. If I choose to play again, I get a new word to guess and my score and lives are reset. If I choose not to play again, I'm taken back to the welcome page.


#### Element Testing



#### Bugs
* ModuleNotFoundError: No module named 'gspread'
    * Install new version of pip (pip-22.1.2) - python -m pip install --upgrade pip
    * Install gspread.

* TypeError: object of type 'Worksheet' has no len()
  * Convert random word from list_of_words to string by defining a new empty variable as " ".join(list_word), using .join which takes all items and joins them into a string.


---

### Future Features
In the future, features to include are:
  * User will be able to create a username
  * Add a high score board

---

### Deployment


---

### Credits
#### Code
  * Python guidance and some code from The Python Workshop for Beginners Part 2 Udemy video by [XXX](https://www.udemy.com/course/the-python-workshop-for-beginners-part-2/learn/lecture/21928888#overview)
  * Some Python code came from Kylie Ying https://www.youtube.com/watch?v=cJJTnI22IF8&t=615s
  * Clear terminal code came from [Scaler] (https://www.scaler.com/topics/how-to-clear-screen-in-python/)
  * Boilerplate code came from [Code Institute](https://github.com/Code-Institute-Org/gitpod-full-template/tree/main/.vscode)
  * Most issues in the code were resolved by searching through [Stack Overflow](https://stackoverflow.com/)

#### Content
  * 5 hard to guess words taken from https://danq.me/2013/12/15/hangman/

#### Acknowlegdements
  * Inspiration for ReadMe came from the Code Institute Sample ReadMe, Code Institue ReadMe template, my own Project 1 ReadMe and suggestions from my Project 1 assesor.
  * My mentor Martina Terlevic for fantastic guidance.
  * Slack community.
  * 