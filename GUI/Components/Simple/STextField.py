import customtkinter as ctk

class STextField(ctk.CTkEntry):
    
    
    def __init__(self, frame, width: int, height: int, phText: str, contra=False):
        
        #Asignar colores y mandar el super
        self.hasFocus = False
        
        self.P_Color="#3498db"
        self.S_Color="#ffffff"
        self.T_Color="#ebebec"
        
        super().__init__(frame,
                         width=width,
                         height=height,
                         border_width=1,
                         border_color=self.P_Color,
                         placeholder_text=phText,
                         corner_radius=6,
                         fg_color=self.S_Color,
                         text_color="#000000",
                         show="·" if contra else None
                        )
        
        #Cambia el color al pasar por encima y al seleccionar el campo de texto
        self.bind("<Enter>", self.On_TextField)
        self.bind("<Leave>", self.Out_TextField)
        self.bind("<FocusIn>", self.Focus_In_textField)
        self.bind("<FocusOut>", self.Focus_Out_textField)
    
    def On_TextField(self, event):
        if not self.hasFocus:
            self.configure(fg_color=self.T_Color)

    def Out_TextField(self, event):
        if not self.hasFocus:
            self.configure(fg_color=self.S_Color)
        
    def Focus_In_textField(self, event):
        self.hasFocus = True
        self.configure(fg_color=self.T_Color)
        
    def Focus_Out_textField(self, event):
        self.hasFocus = False
        self.configure(fg_color=self.S_Color)