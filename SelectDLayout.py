import tkinter
from tkinter.font import Font
from tkinter import ttk
from DatabaseManager import DatabaseManager
class SelectDLayout(tkinter.Frame):
    def __init__(self, tkinter, row=0, column=0):
        super().__init__(tkinter)
        self.row = row
        self.parent = tkinter
        self.databaseM = DatabaseManager()
        self.column = column
        self.description = self.databaseM.get_info()
        self.name = ""
        self.create_layout()

    def create_layout(self):
        self.zaklaniZnalost = []
        self.obsahKnihy = []
        self.autor = []

        label = tkinter.Label(self.parent, text="Vybraná kniha", font=Font(size=40))
        label.grid(row=self.row, column=self.column, columnspan=self.column + 1)

        self.nameLabel=tkinter.Label(self.parent, text=self.name, font=Font(size=20))
        self.nameLabel.grid(row=self.row + 1, column=self.column, columnspan=self.column + 1)

        delete_all_anime_button = tkinter.Button(self.parent, text="Smazat všechny knihy", anchor="center",
                                             command=lambda: self.delete_all_anime())
        delete_all_anime_button.grid(row=self.row + 2, column=self.column)

        delete_anime_button = tkinter.Button(self.parent, text="Smazat knihu", anchor="center",
                                             command=lambda: self.delete_anime())
        delete_anime_button.grid(row=self.row + 2, column=self.column + 1)

        self.animeVar = tkinter.StringVar()
        self.show_anime = ttk.Combobox(self.parent, textvariable=self.animeVar, value=self.databaseM.return_name_database(), state="readonly")
        self.show_anime.grid(row=self.row + 2, column=self.column + 2)
        self.show_anime.bind('<<ComboboxSelected>>', self.change_description)

        for i in range(6):
            print(i)
            self.zaklaniZnalost.append(tkinter.Label(self.parent, text=self.description[i]))
        for i in range(6):
            self.zaklaniZnalost[i].grid(row=self.row + i + 3, column=self.column)

        bookDetail = tkinter.Label(self.parent, text="Obsah knihy", font=Font(size=20))
        bookDetail.grid(row=self.row + 10, column=self.column)

        for i in range(5):
            self.obsahKnihy.append(tkinter.Label(self.parent, text=self.description[i + 6]))
        for i in range(5):
            self.obsahKnihy[i].grid(row=self.row + i + 12, column=self.column)

        bookAutor = tkinter.Label(self.parent, text="Autor", font=Font(size=20))
        bookAutor.grid(row=self.row + 16, column=self.column)

        for i in range(6):
            self.autor.append(tkinter.Label(self.parent, text=self.description[i + 11]))
        for i in range(6):
            self.autor[i].grid(row=self.row + i + 18, column=self.column)

    def change_description(self, event):
        self.name = self.animeVar.get()
        self.update_all()
        self.description = self.databaseM.read_from_file(self.name)
        self.create_layout()
        if event:
            print(event.widget.get())

    def update_all(self):
        self.description = self.databaseM.get_info()
        for i in range(6):
            self.zaklaniZnalost[i].config(text=self.description[i])
        for i in range(5):
            self.obsahKnihy[i].config(text=self.description[i + 6])
        for i in range(6):
            self.autor[i].config(text=self.description[i + 11])
        self.nameLabel.config(text="")

    def delete_all_anime(self):
        self.databaseM.delete_datebase()
        self.update_all()

    def delete_anime(self):
        self.databaseM.delete_name(self.name)
        self.name = ""

