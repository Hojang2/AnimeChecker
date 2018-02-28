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
        self.animeVar = tkinter.StringVar()

        label = tkinter.Label(self.parent, text="Vybraná kniha", font=Font(size=40))
        label.grid(row=self.row, column=self.column, columnspan=self.column + 3)


        delete_anime_button = tkinter.Button(self.parent, text="Smazat všechny knihy", anchor="center",
                                             command=lambda: self.delete_anime())
        delete_anime_button.grid(row=self.row + 1, column=self.column)


        self.show_anime = ttk.Combobox(self.parent, textvariable=self.animeVar, value=self.databaseM.return_database(), state="readonly")
        self.show_anime.grid(row=self.row + 1, column=self.column + 1)
        self.show_anime.bind('<<ComboboxSelected>>', self.change_description)

        label = tkinter.Label(self.parent, text="Vybraná kniha "+self.name, font=Font(size=20))
        label.grid(row=self.row +2, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[0])
        label.grid(row=self.row + 3, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[1])
        label.grid(row=self.row + 4, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[2])
        label.grid(row=self.row + 5, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[3])
        label.grid(row=self.row + 6, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[4])
        label.grid(row=self.row + 7, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[5])
        label.grid(row=self.row + 8, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[6])
        label.grid(row=self.row + 9, column=self.column)

        label = tkinter.Label(self.parent, text="Obsah knihy", font=Font(size=20))
        label.grid(row=self.row + 10, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[7])
        label.grid(row=self.row + 11, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[8])
        label.grid(row=self.row + 12, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[9])
        label.grid(row=self.row + 13, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[10])
        label.grid(row=self.row + 14, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[11])
        label.grid(row=self.row + 15, column=self.column)

        label = tkinter.Label(self.parent, text="Autor", font=Font(size=20))
        label.grid(row=self.row + 16, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[12])
        label.grid(row=self.row + 17, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[13])
        label.grid(row=self.row + 18, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[14])
        label.grid(row=self.row + 19, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[15])
        label.grid(row=self.row + 20, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[16])
        label.grid(row=self.row + 21, column=self.column)

        label = tkinter.Label(self.parent, text=self.description[17])
        label.grid(row=self.row + 22, column=self.column)

    def change_description(self, event):
        self.description = self.databaseM.read_from_file(self.animeVar.get())
        self.name = self.animeVar.get()
        self.create_layout()
        if event:
            print(event.widget.get())


    def delete_anime(self):
        self.databaseM.delete_datebase()
        self.create_layout()


