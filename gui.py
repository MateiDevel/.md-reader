import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path

class GUI(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill='both', expand=True)
        
        def filed():
            file = filedialog.askopenfile()
            if file:
                filepath = file.name
                ext = Path(filepath).suffix
                if ext == '.md':
                    filelabel.configure(text=filepath)
                else:
                    filelabel.configure(text='This is not a .md file...')
                file.close()
        
    
        filebtn = ctk.CTkButton(self, text='File', command=filed)
        filebtn.place(x=10, y=50)    
        filelabel = ctk.CTkLabel(self, text='select file')
        filelabel.place(x=10, y=10)
        