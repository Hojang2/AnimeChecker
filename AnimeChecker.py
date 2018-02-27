#!/usr/bin/env python3
from UpdateALayout import UpdateALayout
from AddAnimeLayout import AddAnimeLayout
from SelectALayout import SelectALayout
from DatabaseManager import DatabaseManager
import tkinter

class Checker(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.dManager = DatabaseManager()
        self.parent.title("Moje anime")
        self.parent.minsize(900, 600)
        self.parent.resizable(True, True)
        self.create_widgets()

    def create_widgets(self):
        update_button = tkinter.Button(self.parent, text="Načíst změny", anchor="center", command=lambda: self.update_all())
        update_button.grid(row=0, column=0, columnspan=6)

        self.addAnimeL = AddAnimeLayout(self.parent, row=1)
        self.updateL = UpdateALayout(self.parent,row=1, column=5)
        self.selectL = SelectALayout(self.parent,row=10)

    def update_all(self):
        self.addAnimeL.create_layout()
        self.updateL.create_layout()
        self.selectL.create_layout()
   #def validate_numbers(self, action, index,value, ):
   #kvalita
   #rok vydani

root = tkinter.Tk()
app = Checker(root)
app.mainloop()