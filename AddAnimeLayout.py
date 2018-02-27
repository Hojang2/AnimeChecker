import tkinter
from tkinter.font import Font
from DatabaseManager import DatabaseManager

class AddAnimeLayout(tkinter.Frame):
    def __init__(self, tkinter,row=0, column=0):
        super().__init__(tkinter)
        self.row = row
        self.dManager = DatabaseManager()
        self.column = column
        self.parent = tkinter
        self.create_layout()

    def create_layout(self):
        label = tkinter.Label(self.parent, text="Přidat nové anime", font=Font(size=40))
        label.grid(row=self.row, column=self.column, columnspan=self.column + 3)

        confirm_newA_button = tkinter.Button(self.parent, text="Přidat anime", command=lambda: self.add_anime())
        confirm_newA_button.grid(row=self.row + 1, column=self.column, columnspan=self.column + 3)

        label = tkinter.Label(self.parent, text="Zadej název nového anime které chceš sledovat")
        label.grid(row=self.row + 2, column=self.column)

        self.new_anime = tkinter.Entry(self.parent)
        self.new_anime.grid(row=self.row + 2, column=self.column + 1)

        label = tkinter.Label(self.parent, text="Zadej počet epizod")
        label.grid(row=self.row + 3, column=self.column)

        label = tkinter.Label(self.parent, text="Zadej naposledy viděnou epizodu")
        label.grid(row=self.row + 4, column=self.column)

    def add_anime(self):
        if self.new_anime.get() != "":
            self.dManager.add_new_anime_to_db(self.new_anime.get())
        self.new_anime.delete(0, 'end')
        self.create_layout()
