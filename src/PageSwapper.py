"""
READ ME:
This file is a peiece of utility and is responsible for swaping frames throughout the program. 
This makes it seem like the Player is flicking through pages.
"""

#########################
## LIBRARIES ##
#########################
import customtkinter as ctk


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

def SwapPage(pageToAdd: ctk.CTkFrame, pageToRemove: ctk.CTkFrame):
    """
    ABOUT THIS FUNCTION:
    This function is used to swap frames in a program allowing the Player to move from page to page without issue.
    """
        
    # Swapping the pages.
    pageToRemove.pack_forget()
    pageToAdd.pack()


#########################
## CLASSES ##
#########################



#########################
## MAIN ##
#########################