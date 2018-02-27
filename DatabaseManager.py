import os
class DatabaseManager:
    def add_new_anime_to_db(self, anime=""):
        refractore_names = self.return_database()
        name_database = open("MainAnime.txt", mode="w")
        if(self.check_database(refractore_names, anime) != True):
            refractore_names.append(anime)
            anime_database = open("AnimeDatabase/" + anime + ".txt", mode="w")
            anime_database.close()
        for str in refractore_names:
            name_database.write(str+"\n")
        name_database.close()

    def delete_datebase(self):
        name_database = open("MainAnime.txt", mode="w")
        for i, name in enumerate(self.return_database()):
            os.remove("AnimeDatabase/" + name + ".txt")
            name_database.seek(i)
            name_database.truncate()
        name_database.close()

    def return_database(self):
        name_database = open("MainAnime.txt", mode="r")
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

