import customtkinter as ctk
from GUI.Components.Simple.SButton import SButton
from GUI.Components.Simple.SFrameGrid import SFrameGrid
from GUI.Components.Simple.STextField import STextField
from Connector_API.dataclasses import Work, User, Composer
from Connector_API.Connectors.UserConector import UserConector
from GUI.Windows.User.Rate import RateWindow

class CWorkUnrated(ctk.CTkFrame):
    def __init__(self, master, work: Work, user: User):
        self.master=master
        super().__init__(master, fg_color="#ffffff")

        self.user = user
        self.work = work

        # Data attributes
        self.title = work.title
        self.composer = work.composer.full_name
        self.epoch = work.composer.epoch
        self.genre = work.genre

        # Build UI
        self.create()

    def create(self):
        # Configure layout to stretch horizontally
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

        # LEFT SIDE FRAME (info)
        self.left_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.left_frame.grid_columnconfigure(0, weight=1)

        # Labels
        self.title_label = ctk.CTkLabel(
            self.left_frame, text=self.title, font=("Arial", 16, "bold"), text_color="black"
        )
        self.title_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.composer_label = ctk.CTkLabel(
            self.left_frame, text=f"Composer: {self.composer}", text_color="black"
        )
        self.composer_label.grid(row=1, column=0, sticky="w")

        self.epoch_label = ctk.CTkLabel(
            self.left_frame, text=f"Epoch: {self.epoch}", text_color="black"
        )
        self.epoch_label.grid(row=2, column=0, sticky="w")

        self.genre_label = ctk.CTkLabel(
            self.left_frame, text=f"Genre: {self.genre}", text_color="black"
        )
        self.genre_label.grid(row=3, column=0, sticky="w")

        # RIGHT SIDE FRAME (buttons)
        self.right_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.right_frame.grid_rowconfigure((0, 1), weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        # Buttons
        '''
        self.see_composer_button = SButton(
            self.right_frame,
            color="blue",
            text="See Composer",
            command=self._handle_see_composer,
            width=80
        )
        self.see_composer_button.grid(row=0, column=0, sticky="ew", pady=(0, 5))
        '''
        
        self.rate_work_button = SButton(
            self.right_frame,
            color="blue",
            text="Save and rate work",
            command=self._handle_rate_work,
            width=80
        )
        self.rate_work_button.grid(row=0, column=0, sticky="ew")

    def _handle_rate_work(self):
        RateWindow(user_conector=UserConector(), work_master=self.master, user=self.user, work=self.work)