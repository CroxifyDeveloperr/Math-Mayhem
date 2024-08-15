"""
READ ME:
This file is in charge of handling the different phases of combat as well as calculating rewards and handling Player data.
"""

#########################
## LIBRARIES ##
#########################
import customtkinter as ctk
import operator, random, threading, time
from tkinter import messagebox
from PIL import Image, ImageTk


#########################
## FILES ##
#########################
import Main
from PageSwapper import SwapPage
from CharacterClass import Character
from PlayerDataClass import PlayerData


#########################
## VARIABLES ##
#########################
player_info = {}
computer_info = {}

player = Character(name = "Player")
computer = Character(name = "Computer")
player_data = PlayerData()


#########################
## CONSTANTS ##
#########################
OPERATORS_DICT = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    }


#########################
## PRIVATE FUNCTIONS ##
#########################
def PlayerCharacterSelected(character_name: str):
    """
    ABOUT THIS FUNCTION:
    This function is invoked when the Player selects a character.
    This function will store the Player's chosen character so that it be utilized later on when dealing with combat.
    """

    # Storing the computer's chosen character so that it can be passed around files & invoking the selection of the computer's character.
    player_info["character_image"] = Main.characters[character_name]


def ChooseComputerCharacter(player_character: str):
    """
    ABOUT THIS FUNCTION:
    This function is invoked after the Player's character has been chosen.
    This function chooses a character from the remainder and stores it so that it can be utilized when dealing with combat.
    """

    # Grabbing possible characters.
    character_names = list(Main.characters.keys())

    # Choosing a random character for the computer and ensuring that it's not the same as the one the Player has chosen.
    computer_character = None
    while computer_character is None:
        character_name = character_names[random.randint(0, len(character_names)-1)]
        if character_name == player_character:
            continue
        computer_character = character_name
    
    # Storing the computer's chosen character so that it can be passed around files.
    computer_info["character_image"] = Main.characters[computer_character]


def GetChosenPlayerCharacterImage():
    """
    ABOUT THIS FUNCTION:
    This function returns the image of the Player's chosen character to where it was called from.
    """

    return player_info["character_image"]


def GetChosenComputerCharacterImage():
    """
    ABOUT THIS FUNCTION:
    This function returns the image of the computer's chosen character to where it was called from.
    """
    
    return computer_info["character_image"]


def GenerateProblem() -> str:
    """
    ABOUT THIS FUNCTION:
    This function is responsible for creating the math problems itself.
    Two numbers and an arithmic operator are assigned at random to create a problem.
    These numbers are one through ten, and the operators are:
        - Addition
        - Subtraction
        - Multiplication
        - Division
    """

    num1, num2 = random.randint(1, 10), random.randint(1, 10)
    operators = list(OPERATORS_DICT.keys())
    operator = operators[random.randint(1, len(operators)-1)]
    problem = f"{num1} {operator} {num2}"
        
    arithmitic_func = OPERATORS_DICT[operator]
    answer = arithmitic_func(num1, num2)
    print(answer)

    return problem, answer


def ValidateAnswer(battleground, answer_storage: ctk.StringVar, answer: str):
    """
    ABOUT THIS FUNCTION:
    This function is used to filter the Player's input and validate their answer to see if it's correct.
    """
    try:
        player_answer = answer_storage.get()

        # Checking if the Player has left the textbox empty.
        if len(player_answer) == 0:
            raise Exception("Input cannot be left empty.")
        
        # Checking if the Player has inserted alphabetical characters or white space.
        for i in player_answer:
            if i.isalpha():
                raise Exception("Input can only contain numerical values.")
            elif i.isspace():
                raise Exception("Input cannot contain any spaces.")
        
        # Checking if the Player's answer is correct.
        if answer == int(player_answer):
            battleground.answer_status.configure(text = "✔️")

            # Subtracting health from the computer's character.
            computer.Damage()
            battleground.computer_health.configure(text = f"Health: {computer.health}")
        else:
            battleground.answer_status.configure(text = "❌")

    except Exception as exception:
        messagebox.showerror("Error", exception)


