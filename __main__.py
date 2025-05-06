import customtkinter as ctk 
from gui import GUI

def main():
    app = ctk.CTk()
    app.title()
    app.geometry('800x600')
    app.resizable(False,False)
    gui = GUI(master=app)
    app.mainloop()
    
main()