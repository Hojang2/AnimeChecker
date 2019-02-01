#!/usr/bin/env python3
from AddAnimeLayout import AddAnimeLayout
from SelectALayout import SelectALayout
from DatabaseManager import DatabaseManager
import tkinter


class Checker(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.dManager = DatabaseManager()
        self.parent.title("Anime page")
        self.parent.minsize(900, 600)
        self.parent.resizable(True, True)
        self.addAnimeL = None
        self.selectL = None
        self.create_widgets()

    def create_widgets(self):
        update_button = tkinter.Button(self.parent, text="Reload",
                                       anchor="center",
                                       command=lambda: self.update_all())

        update_button.grid(row=0, column=0, columnspan=6)

        self.addAnimeL = AddAnimeLayout(self.parent, row=1)
        self.selectL = SelectALayout(self.parent, row=13)

    def update_all(self):
        self.addAnimeL.create_layout()
        self.selectL.create_layout()


root = tkinter.Tk()
app = Checker(root)
app.mainloop()