def ValidateInput(user_input: str):
    """
    ABOUT THIS FUNCTION:
    This function is responsible for the filtering of the user input, ensuring that the user isn't capable of crashing or exploiting the program.
    """
    try:
        # Checking if the input was left empty.
        if len(user_input) == 0:
            raise Exception("Input cannot be empty.")
        
        # Checking if input is less than the minimum character limit.
        elif len(user_input) < 3:
            raise Exception("Input must contain at least 3 characters.")
        
        # Checking if input hasn't exceeded the 10 character limit.
        elif len(user_input) > 10:
            raise Exception("Input cannot exceed the 10 character limit.")
        
        # Checking if the input only contains alphabetical characters.
        elif not user_input.isalpha():
            raise Exception("Input can only contain alphabetical characters.")
        
    except Exception as exception:
        messagebox.showerror("Error", exception)
    
    player_data.name = user_input


def CleanUpCombat():
    """
    ABOUT THIS FUNCTION:
    This function is responsible for cleaning up the backend after the battle is over.
    This functino will reset certain properties, making the application replayable.
    """

    # Resetting character health.
    player.health = 100
    computer.health = 100


def BeginCombat(program) -> None:
    """
    ABOUT THIS FUNCTION:
    This function is responsible for the combat of the computers character.
    Combat will continue until either the Player's character or computer's character has no health left.
    This function is executed in a different thread so that both the Player and the computer can work at their own pace.
    This function also invokes the reward function once the winner has been decided.
    If a reward were to be given, the Player's data will be automatically saved.
    """

    winner = ""
    while True:

        # Checking if the Player's or the computer's character is unable to continue.
        if computer.health == 0:
            winner = "Player"
            break
        elif player.health == 0:
            winner = "Computer"
            break

        # Damaging the Player a random amount each second.
        time.sleep(2)
        if random.randint(1, 10) <= 8:
            player.Damage()
            program.battleground_page.player_health.configure(text = f"Health: {player.health}")

    # Creating rewards & updated label messages.
    result_message = f"{winner} wins!"

    reward_message = ""
    if winner == "Player":
        reward_message = f"Reward: +1 win"
        player_data.wins += 1
        player_data.SaveData()
    elif winner == "Computer":
        reward_message = ""

    # Invoking a page swap & sending messages to the client.
    SwapPage(pageToAdd = program.result_page, pageToRemove = program.battleground_page)
    program.result_page.CreateRewards(result_message, reward_message)



def SetupCombat(program):
    """
    ABOUT THIS FUNCTION:
    This function is responsible for:
        1. Placing the characters in the battlefield and making then visible.
        2. Creating and math problems and checking the result.
        3. Damaging characters.
        4. Deciding a winner.
    """

    # Checking if the Player has provided all inputs needed.
    try:
        if len(player_data.name) == 0:
            raise Exception("All inputs must be satisfied before moving on.")
    except Exception as exception:
        messagebox.showerror("Error", exception)
        return

    # Swapping pages.
    SwapPage(pageToAdd = program.battleground_page, pageToRemove = program.character_selection_page)

    # Updating images im their respective frames.
    battleground_page = program.battleground_page
    player_character_image = GetChosenPlayerCharacterImage().resize((150,150))
    computer_character_image = GetChosenComputerCharacterImage().resize((150,150))
    battleground_page.player_character_image.configure(image = ImageTk.PhotoImage(player_character_image))
    battleground_page.computer_character_image.configure(image = ImageTk.PhotoImage(computer_character_image))

    # Updating name and health text labels.
    battleground_page.player_name.configure(text = f"{player.name}")
    battleground_page.computer_name.configure(text = f"{computer.name}")
    battleground_page.player_health.configure(text = f"Health: {player.health}")
    battleground_page.computer_health.configure(text = f"Health: {computer.health}")

    # Begining combat for the Computer.
    threading.Thread(target = lambda: BeginCombat(program)).start()


#########################
## CLASSES ##
#########################


#########################
## MAIN ##
#########################