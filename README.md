# Mini-projects

# ====================================

# Pong Game

A modern rendition of the classic Pong game built using Python's Turtle graphics. Play against a friend or challenge the computer!


## Table of Contents
- [Features](#pong-features)
- [Installation](#pong-installation)
- [Usage](#pong-usage)
- [Screenshots](#pong-screenshots)

<br>

<a name="pong-features"></a>
## Features
- **Two Modes:** Play against the computer or challenge your friend in a two-player duel!
- **Customizable Difficulty:** Adjust the game's difficulty level to fit your preference.
- **Dynamic Ball Speed:** The ball's speed dynamically increases during gameplay, with up to 15 escalating speed levels to challenge players.
- **Winner:** The first player to reach 10 points wins the game!
- **Graphics:** Enjoy the classic game with updated graphics and smooth gameplay.
- **Reset Functionality:** Easily reset the game at any point to start afresh. To switch between modes, simply restart the game.


<a name="pong-installation"></a>
## Installation
**Clone the repository:**

`git clone https://github.com/azashev/Mini-projects.git`

<br>

**Navigate to the Pong game directory:**

`cd Mini-projects/Pong`

<br>

**Run the game:**

`python main.py`


<a name="pong-usage"></a>
## Usage
- Use the arrow keys (Up and Down) to move the right paddle.
- Use the W and S keys to move the left paddle.
- Score by getting the ball past your opponent's paddle!
- As you play, watch out for the increasing ball speed, offering a progressively challenging experience.
- Click the Reset button to reset the game at any time.


For a two-player game:
Enter "p" for two-player mode.

Use the aforementioned controls to play against your friend.


For a single-player game against the computer:
Enter "c" for single-player mode.

Adjust the difficulty as per your preference.

Use the arrow keys to move your paddle.


- As you play, watch out for the increasing ball speed, offering a progressively challenging experience.
- Click the Reset button to reset the game at any time.


<a name="pong-screenshots"></a>
## Screenshots
<img src="https://github.com/azashev/Mini-projects/assets/102361003/7369dec6-3666-4885-92b1-6b11b24f081f" alt="Screenshot_13-pong" width="400"/>

<img src="https://github.com/azashev/Mini-projects/assets/102361003/b4073d8e-9836-4684-813a-bd955585937c" alt="Screenshot_11-pong" width="400"/>

<img src="https://github.com/azashev/Mini-projects/assets/102361003/58aeb72f-6c83-45c9-a05d-61c99310c9f2" alt="Screenshot_12-pong" width="400"/>

<img src="https://github.com/azashev/Mini-projects/assets/102361003/d0137ab5-bb96-48ce-a5d5-d143a2ef58cd" alt="Screenshot_15-pong" width="400"/>

<img src="https://github.com/azashev/Mini-projects/assets/102361003/faf8f17a-1518-4030-bb52-e63678bcf3a2" alt="Screenshot_14-pong" width="400"/> 

<img src="https://github.com/azashev/Mini-projects/assets/102361003/44d66598-8b13-4b22-ae60-e09f1f98921b" alt="Screenshot_14-pong" width="400"/> 

<br>

# =====================================

<br>

# Console Connect Four

A simple two-player connect four game.

## Table of Contents
- [Logic](#console-connect-four-logic)
- [Installation](#console-connect-four-installation)
- [Screenshots](#console-connect-four-screenshots)

<br>
  
<a name="console-connect-four-logic"></a>
## The main logic

A player wins when they connect four slots
The winning connected slots must be consecutive

A connection can be:

- Horizontal
- Vertical
- Diagonal

<img src="https://user-images.githubusercontent.com/102361003/212683358-9a1c3280-cec3-426a-80c1-9e10ed926c08.png" alt="connect-four" width="600"/>


<a name="console-connect-four-installation"></a>
## Installation
**Clone the repository:**

`git clone https://github.com/azashev/Mini-projects.git`

<br>

**Navigate to the Console Connect Four directory:**

`cd Mini-projects/"Console Connect Four"`

<br>

**Run the game:**

`python connect_four.py`

<br>

**Or test it on [Replit](https://replit.com/@azashev/Console-Connect-Four?v=1)**


<a name="console-connect-four-screenshots"></a>
## Screenshots

<img src="https://user-images.githubusercontent.com/102361003/212755152-c7d4b40e-f74d-436d-a535-76b6b77999a3.png" width="600"/>

<img src="https://user-images.githubusercontent.com/102361003/212755320-39ddfdea-c743-48e0-97d0-f3f29e0ee160.png" width="600"/>

<img src="https://user-images.githubusercontent.com/102361003/212755443-7c35b8c5-d891-4f2f-bbdb-4b38d0f7d89b.png" width="600"/>

<img src="https://github.com/azashev/Mini-projects/assets/102361003/7e99e1cb-9460-4d82-a941-2b5e0811ae74" alt="connect-four" width="600"/>

<br>

# =====================================

<br>

# Custom Hangman Game

Guess 3 words with the option to use hints, and keep as many points as you can!

## Table of Contents
- [Rules](#custom-hangman-rules)
- [Installation](#custom-hangman-installation)
- [Screenshots](#custom-hangman-screenshots)

<br>
  
<a name="custom-hangman-rules"></a>
## Rules
- You start with 90 points.
- Guess letters one by one or guess the whole word (a-Z, case insensitive).
- Reveal a random letter by typing `hint!` instead of a letter to help you guess a word. Every hint reduces your points by 10.
- You get 1 hint for short words (words with 5 or less symbols) and 3 for longer ones.
- The first and the last letters of the word will be revealed.
- The hints and the hangman stages reset with each word.
- Each new stage (8 total) comes after a failed guess.
- You lose if you fail to guess a word.
- Guess 3 words and keep as many points as you can!

<img src=https://user-images.githubusercontent.com/102361003/214130208-dc008749-67f8-48c7-b042-f82f3a1788fa.png width="650">


<a name="custom-hangman-installation"></a>
## Installation
**Clone the repository:**

`git clone https://github.com/azashev/Mini-projects.git`

<br>

**Navigate to the Custom Hangman directory:**

`cd Mini-projects/Hangman`

<br>

**(Optional but Recommended) Set up a virtual environment:**

`python -m venv venv`

`source venv/bin/activate`

On Windows:

`venv\Scripts\activate`

<br>

**Install the required packages:**

`pip install pyfiglet`

<br>

**Run the game:**

`python hangman.py`

<br>

**Or test it on [Replit](https://replit.com/@azashev/Custom-Hangman-Game?v=1)**

<a name="custom-hangman-screenshots"></a>
## Screenshots

<img src=https://user-images.githubusercontent.com/102361003/214130458-05381497-ca81-4451-9613-e991249ff7f3.png alt="custom-hangman1" width="600">

<img src=https://user-images.githubusercontent.com/102361003/214130521-68c36620-7643-4237-b6ae-1358480760c4.png alt="custom-hangman2" width="600">

<img src=https://user-images.githubusercontent.com/102361003/214130608-4054b0e7-1dc2-465d-a043-390048291f07.png alt="custom-hangman3" width="600">

<img src=https://user-images.githubusercontent.com/102361003/214130661-b6464807-4381-4a5f-8a21-3ffe0acb3327.png alt="custom-hangman4" width="600">

<img src=https://user-images.githubusercontent.com/102361003/214130717-619c7e21-ee14-4e37-a60f-bb6b16ab9e5c.png alt="custom-hangman5" width="600">

<img src=https://user-images.githubusercontent.com/102361003/214130817-367d6da6-7bf6-4136-bb0d-00de352abf2c.png alt="custom-hangman6" width="600">

<img src=https://user-images.githubusercontent.com/102361003/214130938-5a2c570e-fc7e-40e7-8f95-152d4f50f85a.png alt="custom-hangman7" width="600">

<br>

# =====================================

<br>
