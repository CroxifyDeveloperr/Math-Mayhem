####################
## LIBRARIES ##
####################
import customtkinter as ctk


####################
## CLASSES ##
####################
class Program(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Math Mayhem!")
        self.geometry("700x600")
        self.resizable(False, False)

        self.mainMenu = MainMenu(self)
        self.mainMenu.pack()


class MainMenu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(
            master=parent,
            width=700,
            height=600,
            fg_color="#5ad17a",
            border_color="#32a852", 
            border_width=4
        )
        self.Build()
    
    def Build(self):
        title_frame = ctk.CTkFrame(
            master=self,
            width=350,
            height=125,
            fg_color="#5ad17a",
            border_color="#32a852", 
            border_width=4
        )
        title_frame.place(relx=0.5, rely=0.2, anchor="center")

        self.title = ctk.CTkLabel(
            master=title_frame,
            text="Math Mayhem!",
            text_color="white",
            font=("Calibri", 42, "bold")
        )
        self.title.place(relx=0.5, rely=0.5, anchor="center")

        control_frame = ctk.CTkFrame(
            master=self,
            width=350,
            height=300,
            fg_color="#5ad17a",
            border_color="#32a852", 
            border_width=4
        )
        control_frame.place(relx=0.5, rely=0.65, anchor="center")

        play_button = ctk.CTkButton(
            master=control_frame,
            text="Play",
            text_color="white",
            width=150,
            height=40,
            font=("Calibri", 36, "bold"),
            fg_color="#5ad17a",
            border_color="#32a852",
            border_width=4,
            hover_color="#38c75e"
        )
        play_button.place(relx=0.5, rely=0.20, anchor="center")

        leaderboard_button = ctk.CTkButton(
            master=control_frame,
            text="Leaderboard",
            text_color="white",
            width=150,
            height=40,
            font=("Calibri", 36, "bold"),
            fg_color="#5ad17a",
            border_color="#32a852",
            border_width=4,
            hover_color="#38c75e"
        )
        leaderboard_button.place(relx=0.5, rely=0.50, anchor="center")

        quit_button = ctk.CTkButton(
            master=control_frame,
            text="Quit",
            text_color="white",
            width=150,
            height=40,
            font=("Calibri", 36, "bold"),
            fg_color="#5ad17a",
            border_color="#32a852",
            border_width=4,
            hover_color="#38c75e"
        )
        quit_button.place(relx=0.5, rely=0.80, anchor="center")


####################
## MAIN ##
####################
if __name__ == "__main__":
    program = Program()
    program.mainloop()