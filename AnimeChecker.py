#!/usr/bin/env python3
import tkinter

class Checker(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Pro moje anime")
        self.parent.minsize(900, 600)
        self.parent.resizable(True, True)
        self.create_widgets()

    def create_widgets(self):
        self.label = tkinter.Label(text="Moje nejoblíbenější Anime")
        self.label.pack()

root = tkinter.Tk()
app = Checker(root)
app.mainloop()
