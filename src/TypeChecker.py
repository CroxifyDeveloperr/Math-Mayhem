"""
READ ME:
This file is a piece of utility that checks if the argument of a function matches it's expected type.
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
def CheckArgType(arg, expectedArgType: type) -> bool:
    """
    ABOUT THIS FUNCTION:
    This function is used to check if an arg matches its expected type.
    This function will help prevent repetition and clutter throughout the program.
    """
    
    try:
        # Checking if expectedArgType is that of type.
        if type(expectedArgType) is not type:
            raise TypeError(f"expectedArgType expected 'type' data type. Got '{type(expectedArgType)}'.")
        
        # Checking if arg matches its expected type.
        if type(arg) != expectedArgType:
            raise TypeError(f"arg type '{type(arg)}' does not match expectedArgType '{expectedArgType}'")
        
        return True

    except TypeError as type_error:
        print("CheckArgType Error:", type_error)
        return False

test = 3
CheckArgType(arg = test, expectedArgType = int)

#########################
## CLASSES ##
#########################


#########################
## MAIN ##
#########################