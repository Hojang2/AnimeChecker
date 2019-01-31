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
        self.description = [""]*5
        self.name = ""
        self.create_layout()

    def create_layout(self):
        self.animeVar = tkinter.StringVar()

        label = tkinter.Label(self.parent, text="Vybrané anime", font=Font(size=40))
        label.grid(row=self.row, column=self.column, columnspan=self.column + 3)

        delete_anime_button = tkinter.Button(self.parent, text="Smazat všechny anime", anchor="center",
                                             command=lambda: self.delete_anime())
        delete_anime_button.grid(row=self.row + 1, column=self.column)

        self.show_anime = ttk.Combobox(self.parent, textvariable=self.animeVar,
                                       value=self.databaseM.return_database(),
                                       state="readonly")
        self.show_anime.grid(row=self.row + 1, column=self.column + 1)
        self.show_anime.bind('<<ComboboxSelected>>', self.change_description)

        label = tkinter.Label(self.parent, text="Anime které sleduješ: "+self.name)
        label.grid(row=self.row +2, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[0])
        label.grid(row=self.row + 3, column=self.column, columnspan=self.column + 1)

        label = tkinter.Label(self.parent, text=self.description[1])
        label.grid(row=self.row + 4, column=self.column, columnspan=self.column + 1)

        label = tkinter.Label(self.parent, text=self.description[2])
        label.grid(row=self.row + 5, column=self.column, columnspan=self.column + 1)

        label = tkinter.Label(self.parent, text=self.description[3])
        label.grid(row=self.row + 6, column=self.column, columnspan=self.column + 1)

        label = tkinter.Label(self.parent, text=self.description[4])
        label.grid(row=self.row + 7, column=self.column, columnspan=self.column + 1)

    def change_description(self, event):
        self.description = self.databaseM.read_from_file(self.animeVar.get())
        self.name = self.animeVar.get()
        self.create_layout()
        if event:
            print(event.widget.get())

    def delete_anime(self):
        self.databaseM.delete_datebase()
        self.create_layout()
