<h1 align="left">Python Dice Game</h1>
<p align="left">
  Welcome to the Python Dice Game Readme! Here you will find all the information you need to get started with our program.
  <br> 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [👨‍💻 Description ](#-description-)
- [🏁 Getting Started ](#-getting-started-)
- [Features of our game](#features-of-our-game)
  - [How to create and run the virtual environment](#create-and-run-the-virtual-environment)
  - [Installing](#installing)
    - [Installing make and chocolatey using Windows](#installing-make-and-chocolatey-using-windows)
    - [How to do testings](#testings)
    - [How to generate documentation and HTML](#generate-documentation-and-html)
    - [How to generate UML](#generate-uml)
    - [Other useful commands](#other-useful-commands)
  - [Usage](#usage)
  - [Running the game](#running-game)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)

## 🧐 About <a name = "about"></a>

The dice game Pig has been implemented in Python. Players have the option of playing versus a computer or a live opponent. If they decide to compete against the machine, they can also pick the degree of difficulty.

## 👨‍💻 Description <a name = "description"></a>

The Pig dice game can be played in the console using this application. Players take turns rolling a single die, and they can either hold to end their turn and keep their current score, or roll again to raise it. A player's turn ends instantly and their existing score is lost if they roll a 1. The game is won by the first player to accumulate 100 points.

There is a primary menu in the software where users can begin a new game, view high scores, see the rules, or toggle cheat, pick level or quit the game.

## 🏁 Getting Started <a name = "getting_started"></a>
To get started with this program, simply download the code and run it in the terminal.

### Features of our game <a name = "features"></a>
A class for dice games that lets players compete against computers or other players.

A high score class that records the highest marks received in each game mode.
A form of player that enables name changes for users.

A dice-rolling simulation lesson using dice hands.
A type of intelligence that regulates how challenging the computer opponent is.
A primary class that manages the game's pace and shows the main menu.
The user's ability to view the rules.
The option to exit the game for the user.
When asked to roll or hold, the user has the option to "cheat" by typing "cheat".
Checking for errors to make sure the user choose a reliable option in the main menu.

### Create and run the virtual environment <a name = "create_run_venv"></a>
  Creating virtual environment:
python -m venv [venv_name]

Running virtual environment:
On Windows:
[venv_name]/Scripts/activate.bat
On Mac and Linux:
source [venv_name]/bin/activate


### Installing <a name = "installing"></a>

This program requires Python 3 to be installed on your computer.

Install requirements:make install-requirements
Install toml:make install-toml
Build toml:make build-toml

### Installing make and chocolatey using Windows <a name = "install_make_and_chocolatey_windows"></a>
   To install Make and Chocolatey on Windows, follow these steps:
   1.Install Chocolatey package manager by opening PowerShell as an administrator and running the following command:Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

  
  2. After Chocolatey has been installed, you can use it to install Make by running the following command in PowerShell(Do not forget to run it as administrator):
    choco install make
  
  3. Once Make has been installed, you can verify the installation by running the following command:
    make --version


## Testings <a name = "testings"></a>
To run the tests, enter the following commands in the terminal:
  $ make test
  $ make pylint
  $ make coverage
  $ make coverage report -m

## Generate documentation and HTML <a name = "doc_and_html"></a>
  $ make pydoc

### Generate UML <a name = "generate_uml"></a>
  $ make pyreverse

### Other useful commands <a name = "other_commands"></a>
  check-venv
  make clean

### Running game
  1. To run the game run the following command on the gitbash terminal:
    make run

### Usage <a name = "usage"></a>

To play the game, simply download the code and run it in the terminal. The main menu will be displayed, and players can select an option using the numbered choices provided. Players can choose to start a new game, display high scores, display the rules, or quit the game.

If the player selects to start a new game, they will be prompted to choose whether they want to play against the computer or another human player. If they choose to play against the computer, they will also be prompted to choose the difficulty level.

Once the game starts, players take turns rolling a single die, and can choose to either roll again to increase their score, or hold to end their turn and keep their current score. If a player rolls a 1, their turn ends immediately and their current score is forfeited. The first player to reach 30 points wins the game.

The program includes the following features:

A Dice game class that allows the user to play the game against a computer or another player.
A high score class that keeps track of the top scores for each game mode.
A player class that allows the user to change their name.
A dice hand class that simulates the rolling of dice.
An intelligence class that controls the difficulty of the computer opponent.
A main class that controls the flow of the game and displays the main menu.
The ability for the user to display the rules.
The ability for the user to quit the game.
The ability for the user to cheat by entering "cheat" when prompted to roll or hold.
Error checking to ensure the user enters a valid choice in the main menu.


## ⛏️ Built Using <a name = "built_using"></a>
This program was built using Python 3.

## ✍️ Authors <a name = "authors"></a>

This program was created by:

- Us
- 