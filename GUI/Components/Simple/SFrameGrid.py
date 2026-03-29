import customtkinter as ctk

class SFrameGrid(ctk.CTkFrame):
    
    def __init__(self, frame, column: int, row: int):
        
        #Sirve solo para crear frames con grid, no con pack
        super().__init__(frame)
        
        for i in range(column):
            print("Column")
            self.grid_columnconfigure(i, weight=1)
        
        for i in range(row):
            print("row")
            self.rowconfigure(i, weight=1)
            
        self.configure(fg_color="#ffffff")