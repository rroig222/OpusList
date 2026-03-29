import customtkinter as ctk
from GUI.Components.Simple.SFrameGrid import SFrameGrid
from GUI.Components.Simple.STextField import STextField
from GUI.Components.Simple.SButton import SButton
from Connector_API.Connectors.UserConector import UserConector
from tkinter import messagebox

class RegisterWindow(ctk.CTk):

    def __init__(self, user_conector: UserConector):
        super().__init__()
        self.user_conector = user_conector
        self.crear()
        
    def crear(self):
        
        self.title("Crear nuevo usuario")
        self.geometry("600x500")
        self.configure(fg_color="#ffffff")
        
        #Crear el Frame principal
        frame = SFrameGrid(self, 1, 5)
        frame.pack(fill="both", expand=True)
        
        
        #Crear los campos de texto
        frameText = SFrameGrid(frame, 1, 5)
        frameText.grid(column = 0, row = 1, rowspan=3)

        self.InNombreUsuario = STextField(frameText, 300, 31, "Nombre de Usuario")
        self.InNombreUsuario.grid(column=0, row=0, pady=10)        

        self.InEmail = STextField(frameText, 300, 31, "Email")
        self.InEmail.grid(column=0, row=1, pady=10)
        
        self.InContrasena = STextField(frameText, 300, 31, "Contraseña", True)
        self.InContrasena.grid(column=0, row=2, pady=10)
        
        self.InConfirmContra = STextField(frameText, 300, 31, "Confirmar Contraseña", True)
        self.InConfirmContra.grid(column=0, row=3, pady=10)

        self.InfoLabel = ctk.CTkLabel(frameText,text_color="#000000",text="")
        self.InfoLabel.grid(column=0, row=4, pady=10)

        #Crear los botones
        framebtn = ctk.CTkFrame(frame, fg_color="#ffffff")
        framebtn.grid(column=0, row=5, sticky="nsew", pady=10, padx = 20)

        self.btn_Crear = SButton(framebtn, "Crear Usuario", "blue", command=self.CrearUsuario)
        self.btn_Crear.pack(side="right", padx=20, pady=10)
        
        btn_Cancelar = SButton(framebtn, "Cancelar", "white", command=self.Cancel)
        btn_Cancelar.pack(side="right", pady=10)
        
        self.mainloop()
        
        
    def Cancel(self):

        from GUI.Windows.Auth.Login import LoginWindow

        self.destroy()
        LoginWindow(user_conector=self.user_conector)
        
    def CrearUsuario(self):

        from GUI.Windows.Auth.Login import LoginWindow

        username = self.InNombreUsuario.get()
        password = self.InContrasena.get()
        email = self.InEmail.get()

        try:
            self.user_conector.create_user(username=username, password=password, email=email)
            self.destroy()
            messagebox.showinfo("Información", "Usuario creado correctamente")
            LoginWindow(user_conector=self.user_conector)

        
        except ValueError as e:
            self.InfoLabel.configure(text="El nombre de usuario o email esta ocupado")
        