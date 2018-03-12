import tkinter
from tkinter import ttk
from tkinter.font import Font
from DatabaseManager import DatabaseManager

class AddDLayout(tkinter.Frame):
    def __init__(self, tkinter,row=0, column=0):
        super().__init__(tkinter)
        self.row = row
        self.dManager = DatabaseManager()
        self.column = column
        self.parent = tkinter
        self.last_anime = ""
        self.create_layout()

    def create_layout(self):
        label = tkinter.Label(self.parent, text="Přidat novou knihu", font=Font(size=40))
        label.grid(row=self.row, column=self.column, columnspan=self.column + 3)

        label = tkinter.Label(self.parent, text="Kniha", font=Font(size=20))
        label.grid(row=self.row + 1, column=self.column)

        confirm_newA_button = tkinter.Button(self.parent, text="Přidat knihu", command=lambda: self.add_anime(), width=15, height=2)
        confirm_newA_button.grid(row=self.row + 1, column=self.column + 1, columnspan=self.column + 2, rowspan=2)

        label = tkinter.Label(self.parent, text="Zadej název nové knihy", font=Font(size=10))
        label.grid(row=self.row + 2, column=self.column)
        self.name_anime = tkinter.Entry(self.parent)
        self.name_anime.grid(row=self.row + 3, column=self.column)


        genres1 = ["poezie", "próza"]
        genres2 = ["lyrika", "epika", "drama"]

        self.book_genreVar = tkinter.StringVar()
        self.book_genreVar2 = tkinter.StringVar()

        label = tkinter.Label(self.parent, text="Zadej žánry knihy")
        label.grid(row=self.row + 5, column=self.column)
        self.book_genreCombobox = ttk.Combobox(self.parent,  textvariable=self.book_genreVar, value=genres1, state="readonly")
        self.book_genreCombobox.grid(row=self.row + 5, column=self.column + 1)
        self.book_genre2Combobox = ttk.Combobox(self.parent, textvariable=self.book_genreVar2, value=genres2, state="readonly")
        self.book_genre2Combobox.grid(row=self.row + 5, column=self.column + 2)


        detailGenres = ["Bajka", "Báje(Mýtus)", "Legenda", "Pověst", "Pohádka", "Povídka", "Novela", "Román", "Balada",
                        "Romance", "Píseň", "Elegie", "Óda", "Epigraf", "Epitaf", "Tragédie", "Komedie", "Činohra"]
        self.detailGenresVar = tkinter.StringVar()
        label = tkinter.Label(self.parent, text="Zadej specifický literární žánr")
        label.grid(row=self.row + 6, column=self.column)
        self.detailGenresCombobox = ttk.Combobox(self.parent, textvariable=self.detailGenresVar, value=detailGenres, state="readonly")
        self.detailGenresCombobox.grid(row=self.row + 6, column=self.column + 1)

        label = tkinter.Label(self.parent, text="Zadej členění textu:")
        label.grid(row=self.row + 7, column=self.column)
        self.textDiversity = tkinter.Entry(self.parent)
        self.textDiversity.grid(row=self.row + 7, column=self.column + 1)

        tellerForm = ["ich", "er"]
        self.tellerFormVar = tkinter.StringVar()
        label = tkinter.Label(self.parent, text="Zadej formu vypravěče")
        label.grid(row=self.row + 8, column=self.column)
        self.tellerFormCombobox = ttk.Combobox(self.parent,  textvariable=self.tellerFormVar, value=tellerForm, state="readonly")
        self.tellerFormCombobox.grid(row=self.row + 8, column=self.column + 1)

        tellerType = ["subjektivní", "objetivní", "oko kamery"]
        self.tellerTypeVar = tkinter.StringVar()
        label = tkinter.Label(self.parent, text="Zadej typ vypravěče")
        label.grid(row=self.row + 9, column=self.column)
        self.tellerTypeCombobox = ttk.Combobox(self.parent, textvariable=self.tellerTypeVar, value=tellerType, state="readonly")
        self.tellerTypeCombobox.grid(row=self.row + 9, column=self.column + 1)

        speakType = ["přímá", "nepřímá", "polopřímá", "nevlastní přímá", "monolog", "dialog"]
        self.speakTypeVar = tkinter.StringVar()
        label = tkinter.Label(self.parent, text="Určete typ řeči hlavních postav")
        label.grid(row=self.row + 10, column=self.column)
        self.speakTypeCombobox = ttk.Combobox(self.parent, textvariable=self.speakTypeVar, value=speakType, state="readonly")
        self.speakTypeCombobox.grid(row=self.row + 10, column=self.column + 1)

        label = tkinter.Label(self.parent, text="Autor", font=Font(size=20))
        label.grid(row=self.row + 11, column=self.column)

        label = tkinter.Label(self.parent, text="Jmenujte autora")
        label.grid(row=self.row + 12, column=self.column)
        self.bookAutor = tkinter.Entry(self.parent)
        self.bookAutor.grid(row=self.row + 12, column=self.column + 1)

        label = tkinter.Label(self.parent, text="Zařaďte dílo do doby ve které vzniklo")
        label.grid(row=self.row + 13, column=self.column)
        self.bookAge = tkinter.Entry(self.parent)
        self.bookAge.grid(row=self.row + 13, column=self.column + 1)

        label = tkinter.Label(self.parent, text="Zařaďte autora do lit. směru")
        label.grid(row=self.row + 15, column=self.column)
        self.bookAutorWrite = tkinter.Entry(self.parent)
        self.bookAutorWrite.grid(row=self.row + 15, column=self.column + 1)

        label = tkinter.Label(self.parent, text="Jmenujte další představitele uvedeného směru")
        label.grid(row=self.row + 16, column=self.column)
        self.bookOtherAutor = tkinter.Entry(self.parent)
        self.bookOtherAutor.grid(row=self.row + 16, column=self.column + 1)

        label = tkinter.Label(self.parent, text="Jmenujte další díla tohoto autora")
        label.grid(row=self.row + 17, column=self.column)
        self.bookOtherAutorBook = tkinter.Entry(self.parent)
        self.bookOtherAutorBook.grid(row=self.row + 17, column=self.column + 1)

        label = tkinter.Label(self.parent, text="Jmenujte podobné dílo jiného autora")
        label.grid(row=self.row + 18, column=self.column)
        self.otherBook = tkinter.Entry(self.parent)
        self.otherBook.grid(row=self.row + 18, column=self.column + 1)

        label = tkinter.Label(self.parent, text="Obsah knihy", font=Font(size=20))
        label.grid(row=self.row + 6, column=self.column + 2)

        label = tkinter.Label(self.parent, text="Určete čas v knize")
        label.grid(row=self.row + 7, column=self.column + 2)
        self.bookTime = tkinter.Entry(self.parent)
        self.bookTime.grid(row=self.row + 7, column=self.column + 3)

        label = tkinter.Label(self.parent, text="Stručně shrňte základní zápletku díla:")
        label.grid(row=self.row + 8, column=self.column +2)
        self.bookPlot = tkinter.Text(self.parent, width=25, height=5)
        self.bookPlot.grid(row=self.row + 9, column=self.column + 2, rowspan=4)

        label = tkinter.Label(self.parent, text="Jak kniha/příběh začíná?")
        label.grid(row=self.row + 13, column=self.column +2)
        self.bookStart = tkinter.Text(self.parent, width=25, height=5)
        self.bookStart.grid(row=self.row + 14, column=self.column + 2, rowspan=4)

        label = tkinter.Label(self.parent, text="Jak kniha/příběh končí?")
        label.grid(row=self.row + 18, column=self.column + 2)
        self.bookEnd = tkinter.Text(self.parent, width=25, height=5)
        self.bookEnd.grid(row=self.row + 19, column=self.column + 2, rowspan=4)

        label = tkinter.Label(self.parent, text="Určete místo odehrání příběhu z celé knihy?")
        label.grid(row=self.row + 8, column=self.column + 3)
        self.bookPlace = tkinter.Text(self.parent, width=25, height=5)
        self.bookPlace.grid(row=self.row + 9, column=self.column + 3, rowspan=4)

        label = tkinter.Label(self.parent, text="Charakterizujte hlavní postavy")
        label.grid(row=self.row + 13, column=self.column + 3)
        self.bookFigures = tkinter.Text(self.parent, width=25, height=5)
        self.bookFigures.grid(row=self.row + 14, column=self.column + 3, rowspan=4)


    def add_anime(self):
        data=[self.book_genreVar.get()+", "+ self.book_genreVar2.get(), self.detailGenresVar.get(), self.textDiversity.get(), self.tellerFormVar.get(),
            self.tellerTypeVar.get(), self.speakTypeVar.get(), self.bookAutor.get(), self.bookAge.get(),
            self.bookAutorWrite.get(), self.bookOtherAutor.get(), self.bookOtherAutorBook.get(), self.otherBook.get(), self.bookTime.get(),
            self.bookPlot.get(index1=0.0, index2=tkinter.END).replace("\n", " "), self.bookStart.get(index1=0.0, index2=tkinter.END).replace("\n", " "),
            self.bookEnd.get(index1=0.0, index2=tkinter.END).replace("\n", " "), self.bookPlace.get(index1=0.0, index2=tkinter.END).replace("\n", " "),
            self.bookFigures.get(index1=0.0, index2=tkinter.END).replace("\n", " ")]

        if self.name_anime.get() != "":
            self.dManager.add_new_anime_to_db(self.name_anime.get())
            self.last_anime = self.name_anime.get()
            self.dManager.write_to_file(self.name_anime.get(), data)
        self.name_anime.delete(0, 'end')
        self.create_layout()
