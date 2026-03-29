import customtkinter as ctk

from GUI.Components.Simple.SFrameGrid import SFrameGrid
from GUI.Components.Simple.STextField import STextField
from GUI.Components.Simple.SButton import SButton
from GUI.Components.Complex.CWork import CWork
from GUI.Components.Complex.CWorkUnrated import CWorkUnrated

from Connector_API.Connectors.UserConector import UserConector
from Connector_API.Connectors.WorkConnector import WorkConector
from Connector_API.dataclasses import User, Work, Composer
from tkinter import messagebox

class SearchDBWindow(ctk.CTk):
    def __init__(self, user_conector: UserConector, user: User, query: str):
        super().__init__()
        self.user_conector = user_conector
        self.work_connector = WorkConector()
        self.query: str = query
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
        self.search_btn = SButton(frame=frame, text="Search in openopus", color="blue", command=self.search_btn)
        self.search_btn.grid(row=0, column=0, columnspan=5, pady=10)

        # --- CENTRO (SCROLLABLE) ---
        self.works_frame = ctk.CTkScrollableFrame(frame, orientation="vertical", bg_color="#ffffff", fg_color="#e7e7e7")
        self.works_frame.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=20, pady=10)

        # IMPORTANTE: hacer que crezca correctamente
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure((0,1,2,3,4), weight=1)

        # --- ABAJO ---
        self.bottom_btn = SButton(frame=frame, text="Back to Dashboard", color="red", command=self.back_to_Dashboard)
        self.bottom_btn.grid(row=2, column=0, columnspan=5, pady=10)

        # Ejemplo: añadir elementos dentro del scroll
        self.build_works()

        self.mainloop()

    def build_works(self):
        try:
            works: list[tuple[Work, int | None]] = self.work_connector.search_work_db(
                user=self.user,
                query=self.query
            )

            if not works:
                messagebox.showerror("No works found, try to search in OpenOpus")

            for work, rated in works:
                if rated is not None:
                    work_frame = CWork(master=self.works_frame, work=work, user=self.user)
                else:
                    work_frame = CWorkUnrated(master=self.works_frame, work=work, user=self.user)

                work_frame.pack(fill="x", padx=10, pady=10)


        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except ConnectionError as e:
            messagebox.showerror("Connection error", str(e))
        except Exception as e:
            messagebox.showerror("Unexpected error", str(e))

    def back_to_Dashboard(self):
        from GUI.Windows.User.Dashboard import DashboardWindow
        self.destroy()
        DashboardWindow(user_conector=self.user_conector, user=self.user)

    def search_btn(self):
        from GUI.Windows.User.Search import SearchWindow
        self.destroy()
        SearchWindow(user_conector=self.user_conector, user=self.user, openopus=True)


