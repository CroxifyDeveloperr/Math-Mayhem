"""
READ ME:
This file is responsible for all the UI seen throughout the program and doesn't contain much functionality.
"""

#########################
## LIBRARIES ##
#########################
import customtkinter as ctk


#########################
## FILES ##
#########################
from Enums import StyleEnum


#########################
## VARIABLES ##
#########################


#########################
## CONSTANTS ##
#########################
BACKGROUND_COLOR = StyleEnum.BACKGROUND_COLOR
FOREGROUND_COLOR = StyleEnum.FOREGROUND_COLOR
BORDER_COLOR = StyleEnum.BORDER_COLOR
TEXT_COLOR = StyleEnum.TEXT_COLOR
BUTTON_HOVER_COLOR = StyleEnum.BUTTON_HOVER_COLOR
BORDER_WIDTH = StyleEnum.BORDER_WIDTH
CORNER_RADIUS = StyleEnum.CORNER_RADIUS


#########################
## PRIVATE FUNCTIONS ##
#########################


#########################
## CLASSES ##
#########################
class Program(ctk.CTk):
    """
    ABOUT THIS CLASS:
    This class is responsible for the creation of the window.
    All pages (main menu, character selection, etc) will be stored in this class making page manipulation easier.
    The program class inherits from the Tk class, allowing us to manipulate its properties in the constructor.
    """
    
    def __init__(self):
        """
        ABOUT THIS FUNCTION:
        This function is a constructor, meaning it will fire automatically when an object of the program class is created.
        This function creates the window used for the program and begins the process of customizing it.
        Pages are also created, with the relvant page being displayed while the rest are stored away.
        """
        super().__init__()
        self.title("Math Mayhem")
        self.geometry("800x700")
        self.resizable(False, False)

        main_menu_page = MainMenu(self)
        character_selection_page = CharacterSelection(self)
        battleground_page = Battleground(self)
        result_screen = ResultScreen(self)
        leaderboard = Leaderboard(self)

        main_menu_page.pack()



class MainMenu(ctk.CTkFrame):
    """
    ABOUT THIS CLASS:
    This class is responsible for the creation and style of the main menu page.
    """

    def __init__(self, parent):
        """
        ABOUT THIS FUNCTION:
        This function is a constructor, meaning it will fire automatically when an object of the main menu class is created.
        This function creates the inital frame which can later be built.
        """

        super().__init__(
            master = parent,
            width = 800,
            height = 700,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH
        )
        self.Build()


    def Build(self):
        """
        ABOUT THIS FUNCTION:
        This function takes the created frame and adds widgets to them. These widgets are then customized.
        """
        title_frame = ctk.CTkFrame(
            master = self,
            width = 400,
            height = 100,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH,
            corner_radius = CORNER_RADIUS,
        ).place(relx=0.5, rely=0.15, anchor="center")

        title = ctk.CTkLabel(
            master = title_frame,
            text = "Math Mayhem",
            text_color = TEXT_COLOR,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            font = ("Arial", 32, "bold")
        ).place(relx=0.5, rely=0.15, anchor="center")

        control_frame = ctk.CTkFrame(
            master = self,
            width = 400,
            height = 500,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH,
            corner_radius = CORNER_RADIUS,
        ).place(relx=0.5, rely=0.6125, anchor="center")

        play_button = ctk.CTkButton(
            master = control_frame,
            text = "Play",
            font = ("Arial", 24, "bold"),
            text_color = TEXT_COLOR,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_color = BORDER_COLOR,
            border_width = BORDER_WIDTH,
            hover_color = BUTTON_HOVER_COLOR,
            width = 200,
            height = 75,
            command = None
        ).place(relx=0.5, rely=0.45, anchor="center")

        Leaderboard_button = ctk.CTkButton(
            master = control_frame,
            text = "Leaderboard",
            font = ("Arial", 24, "bold"),
            text_color = TEXT_COLOR,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_color = BORDER_COLOR,
            border_width = BORDER_WIDTH,
            hover_color = BUTTON_HOVER_COLOR,
            width = 200,
            height = 75,
            command = None
        ).place(relx=0.5, rely=0.6, anchor="center")

        quit_button = ctk.CTkButton(
            master = control_frame,
            text = "Quit",
            font = ("Arial", 24, "bold"),
            text_color = TEXT_COLOR,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_color = BORDER_COLOR,
            border_width = BORDER_WIDTH,
            hover_color = BUTTON_HOVER_COLOR,
            width = 200,
            height = 75,
            command = quit
        ).place(relx=0.5, rely=0.75, anchor="center")


class CharacterSelection(ctk.CTkFrame):
    """
    ABOUT THIS CLASS:
    This class is responsible for the creation and style of the character selection page.
    """
     
    def __init__(self, parent):
        """
        ABOUT THIS FUNCTION:
        This function is a constructor, meaning it will fire automatically when an object of the character selection class is created.
        This function creates the inital frame which can later be built.
        """
        pass
     
    
    def Build(self):
        """
        ABOUT THIS FUNCTION:
        This function takes the created frame and adds widgets to them. These widgets are then customized.
        """
        pass



class Battleground(ctk.CTkFrame):
    """
    ABOUT THIS CLASS:
    This class is responsible for the creation and style of the battleground page.
    """
     
    def __init__(self, parent):
        """
        ABOUT THIS FUNCTION:
        This function is a constructor, meaning it will fire automatically when an object of the battleground class is created.
        This function creates the inital frame which can later be built.
        """
        pass
     
    
    def Build(self):
        """
        ABOUT THIS FUNCTION:
        This function takes the created frame and adds widgets to them. These widgets are then customized.
        """
        pass
    


class ResultScreen(ctk.CTkFrame):
    """
    ABOUT THIS CLASS:
    This class is responsible for the creation and style of the result screen page.
    """
     
    def __init__(self, parent):
        """
        ABOUT THIS FUNCTION:
        This function is a constructor, meaning it will fire automatically when an object of the result screen class is created.
        This function creates the inital frame which can later be built.
        """
        pass
     
    
    def Build(self):
        """
        ABOUT THIS FUNCTION:
        This function takes the created frame and adds widgets to them. These widgets are then customized.
        """
        pass



class Leaderboard(ctk.CTkFrame):
    """
    ABOUT THIS CLASS:
    This class is responsible for the creation and style of the leaderboard page.
    """
     
    def __init__(self, parent):
        """
        ABOUT THIS FUNCTION:
        This function is a constructor, meaning it will fire automatically when an object of the leaderboard class is created.
        This function creates the inital frame which can later be built.
        """
        pass
     
    
    def Build(self):
        """
        ABOUT THIS FUNCTION:
        This function takes the created frame and adds widgets to them. These widgets are then customized.
        """
        pass



#########################
## MAIN ##
#########################
if __name__ == "__main__":
    program = Program()
    program.mainloop()
