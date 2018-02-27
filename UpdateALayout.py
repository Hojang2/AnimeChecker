import tkinter
from tkinter.font import Font
from tkinter import ttk
from DatabaseManager import DatabaseManager

class UpdateALayout(tkinter.Frame):
    def __init__(self, tkinter, row=0, column=0):
        super().__init__(tkinter)
        self.databaseM = DatabaseManager()
        self.parent = tkinter
        self.row = row
        self.column = column
        self.create_layout()

    def create_layout(self):
        label = tkinter.Label(self.parent, text="Aktualizovat vybrané anime", font=Font(size=40))
        label.grid(row=self.row, column=self.column, columnspan=self.column + 2)

        label = tkinter.Label(self.parent, text="Vyber anime, které chceš aktualizovat")
        label.grid(row=self.row+1, column=self.column)

        self.select_anime = ttk.Combobox(self.parent, value=self.databaseM.return_database())
        self.select_anime.grid(row=self.row + 1, column=self.column + 1)

    def update_data(self):
        self.create_layout()
