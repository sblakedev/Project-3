## Hangman Game

This is a Hangman game created in Python. It runs in the Code Institute mock terminal on Heroku. 

---

### Table of Contents
  * [Responsive Mockup](https://github.com/sblakedev/Project-2#responsive-mockup)
  * [User Experience](https://github.com/sblakedev/Project-2#user-experience)
  * [Features](https://github.com/sblakedev/Project-2#features)
  * [Technologies Used](https://github.com/sblakedev/Project-2/blob/main/README.md#technologies-used)
  * [Testing](https://github.com/sblakedev/Project-2#testing)
  * [Future Features](https://github.com/sblakedev/Project-2/blob/main/README.md#future-features)
  * [Deployment](https://github.com/sblakedev/Project-2#deployment)
  * [Credits](https://github.com/sblakedev/Project-2#credits)

---

### Responsive MockUp
![Responsive MockUp](assets/images/readme/ResponsiveDesign.PNG)

---

### User Experience
#### User Stories
* User Goals
    a. As a User, I want to understand the main purpose of the site.
    b. As a User, I want to be given an option to play the game or not.
    c. As a User, I want to understand the rules of the game.
    d. As a User, I want to be able to guess a letter and know that the game recognises my choice.
    e. As a User, I want to be able to see how many guesses I have made and see my current score.
    f. As a User, I want to be able to get my final score when the game is finished.
    g. As a User, when the game is finished, I want to be able to choose to play again or exit the game.
    h. As a User, I want to be able to exit the game at any point.

<!--#### Design
* Colour Scheme
    * The two main colours used are Red and Yellow. Red and yellow are synonomous with the Harry Potter series so they are good choices for the purpose of this website. 
* Typography
    * The Abel font is the main font used throughout the website with Sans Serif as the fallback font in case the font isn't being imported to the site correctly. It is clean, simple and easy to read and is similar to the original font associated with Harry Pooter.
* Wireframes
    * ![Desktop Wireframe](assets/images/readme/Potter%20Quiz%20Desktop%20Wireframes.PNG)
    * ![Tablet Wireframe](assets/images/readme/Potter%20Quiz%20Tablet%20Wireframes.PNG)
    * ![Phone Wireframe](assets/images/readme/Potter%20Quiz%20Phone%20Wireframes.PNG)-->

---

### Features
#### Heading
![Heading](assets/images/readme/Heading.PNG)
* The heading appears at the top of the page
* If a user clicks the heading, they can return to the Welcome Area

#### Welcome Area and Start Button
![Welcome Area and Start Button](assets/images/readme/WelcomeArea-and-StartButton.PNG)
* The welcome area welcomes the user to the site
* The user can start the quiz by clicking the Start Button

#### Question Area and Score Area
![Question Area and Score Area](assets/images/readme/QuestionArea.PNG)
* This area contains the question and 4 possible answers.
* Once the user clicks on an answer, they will be taken to the next question.
* If the user clicks the correct answer, the background on that answer turns green.
* If the user clicks the incorrect answer, the background on that answer turns red.
* The score area shows the user's score.
![User's current score](assets/images/readme/CurrentScore.PNG)
* The score area also shows how many questions the user has answered out of 10.
![Question count](assets/images/readme/QuestionNumber.PNG)

#### Results Area and Play Again Button
![Results Area and Play Again Button](assets/images/readme/ResultsArea.PNG)
* The results area shows the user's results based on their score out of ten. Possible results are Outstanding, Exceeds Expectations, Acceptable, Pass and Troll.
* The results area also contains the play again button. When the user clicks the play again button, it will refresh the quiz score and bring the user back to the welcome area.

#### Footer
![Footer](assets/images/readme/Footer.PNG)
* The footer section includes links to the relevant social media sites for the quiz website. The links will open to a new tab to allow easy navigation for the user. The footer is valuable to the user as it enables them to contact the site owners if needed.

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
The W3C Markup Validator, W3C CSS Validator Services and JSHint were used to validate every page of the project to ensure there were no syntax errors in the project.
* HTML
![HTML Validation](assets/images/readme/HTMLValidation.PNG)
* CSS
![CSS Validation](assets/images/readme/CSSValidation.PNG)
* Javascript
![JavaScript Validation](assets/images/readme/JSValidation.PNG)

#### User Stories Testing
a. As a visitor, I want to understand the main purpose of the site.
   * As a visitor, I understand that this is a Harry Potter quiz site which will give me a result based on my final score.

b. As a visitor, I want to be able to navigate easily around the site and start the quiz.
   * As a visitor, I see that I can start the quiz by clicking the start button.

c. As a visitor, I want to be able to read the question and see relevant answers.
   * As a visitor, I can see the question and 4 different answers relevant to the question.

d. As a visitor, I want to be able to answer the question and know that the site recognises my choice.
   * As a visitor, I can see that the box changes when I hover over an answer. If I get the answer correct, the box flashes green. If I get the answer wrong, the box flashes red.

e. As a visitor, I want to be able to see how many questions I have answered and see my current score.
   * As a visitor, I can see under the answers, how many questions out of 10 that I have answered and what my current score is.

f. As a visitor, I want to be able to get my final result when the quiz is finished.
   * As a visitor, after I have answered all 10 questions, I can see the box that contains my score and what my result is based on this score. If I do the quiz again and get a different score, the result may change to reflect the new score.

g. As a visitor, I want to be able to easily get in contact with the site creator in case I have any issues with the site.
   * As a visitor, I can see the relevant social media links which I can open in a new window to contact the owner of the quiz site.

#### Element Testing
* Heading
    * Expected Result
        When the heading "Harry Potter Quiz" is clicked, the user should be returned to the Welcome Area.
    * Testing
        When the heading "Harry Potter Quiz" is clicked, the user is returned to the Welcome Area.
* Start Button
    * Expected Result
        When the start button is clicked, the user should be taken to the question area which should display the question and 4 relevant answers.
    * Testing
        When the start button is clicked, the user is taken to the question area which displays the question and 4 relevant answers.
* Answer Box
    * Expected Result
        When the user hovers over an answer, the border should change thickness and colour. When the answer is clicked, if it correct, the box should flash green before moving on to the next question. If the answer is incorrect, the box should flash red before moving on to the next question. When a question has been answered, the answer count below the answers, should increase by one. The score should also increase depending on whether the correct answer was chosen or not. When all questions have been answered, the user should be taken to the results page, where they are shown a result which corresponds to the score.
    * Testing
        When the user hovers over the answer, the border changes thickness and changes the colour to a dark red. When the correct answer is clicked, the box flashes green before showing the next question. When the incorrect answer is clicked, the box flashes red before showing the next question. When the next question shows, the answer count has increased by one. When a correct answer is chosen, the score increases. When an incorrect answer is chosen, the score stays as is. When all the questions have been answered, the user is taken to the results page which displays the user's score and a result which corresponds to the score. Re-starting the quiz and getting a different score changes the result.
* Play Again Button
    * Expected Result
        When the play again button is clicked, the user should be taken back to the welcome area with all scores and results refreshed.
    * Testing
        When the play again button is clicked, the user is taken back to the welcome area. When the start button is clicked, all scores and results have been refreshed.
#### Bugs
* ModuleNotFoundError: No module named 'gspread'
    * Install new version of pip (pip-22.1.2) - python -m pip install --upgrade pip
    * Install gspread.

* After entering username and getting user validation, program asks for username again
    * Put a break in to if statement in while loop.

* TypeError: object of type 'Worksheet' has no len()

#### Lighthouse Report
![Lightouse Report](assets/images/readme/LighthouseReport.PNG)

---

### Future Features
In the future, features to include are:
  * User will be able to create a username
  * Add a high score board

---

### Deployment
#### GitHub Pages
I used the following steps to deploy the project.

1. Log in to Github and navigate to the repository.
2. On Github repository page, click on settings tab.
3. Scroll down to Pages tab on the menu on the left hand side.
4. Under Source, click the Branch drop down menu and select main.
5. Click Save.
6. The page will update and show the text "Your site is published at https://sblakedev.github.io/Project-2/"

#### Forking the Repository
To fork the repository in order to make a copy so as to view or make changes to the site without affecting the original repository, the following steps are to be used.

1. Log in to Github and navigate to the repository.
2. On the right hand side, above the setting tab, click the 'Fork' button.
3. There will now be a copy of the original respository in your GitHub account.

#### Cloning the Repository
To make a local clone, the following steps are to be used.

1. Log in to Github and navigate to the repository.
2. Above the list of files, click the 'Code' button.
3. Copy the link under HTTPS to clone using HTTPS.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone and then paste the link you copied earlier.
7. Press enter. Your local clone has been created.

---

### Credits
#### Code
  * CSS grid help: css-tricks.com and https://codepen.io/mogpt/pen/ebXdzg
  * Python guidance and some code from The Python Workshop for Beginners Part 2 Udemy video by [XXX](https://www.udemy.com/course/the-python-workshop-for-beginners-part-2/learn/lecture/21928888#overview)
  * Boilerplate code came from [Code Institute](https://github.com/Code-Institute-Org/gitpod-full-template/tree/main/.vscode)
  * Most issues in the code were resolved by searching through [Stack Overflow](https://stackoverflow.com/) and [W3Schools](https://www.w3schools.com/)

#### Media
  * Favicon from http://clipart-library.com/images_k/lightning-bolt-transparent-background/lightning-bolt-transparent-background-24.png

#### Content
  * 5 hard to guess words taken from https://danq.me/2013/12/15/hangman/

#### Acknowlegdements
  * Inspiration for ReadMe came from the Code Institute Sample ReadMe, Code Institue ReadMe template, my own Project 1 ReadMe and suggestions from my Project 1 assesor.
  * My mentor Martina Terlevic for fantastic guidance.
  * Slack community.
  * Code Institute Tutors - James, Sean and Oisin.