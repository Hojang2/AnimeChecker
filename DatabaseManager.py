import os
class DatabaseManager:
    def add_new_anime_to_db(self, anime=""):
        refractore_names = self.return_database()
        name_database = open("MainDiaryDetails.txt", mode="w")
        if(self.check_database(refractore_names, anime) != True):
            refractore_names.append(anime)
            self.write_to_file(anime)
        for str in refractore_names:
            name_database.write(str+"\n")
        name_database.close()

    def delete_datebase(self):
        name_database = open("MainDiaryDetails.txt", mode="w")
        refractore_names=self.return_database()
        for i, name in enumerate(refractore_names):
            os.remove("DiaryDatabase/" + name + ".txt")
            name_database.seek(i)
            name_database.truncate()
        name_database.close()

    def write_to_file(self, name="", data=[]):
        info_list = ["Pocet epizod:", "Poslední viděná epizoda:", "Žánr:", "Kvalita:", "Poznámka:"]
        anime_data = open("DiaryDatabase/" + name + ".txt", mode="w")
        for i, data in enumerate(data):
            anime_data.write(info_list[i]+" "+str(data)+"\n")
        anime_data.close()

    def read_from_file(self, file_name):
        anime_data=open("DiaryDatabase/" + file_name + ".txt", mode="r")
        return anime_data.read().splitlines()

    def return_database(self):
        name_database = open("MainDiaryDetails.txt", mode="r")
        refractore_names = name_database.read().splitlines()
        name_database.close()
        return refractore_names

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

