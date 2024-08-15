"""
READ ME:
This file creates the character class.
The character class is used to store the name of who the character belongs too and keeps track of the character's health.
"""
#########################
## LIBRARIES ##
#########################


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
class Character:
    """
    ABOUT THIS CLASS:
    This class keeps track of the character's health and allows us to know who the character belongs too.
    """

    def __init__(self, name: str):
        """
        ABOUT THIS FUNCTION:
        This function is a constructor and fires upon the creation of an object from this class.
        This function initializes the variables "name" and "health" so they can me access, and manipulated throughout the backend.
        """
        
        self.name = name
        self.health = 100
    

    def Damage(self):
        """
        ABOUT THIS FUNCTION:
        This function damages the character by subtracting health from it.
        This function also checks if the character has no health left.
        The function will return a bool based on the outcome which will decide what happens next in the program.
        """

        self.health -= 10
        if self.health == 0:
            return True
        
        return False


#########################
## MAIN ##
#########################