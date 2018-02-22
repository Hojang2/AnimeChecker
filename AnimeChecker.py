#!/usr/bin/env python3
import tkinter
from DatabaseHandler import DatabaseHandler
from tkinter.font import Font
from tkinter import ttk


class Checker(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Moje anime")
        self.parent.minsize(900, 600)
        self.parent.resizable(True, True)
        self.dHandler = DatabaseHandler()
        self.data = self.dHandler.return_database()
        self.create_widgets()

    def add_new_anime(self):
        if self.new_anime.get() != "":
            self.dHandler.add_new_anime_to_db(self.new_anime.get())
            self.data = self.dHandler.return_database()
            self.show_anime.config(values=self.data)
            self.new_anime.delete(0, 'end')

    def delete_anime(self):
        self.dHandler.delete_datebase()
        self.data = self.dHandler.return_database()
        self.show_anime.config(values=self.data)

    def create_widgets(self):
        label = tkinter.Label(text="Nejoblíbenější Anime", font=Font(size=50))
        label.grid(row=0, column=0, columnspan=5, rowspan=1)

        label = tkinter.Label(text="Přidat nové Anime", font=Font(size=40))
        label.grid(row=1, column=0, columnspan=5, rowspan=1)

        label = tkinter.Label(text="Zadej název nového anime které chceš sledovat")
        label.grid(row=2, column=0)

        self.new_anime = tkinter.Entry(self.parent)
        self.new_anime.grid(row=2, column=1)
        confirm_newA_button = tkinter.Button(self.parent, text="Přidat anime",
                                             command=lambda: self.add_new_anime())
        confirm_newA_button.grid(row=2, column=2)

        label = tkinter.Label(text="Nejnovější díly", font=Font(size=40))
        label.grid(row=4, column=0, columnspan=5, rowspan=1)

        label = tkinter.Label(text="Anime které sleduješ:")
        label.grid(row=5, column=0)

        print(self.data)
        self.show_anime = ttk.Combobox(self.parent, values=self.data)
        self.show_anime.grid(row=5, column=1)

        delete_anime_button = tkinter.Button(self.parent, text="Smazat všechny anime",
                                             command=lambda: self.delete_anime(), anchor="center")
        delete_anime_button.grid(row=6, column=0, columnspan=5)

        label = tkinter.Label(text="Vybrané anime", font=Font(size=40))
        label.grid(row=7, column=0, columnspan=5, rowspan=1)
root = tkinter.Tk()
app = Checker(root)
app.mainloop()
