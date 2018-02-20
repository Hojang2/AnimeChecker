#!/usr/bin/env python3
import tkinter
import DatabaseHandler
from tkinter.font import Font
from tkinter import ttk

class Checker(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Pro moje anime")
        self.parent.minsize(900, 600)
        self.parent.resizable(True, True)
        self.create_widgets()

    def create_widgets(self):
        self.label = tkinter.Label(text="Nejoblíbenější Anime", font=Font(size=50))
        self.label.grid(row=0, column=0, columnspan=4, rowspan=1)

        self.label = tkinter.Label(text="Zadej nové anime které chceš sledovat")
        self.label.grid(row=2, column=0)

        self.label = tkinter.Entry()
        self.label.grid(row=2, column=1)

        self.label = tkinter.Label(text="Anime které sleduješ:")
        self.label.grid(row=2, column=2)

        self.combobox = ttk.Combobox(self.parent)
        self.combobox.grid(row=2,column=3)

        self.label = tkinter.Label(text="Nejnovější díly", font=Font(size=40))
        self.label.grid(row=3, column=0, columnspan=4, rowspan=1)

        self.label = tkinter.Label(text="Vybrané anime", font=Font(size=40))
        self.label.grid(row=4, column=0, columnspan=4, rowspan=1)

root = tkinter.Tk()
app = Checker(root)
app.mainloop()
