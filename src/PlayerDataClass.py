"""
READ ME:
This file is used to create a class for the Player's data. 
This acts a cahce, collecting data throughout the programs lifetime and being stored in a file when required.
"""

#########################
## LIBRARIES ##
#########################
import json

#########################
## FILES ##
#########################


#########################
## VARIABLES ##
#########################


#########################
## CONSTANTS ##
#########################


#########################
## PRIVATE FUNCTIONS ##
#########################


#########################
## CLASSES ##
#########################
class Stack:
    """
    ABOUT THIS CLASS:
    This class is creates our custom stack data structure. This will allow for data to be stored easily.
    Data within the stack will be stored in an organized matter, players with highest wins at the bottom and the lowest wins at the top. 
    """

    def __init__(self):
        """
        ABOUT THIS FUNCTION:
        This function is a constructor, and fires upon the creation of the stack class.
        This function initializes a variable that is used to house the data.
        This variable is a private variable, meaning that it canno't be accessed outside of certain methods.
        """

        self._data = []


    def UnpackDict(self, element: dict) -> tuple[str, int]:
        string, number = "", 0
        for key, value in element.items():
            string, number = key, value

        return string, number

    
    def PercisionPeek(self, index: int):
        """
        ABOUT THIS FUNCTION:
        Returns the element of a specific index without mainipulating it.
        """

        return self._data[index]


    def Push(self, element: dict[str : int]):
        """
        ABOUT THIS FUNCTION:
        This function adds the provided element to the stack after it has been organized.
        """

        # Getting the stack from the json file.
        with open("src\Database.json", "r") as f:
            data = json.load(f)
            self._data = data
        
        print(self._data)

        # Unpacking the dict.
        player_name, player_wins = self.UnpackDict(element)
        
        # Adding element to stack if stack is empty.
        if len(self._data) == 0:
            print("LENGTH OF ARRAY IS 0")
            self._data.append({player_name : player_wins})

            with open("src\Database.json", "w") as f:
                json.dump(self._data, f)
                return

        # Updating Player's win count if name already exists.
        for index in range(0, len(self._data)):
            stored_player_data = self.PercisionPeek(index)
            stored_player_name, stored_player_wins = self.UnpackDict(stored_player_data)

            # FIX THE WIN UPDATING

            if player_name == stored_player_name:
                print("Player already exits within stack.")
                stored_player_wins += player_wins
                self._data[index] = {player_name : stored_player_wins}
                
                with open("src\Database.json", "w") as f:
                    json.dump(self._data, f)
                    return
                
                
        # Adding Player to stack since Player dosn't exist
        print("Player doen't exist within stack.")

        self._data.append({player_name : player_wins})
        
        with open("src\Database.json", "w") as f:
            json.dump(self._data, f)


    def Pop(self) -> dict:
        """
        ABOUT THIS FUNCTION:
        This function removes the last element from the stack.
        """

        return self._data.pop()

stack = Stack()


class PlayerData():
    """
    ABOUT THIS CLASS:
    This class is used to effectivly manage and store data collected from the Player.
    The Player's name and the amount of wins they have are collected throughout the lifetime of the program.
    Upon winning a game, the Player's data is then sorted from highest to lowest and stored within the database.
    """

    def __init__(self):
        """
        ABOUT THIS FUNCTION:
        This function fires upon the creation of the object.
        This function initializes some variables which can be access and manipulated when needed.
        """

        self.name = ""
        self.wins = 0
    
    
    def SaveData(self):
        """
        ABOUT THIS FUNCTION:a
        This function takes the data collected from the Player throughout the lifetime of the program and sorts it with the pre-existing data already in the database.
        This function will then manipulate a stack data structure that will effectivly organize the code before then being converted into a JSON format and stored elsewhere.
        """
        
        stack.Push({self.name : self.wins})


        print(stack._data)


#########################
## MAIN ##
#########################