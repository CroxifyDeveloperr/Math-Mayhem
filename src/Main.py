"""
READ ME:
This file is responsible for all the UI seen throughout the program and doesn't contain much functionality.
"""

#########################
## LIBRARIES ##
#########################
import customtkinter as ctk
import random, time
from PIL import Image, ImageTk


#########################
## FILES ##
#########################
import StyleEnum, Backend
from PageSwapper import SwapPage


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

CHARACTER_ONE_IMAGE_PATH = "Images\BiggieCheese.png"
CHARACTER_TWO_IMAGE_PATH = "Images\Mike.png"
CHARACTER_THREE_IMAGE_PATH = "Images\Russlle.png"

BATTLEGROUND_BEACH_BACKGROUND_IMAGE_PATH = "Images\BeachBackground.png"
BATTLEGROUND_DESERT_BACKGROUND_IMAGE_PATH = "Images\DesertBackground.png"
BATTLEGROUND_FORREST_BACKGROUND_IMAGE_PATH = "Images\ForrestBackground.png"

#########################
## VARIABLES ##
#########################
character_one_image = Image.open(CHARACTER_ONE_IMAGE_PATH)
character_two_image = Image.open(CHARACTER_TWO_IMAGE_PATH)
character_three_image = Image.open(CHARACTER_THREE_IMAGE_PATH)

characters = {
    "CharacterOne" : character_one_image,
    "CharacterTwo" : character_two_image,
    "CharacterThree" : character_three_image
}

beach_background_image = Image.open(BATTLEGROUND_BEACH_BACKGROUND_IMAGE_PATH)
desert_background_image = Image.open(BATTLEGROUND_DESERT_BACKGROUND_IMAGE_PATH)
forrest_background_image = Image.open(BATTLEGROUND_FORREST_BACKGROUND_IMAGE_PATH)

resized_character_one_image = character_one_image.resize((200, 350))
resized_character_two_image = character_two_image.resize((200, 350))
resized_character_three_image = character_three_image.resize((200, 350))

resized_beach_background_image = beach_background_image.resize((800, 500))
resized_desert_background_image = desert_background_image.resize((800, 500))
resized_forrest_background_image = forrest_background_image.resize((800, 500))


