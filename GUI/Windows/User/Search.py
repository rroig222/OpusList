import customtkinter as ctk

from GUI.Components.Simple.SFrameGrid import SFrameGrid
from GUI.Components.Simple.STextField import STextField
from GUI.Components.Simple.SButton import SButton
from GUI.Components.Complex.CWork import CWork

from GUI.Windows.User.Searched_DB import SearchDBWindow
from GUI.Windows.User.Searched_OpenOpus import SearchOpenOpusWindow

from Connector_API.Connectors.UserConector import UserConector
from Connector_API.dataclasses import User
from tkinter import messagebox


class SearchWindow(ctk.CTk):
    def __init__(self, user_conector: UserConector, user: User, openopus: bool = False):
        super().__init__()
        self.user_conector = user_conector
        self.user = user
        self.openopus = openopus
        self.crear()

    def crear(self):
        # Configuración básica
        self.title("Search")
        self.geometry("300x220")
        self.configure(fg_color="#ffffff")
        self.resizable(False, False)

        # Frame principal
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Campo Composer
        self.composer_label = ctk.CTkLabel(self.frame, text="Composer")
        self.composer_entry = ctk.CTkEntry(self.frame)
        if self.openopus:
            self.composer_label.pack(anchor="w", padx=5)
            self.composer_entry.pack(fill="x", padx=5, pady=(0, 10))
            



        # Campo Work Title
        self.title_label = ctk.CTkLabel(self.frame, text="Work title")
        self.title_label.pack(anchor="w", padx=5)

        self.title_entry = ctk.CTkEntry(self.frame)
        self.title_entry.pack(fill="x", padx=5, pady=(0, 15))

        # Frame botones
        self.button_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.button_frame.pack(side="bottom", pady=10)

        # Botón Cancel
        self.cancel_button = SButton(
            frame=self.button_frame,
            text="Cancel",
            color="white",
            command=self.cancel
        )
        self.cancel_button.pack(side="left", padx=5)

        # Botón Save
        self.search_button = SButton(
            frame=self.button_frame,
            text="Search",
            color="blue",
            command=self.search
        )
        self.search_button.pack(side="left", padx=5)

    def search(self):
        composer = self.composer_entry.get()
        title = self.title_entry.get()

        if not self.openopus:
            self.destroy()
            SearchDBWindow(user_conector=self.user_conector, user=self.user, query = title)

        else:
            self.destroy()
            SearchOpenOpusWindow(user_conector=self.user_conector, user=self.user, composer_query=composer, query=title)

    def cancel(self):
        self.destroy()
        