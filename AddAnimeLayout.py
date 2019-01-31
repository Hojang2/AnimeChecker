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
        self.last_anime = ""
        self.create_layout()

    def create_layout(self):
        label = tkinter.Label(self.parent, text="Přidat nové anime", font=Font(size=40))
        label.grid(row=self.row, column=self.column, columnspan=self.column + 3)

        confirm_newA_button = tkinter.Button(self.parent, text="Přidat anime", command=lambda: self.add_anime(), width=15, height=2)
        confirm_newA_button.grid(row=self.row + 1, column=self.column, columnspan=self.column + 2)

        label = tkinter.Label(self.parent, text="Zadej název nového anime které chceš sledovat", font=Font(size=10))
        label.grid(row=self.row + 2, column=self.column, columnspan=self.column + 2)
        self.name_anime = tkinter.Entry(self.parent)
        self.name_anime.grid(row=self.row + 3, column=self.column, columnspan=self.column + 2)

        label = tkinter.Label(self.parent, text="Zadej počet epizod")
        label.grid(row=self.row + 5, column=self.column)
        self.episode_anime = tkinter.Entry(self.parent)
        self.episode_anime.grid(row=self.row + 5, column=self.column + 1)

        label = tkinter.Label(self.parent, text="Zadej naposledy viděnou epizodu")
        label.grid(row=self.row + 7, column=self.column)

        self.last_episode_anime = tkinter.Entry(self.parent)
        self.last_episode_anime.grid(row=self.row + 7, column=self.column + 1)

        label = tkinter.Label(self.parent, text="Vyber žánr")
        label.grid(row=self.row + 8, column=self.column)
        self.genre_anime = tkinter.Entry(self.parent)
        self.genre_anime.grid(row=self.row + 8, column=self.column + 1)

        label = tkinter.Label(self.parent, text="Vyber kvalitu anime")
        label.grid(row=self.row + 9, column=self.column)
        self.quality_anime = tkinter.Entry(self.parent)
        self.quality_anime.grid(row=self.row + 9, column=self.column + 1)

        label = tkinter.Label(self.parent, text="Poznámky")
        label.grid(row=self.row + 10, column=self.column)
        self.note_anime = tkinter.Entry(self.parent)
        self.note_anime.grid(row=self.row + 10, column=self.column + 1)

        label = tkinter.Label(self.parent, text="Poslední zadané anime:" +" "+self.last_anime)
        label.grid(row=self.row + 11, column=self.column)

    def add_anime(self):
        data = [self.episode_anime.get(), self.last_episode_anime.get(), self.genre_anime.get(),
                self.quality_anime.get(), self.note_anime.get()]

        if self.name_anime.get() != "":
            self.dManager.add_new_anime_to_db(self.name_anime.get())
            self.last_anime = self.name_anime.get()
            self.dManager.write_to_file(self.name_anime.get(), data)
        self.name_anime.delete(0, 'end')
        self.create_layout()
