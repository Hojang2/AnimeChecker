import os
class DatabaseManager:
    def __init__(self):
        self.info_list = ["Žánr knihy:", "Specifický literární žánr:", "Členění textu:", "Forma vypravěče:",
                          "Typ vypravěče:", "Typ řečí hlavních postav:", "Autor:", "Doba vzniku díla:", "Literární směr:",
                          "Další představitelé:", "Další díla:", "Podobné dílo:", "Čas v knize:", "Zápletka díla:", "Začátek:", "Konec:",
                           "Místo příběhu:", "Hlavní postavy:"]

    def add_new_anime_to_db(self, book="", createFile=True):
        refractore_names = self.return_name_database()
        name_database = open("MainDiaryDetails.txt", mode="w")
        if(self.check_database(refractore_names, book) != True):
            refractore_names.append(book)
            if(createFile):
                self.write_to_file(book)
        for str in refractore_names:
            name_database.write(str+"\n")
        name_database.close()

    def delete_datebase(self):
        refractore_names=self.return_name_database()
        name_database = open("MainDiaryDetails.txt", mode="w")
        for i, name in enumerate(refractore_names):
            name_database.seek(i)
            name_database.truncate()
        name_database.close()

    def remove_file(self, name=""):
        os.remove(name + ".txt")

    def delete_name(self, name=""):
        refractore_names2 = []
        print(name)
        refractore_names = self.return_name_database()
        for name_in in refractore_names:
            if name != name_in:
                refractore_names2.append(name_in)

        self.delete_datebase()
        name_database = open("MainDiaryDetails.txt", mode="w")
        for i in range(len(refractore_names2)):
            name_database.write(refractore_names2[i]+"\n")


    def write_to_file(self, name="", data=[]):
        anime_data = open(name + ".txt", mode="w")
        for i, data in enumerate(data):
            anime_data.write(self.info_list[i]+" "+str(data)+"\n")
        anime_data.close()

    def read_from_file(self, file_name):
        anime_data=open(file_name + ".txt", mode="r")
        return anime_data.read().splitlines()

    def get_info(self):
        return self.info_list

    def return_name_database(self):
        self.is_file_there()
        name_database = open("MainDiaryDetails.txt", mode="r")
        refractore_names = name_database.read().splitlines()
        name_database.close()
        return refractore_names

    def is_file_there(self):
        try:
            name_database = open("MainDiaryDetails.txt", mode="r")
            name_database.close()
        except:
            name_database2 = open("MainDiaryDetails.txt", mode="w")
            name_database2.close()

    def check_database(self, database, name=""):
        for anime in database:
            if anime == name:
                return True
        return False

    def check_symbol(self, string="", symbol=""):
        for a in string:
            if a == symbol:
                    return True
        return False

    def load_book(self, name=""):
        try:
            name_database = open(name + ".txt", mode="r")
            self.add_new_anime_to_db(name, createFile=False)
        except:
            print ("Soubor neexistuje")

