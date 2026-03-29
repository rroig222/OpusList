import customtkinter as ctk

from GUI.Components.Simple.SFrameGrid import SFrameGrid
from GUI.Components.Simple.STextField import STextField
from GUI.Components.Simple.SButton import SButton
from GUI.Components.Complex.CWork import CWork

from Connector_API.Connectors.UserConector import UserConector
from Connector_API.dataclasses import User
from tkinter import messagebox


class DashboardWindow(ctk.CTk):
    def __init__(self, user_conector: UserConector, user: User):
        super().__init__()
        self.user_conector = user_conector
        self.user = user
        self.crear()

    def crear(self):
        self.title("Login")
        self.geometry("800x600")
        self.configure(fg_color="#ffffff")

        # Frame principal
        frame = SFrameGrid(self, column=5, row=3)
        frame.pack(fill="both", expand=True)

        # --- ARRIBA ---
        self.search_btn = SButton(frame=frame, text="Search work", color="blue", command=self.search)
        self.search_btn.grid(row=0, column=0, columnspan=5, pady=10)

        # --- CENTRO (SCROLLABLE) ---
        self.works_frame = ctk.CTkScrollableFrame(frame, orientation="vertical", bg_color="#ffffff", fg_color="#e7e7e7")
        self.works_frame.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=20, pady=10)

        # IMPORTANTE: hacer que crezca correctamente
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure((0,1,2,3,4), weight=1)

        # Ejemplo: añadir elementos dentro del scroll
        self.build_works()

        # --- ABAJO ---
        self.bottom_btn = SButton(frame=frame, text="Log out", color="red")
        self.bottom_btn.grid(row=2, column=0, columnspan=5, pady=10)

        self.mainloop()


    def build_works(self):
        works = self.user_conector.get_rated_works(self.user.id)

        print(works)

        for work in works[1]:
            work_frame = CWork(master=self.works_frame, work=work, user=self.user)
            work_frame.pack(fill="x", padx=10, pady=10)

    def search(self):
        from GUI.Windows.User.Search import SearchWindow
        self.destroy()
        SearchWindow(user_conector=self.user_conector, user=self.user)
        