import customtkinter as ctk

class SButton (ctk.CTkButton):
    
    # Height = 30 and Width = 0 porque así se ajustan al tamaño del texto
    def __init__(self, frame, text: str, color: str, command = None, width=0, height=30,):


        # P_color --> Color Principal
        # S_Color --> Color Secundario
        # P_FColor --> Color Principal de la fuente y bordes
        
        self.color = color
        
        if self.color == "blue":
            
            self.P_Color="#3498db"
            self.S_Color="#2980b9"
            self.P_FColor="#ffffff"
            
        elif self.color == "white":
            
            self.P_Color="#ffffff"
            self.S_Color="#ebebec"
            self.P_FColor="#3498db"
            
        elif self.color == "red":
            
            self.P_Color="#ffffff"
            self.S_Color="#ff5a37"
            self.P_FColor="#ff2d00"
            
        #Crea el boton
        super().__init__(frame,
                        text=text,
                        width=width,
                        height=height,
                        corner_radius=32,
                        border_width=1,
                        fg_color=self.P_Color,
                        text_color=self.P_FColor,
                        border_color=self.P_FColor,
                        command=command if not None else None)
        
        #Cambia el color al pasar por encima del color        
        self.bind("<Enter>", self.On_Button)
        self.bind("<Leave>", self.Out_Button)


    def On_Button(self, event):
        self.configure(fg_color=self.S_Color)
        if self.color=="red":
            self.configure(border_color="#ffffff", text_color="#ffffff")

    def Out_Button(self, event):
        self.configure(fg_color=self.P_Color)
        self.configure(border_color=self.P_FColor, text_color=self.P_FColor)