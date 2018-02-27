import tkinter
from tkinter.font import Font
from tkinter import ttk
from DatabaseManager import DatabaseManager
class SelectALayout(tkinter.Frame):
    def __init__(self, tkinter, row=0, column=0):
        super().__init__(tkinter)
        self.row = row
        self.parent = tkinter
        self.databaseM = DatabaseManager()
        self.column = column
        self.create_layout()

    def create_layout(self):
        label = tkinter.Label(self.parent, text="Vybrané anime", font=Font(size=40))
        label.grid(row=self.row, column=self.column, columnspan=self.column + 3)

        label = tkinter.Label(self.parent, text="Anime které sleduješ:")
        label.grid(row=self.row + 1, column=self.column)

        delete_anime_button = tkinter.Button(self.parent, text="Smazat všechny anime", anchor="center",
                                             command=lambda: self.delete_anime())
        delete_anime_button.grid(row=self.row + 2, column=self.column, columnspan=self.column + 2)

        self.show_anime = ttk.Combobox(self.parent, value=self.databaseM.return_database())
        self.show_anime.grid(row=self.row + 1, column=self.column + 1)

    def delete_anime(self):
        self.databaseM.delete_datebase()
        self.create_layout()


