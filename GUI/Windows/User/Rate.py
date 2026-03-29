import customtkinter as ctk

from GUI.Components.Simple.SFrameGrid import SFrameGrid
from GUI.Components.Simple.STextField import STextField
from GUI.Components.Simple.SButton import SButton

from Connector_API.Connectors.UserConector import UserConector
from Connector_API.dataclasses import User, Work
from tkinter import messagebox


class RateWindow(ctk.CTk):
    def __init__(self, work_master ,user_conector: UserConector, user: User, work: Work):
        super().__init__()
        self.user_conector = user_conector
        self.work_master = work_master
        self.user = user
        self.work = work
        self.crear()

    def crear(self):
        # Configuración básica de ventana
        self.title("Rate")
        self.geometry("250x150")
        self.resizable(False, False)

        # Frame principal
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Combobox (1–5)
        self.combo = ctk.CTkComboBox(
            self.frame,
            values=["1", "2", "3", "4", "5"],
            state="readonly"
        )
        self.combo.set("1")
        self.combo.pack(pady=(10, 15))

        # Frame para botones
        self.button_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.button_frame.pack(side="bottom", pady=10)

        # Botón Save
        self.save_button = SButton(
            frame=self.button_frame,
            text="Save",
            color="blue",
            command=self.save
        )
        self.save_button.pack(side="left", padx=5)

        # Botón Cancel
        self.cancel_button = SButton(
            frame=self.button_frame,
            text="Cancel",
            color="white",
            command=self.cancel
        )
        self.cancel_button.pack(side="left", padx=5)

    def save(self):
        valor = self.combo.get()
        self.user_conector.rate_work(user=self.user, work=self.work, rating=valor)
        self.work_master.update()
        self.destroy()

        

    def cancel(self):
        self.work_master.update()
        self.destroy()