#########################
## PRIVATE FUNCTIONS ##
#########################
def BackgroundPicker() -> ctk.CTkImage:
    """
    ABOUT THIS FUNCTION:
    This function picks a random image from an array and assigns it as the background to the battlefield.
    """
    backgrounds = [resized_beach_background_image, resized_desert_background_image, resized_forrest_background_image]
    background = backgrounds[random.randint(0, len(backgrounds)-1)]
    return background


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

        self.main_menu_page = MainMenu(self)
        self.character_selection_page = CharacterSelection(self)
        self.battleground_page = Battleground(self)
        self.result_page = ResultScreen(self)
        self.leaderboard_page = Leaderboard(self)

        self.main_menu_page.pack()
        # self.result_page.pack()



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
        
        self.title_frame = ctk.CTkFrame(
            master = self,
            width = 400,
            height = 100,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH,
            corner_radius = CORNER_RADIUS,
        )
        self.title_frame.place(relx=0.5, rely=0.15, anchor="center")

        title = ctk.CTkLabel(
            master = self.title_frame,
            text = "Math Mayhem",
            text_color = TEXT_COLOR,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            font = ("Arial", 32, "bold")
        ).place(relx=0.5, rely=0.5, anchor="center")

        self.control_frame = ctk.CTkFrame(
            master = self,
            width = 400,
            height = 500,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH,
            corner_radius = CORNER_RADIUS,
        )
        self.control_frame.place(relx=0.5, rely=0.6125, anchor="center")

        play_button = ctk.CTkButton(
            master = self.control_frame,
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
            command = lambda: SwapPage(pageToAdd = program.character_selection_page, pageToRemove = program.main_menu_page)
        ).place(relx=0.5, rely=0.25, anchor="center")

        Leaderboard_button = ctk.CTkButton(
            master = self.control_frame,
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
        ).place(relx=0.5, rely=0.5, anchor="center")

        quit_button = ctk.CTkButton(
            master = self.control_frame,
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
        super().__init__(
            master = parent,
            width = 800,
            height = 700,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH
        )
        self.Build()
     

    def SetupCombat(self, selected_character: str):
        """
        ABOUT THIS FUNCTION:
        This function has two purposes:
            1. To send the Player's selected character over to CombatHandler.
            2. To invoke the SwapPage function so that the Player can see the battlefield and begin fighting.
            3. To send relevant information to the backend / combat handler.
        """
        Backend.PlayerCharacterSelected(character_name = selected_character)
        Backend.ChooseComputerCharacter(player_character = selected_character)
        Backend.SetupCombat(program)


    def Build(self):
        """
        ABOUT THIS FUNCTION:
        This function takes the created frame and adds widgets to them. These widgets are then customized.
        """

        self.title_frame = ctk.CTkFrame(
            master = self,
            width = 400,
            height = 100,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH,
            corner_radius = CORNER_RADIUS,
        )
        self.title_frame.place(relx=0.5, rely=0.15, anchor="center")

        title = ctk.CTkLabel(
            master = self.title_frame,
            text = "Character Selection",
            text_color = TEXT_COLOR,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            font = ("Arial", 32, "bold")
        ).place(relx=0.5, rely=0.5, anchor="center")

        back_button = ctk.CTkButton(
            master = self,
            width = 125,
            height = 75,
            text = "Back",
            font = ("Arial", 16, "bold"),
            command = lambda: SwapPage(pageToAdd = program.main_menu_page, pageToRemove = program.character_selection_page),
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH,
            corner_radius = CORNER_RADIUS,
            hover_color = BUTTON_HOVER_COLOR
        ).place(relx=0.875, rely=0.15, anchor="center")

        self.character_one = ctk.CTkButton(
            master = self,
            width = 200,
            height = 400,
            text = "",
            command = lambda: self.SetupCombat(selected_character = "CharacterOne"),
            image = ImageTk.PhotoImage(resized_character_one_image),
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH,
            corner_radius = CORNER_RADIUS,
            hover_color = BUTTON_HOVER_COLOR
        ).place(relx=0.2, rely=0.6, anchor="center")

        self.character_two = ctk.CTkButton(
            master = self,
            width = 200,
            height = 400,
            text = "",
            command = lambda: self.SetupCombat(selected_character = "CharacterTwo"),
            image = ImageTk.PhotoImage(resized_character_two_image),
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH,
            corner_radius = CORNER_RADIUS,
            hover_color = BUTTON_HOVER_COLOR
        ).place(relx=0.5, rely=0.6, anchor="center")

        self.character_three_frame = ctk.CTkButton(
            master = self,
            width = 200,
            height = 400,
            text = "",
            command = lambda: self.SetupCombat(selected_character = "CharacterThree"),
            image = ImageTk.PhotoImage(resized_character_three_image),
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH,
            corner_radius = CORNER_RADIUS,
            hover_color = BUTTON_HOVER_COLOR
        ).place(relx=0.8, rely=0.6, anchor="center")



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
        super().__init__(
            master = parent,
            width = 800,
            height = 700,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH
        )
        self.Build()
        self.SetupProblem()


    def Build(self):
        """
        ABOUT THIS FUNCTION:
        This function takes the created frame and adds widgets to them. These widgets are then customized.
        """
        
        self.background_frame = ctk.CTkFrame(
            master = self,
            width = 800,
            height = 500,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH
        )
        self.background_frame.place(relx=0.5, rely=0.36, anchor="center")

        background_holder = ctk.CTkLabel(
            master = self.background_frame,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            text = "",
            image = ImageTk.PhotoImage(BackgroundPicker())
        ).place(relx=0.5, rely=0.5, anchor="center")

        self.control_frame = ctk.CTkFrame(
            master = self,
            width = 800,
            height = 200,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH,
        )
        self.control_frame.place(relx=0.5, rely=0.8575, anchor="center")

        self.question_frame = ctk.CTkFrame(
            master = self.control_frame,
            width = 800,
            height = 200,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH,
        )
        self.question_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.player_name = ctk.CTkLabel(
            master = self.question_frame,
            text = "PLAYER_NAME",
            font = ("Arial", 24, "bold"),
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            text_color = TEXT_COLOR
        )
        self.player_name.place(relx=0.15, rely=0.25, anchor="center")

        self.player_health = ctk.CTkLabel(
            master = self.question_frame,
            text = "PLAYER_HEALTH",
            font = ("Arial", 16, "bold"),
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            text_color = TEXT_COLOR
        )
        self.player_health.place(relx=0.15, rely=0.45, anchor="center")

        self.computer_name = ctk.CTkLabel(
            master = self.question_frame,
            text = "COMPUTER_NAME",
            font = ("Arial", 24, "bold"),
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            text_color = TEXT_COLOR
        )
        self.computer_name.place(relx=0.85, rely=0.25, anchor="center")

        self.computer_health = ctk.CTkLabel(
            master = self.question_frame,
            text = "COMPUTER_HEALTH",
            font = ("Arial", 16, "bold"),
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            text_color = TEXT_COLOR
        )
        self.computer_health.place(relx=0.85, rely=0.45, anchor="center")

        self.player_character_frame = ctk.CTkFrame(
            master = self.background_frame,
            width = 125,
            height = 125,
        )
        self.player_character_frame.place(relx=0.15, rely=0.7, anchor="center")

        self.player_character_image = ctk.CTkLabel(
            master = self.player_character_frame,
            width = 150,
            height = 150,
            text = "",
            image = None
        )
        self.player_character_image.place(relx=0.5, rely=0.5, anchor="center")

        self.computer_character_frame = ctk.CTkFrame(
            master = self.background_frame,
            width = 125,
            height = 125,
        )
        self.computer_character_frame.place(relx=0.85, rely=0.7, anchor="center")

        self.computer_character_image = ctk.CTkLabel(
            master = self.computer_character_frame,
            width = 150,
            height = 150,
            text = "",
            image = None
        )
        self.computer_character_image.place(relx=0.5, rely=0.5, anchor="center")

        self.question_label = ctk.CTkLabel(
            master = self.question_frame,
            text = "Test",
            font = ("Arial", 32, "bold"),
            text_color = TEXT_COLOR
        )
        self.question_label.place(relx=0.5, rely=0.2, anchor="center")

        self.answer_storage = ctk.StringVar(master = self)

        self.answer_entry = ctk.CTkEntry(
            master = self.question_frame,
            textvariable = self.answer_storage,
            width = 150,
            height = 40,
            font = ("Arial", 16, "bold"),
            border_width = BORDER_WIDTH,
            border_color = BORDER_COLOR
        )
        self.answer_entry.place(relx=0.5, rely=0.5, anchor="center")

        self.submit_button = ctk.CTkButton(
            master = self.question_frame,
            text = "Submit Answer",
            font = ("Arial", 16, "bold"),
            width = 25,
            height = 50,
            command = self.SubmitAnswer,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_color = BORDER_COLOR,
            border_width = BORDER_WIDTH,
            hover_color = BUTTON_HOVER_COLOR
        )
        self.submit_button.place(relx=0.5, rely=0.8, anchor="center")

        self.answer_status = ctk.CTkLabel(
            master = self.question_frame,
            text = "",
            font = ("Arial", 16),
            text_color = TEXT_COLOR
        )
        self.answer_status.place(relx=0.65, rely=0.5, anchor="center")


    def SetupProblem(self):
        problem, self.answer = Backend.GenerateProblem()
        self.question_label.configure(text = f"{problem} = ?")

    
    def SubmitAnswer(self):
        Backend.ValidateAnswer(self, self.answer_entry, self.answer)
        self.SetupProblem()
        


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

        super().__init__(
            master = parent,
            width = 800,
            height = 700,
            bg_color = BACKGROUND_COLOR,
            fg_color = FOREGROUND_COLOR,
            border_width = BORDER_WIDTH
        )
        self.Build()
     
    
    def CreateRewards(self, result_message, reward_message):
        self.result.configure(text = result_message)
        self.reward.configure(text = reward_message)


    def Build(self):
        """
        ABOUT THIS FUNCTION:
        This function takes the created frame and adds widgets to them. These widgets are then customized.
        """

        self.result = ctk.CTkLabel(
            master = self,
            text = "RESULT",
            font = ("Arial", 72, "bold"),
            text_color = TEXT_COLOR
        )
        self.result.place(relx=0.5, rely=0.3, anchor="center")

        self.reward = ctk.CTkLabel(
            master = self,
            text = "REWARD",
            font = ("Arial", 36),
            text_color = TEXT_COLOR
        )
        self.reward.place(relx=0.5, rely=0.5, anchor="center")

        continue_button = ctk.CTkButton(
            master = self,
            text = "Continue",
            font = ("Arial", 24),
            width = 150,
            height = 50,
            command = lambda: SwapPage(pageToAdd = program.main_menu_page, pageToRemove = program.result_page),
            text_color = TEXT_COLOR,
            fg_color = BACKGROUND_COLOR,
            bg_color = BACKGROUND_COLOR,
            border_color = BORDER_COLOR,
            border_width = BORDER_WIDTH,
            hover_color = BUTTON_HOVER_COLOR
        )
        continue_button.place(relx=0.5, rely=0.75, anchor="center")



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
