import customtkinter as ctk
from GUI.Components.Simple.SFrameGrid import SFrameGrid
from GUI.Components.Simple.STextField import STextField
from GUI.Components.Simple.SButton import SButton
from Connector_API.Connectors.UserConector import UserConector
from tkinter import messagebox

from GUI.Windows.User.Dashboard import DashboardWindow

class LoginWindow(ctk.CTk):
    def __init__(self, user_conector: UserConector):
        super().__init__()
        self.user_conector = user_conector
        self.crear()

    def crear(self):
        self.title("Login")
        self.geometry("500x400")
        self.configure(fg_color="#ffffff")

        #Crear el Frame principal
        frame = SFrameGrid(self, 2, 3)
        frame.pack(fill="both", expand=True)
        
        #Crear los campos de texto
        frame_TextFields = ctk.CTkFrame(frame, fg_color="#ffffff")
        frame_TextFields.grid(row=1, columnspan=2)
        
        self.textField_Usuario = STextField(frame_TextFields, 300, 31, "Nombre de Usuario")
        self.textField_Usuario.pack(expand=True, pady=10)
        
        self.textField_Contrasena = STextField(frame_TextFields, 300, 31, "Contraseña", contra = True)
        self.textField_Contrasena.pack(expand=True, pady=10)
        
        
        #Crear Los botones
        
        frame_Botones = ctk.CTkFrame(frame, fg_color="#ffffff")
        frame_Botones.grid(row=2, column=1, sticky="e", pady=20)
        
        btn_Registrarse = SButton(frame_Botones, "Registrarse", "white", command=self.Click_Registrarse)
        btn_Registrarse.pack(side="left")

        self.btn_Login = SButton(frame_Botones, "Login", "blue", command=self.Click_Login)
        self.btn_Login.pack(side="left", padx=20)
        
        
        self.mainloop()
        
    def Click_Registrarse(self):
        from GUI.Windows.Auth.Register import RegisterWindow
        self.destroy()
        RegisterWindow(user_conector=self.user_conector)
        
    def Click_Login(self):
        
        username = self.textField_Usuario.get()
        password = self.textField_Contrasena.get()

        try:
            user = self.user_conector.login_check(username=username, password=password)
            self.destroy()
            DashboardWindow(user_conector=self.user_conector, user=user)


        except ValueError as e:
            messagebox.showerror(title="Fail Login", message=f"Error: {e}")