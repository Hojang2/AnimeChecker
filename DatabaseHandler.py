import io
class DatabaseHandler:

    def __init__(self):
        name_database = open("AnimeDatabase/MainAnime.txt", mode="r")
        self.refractore_names = name_database.read().splitlines()
        name_database.close()

    def add_new_anime_to_db(self, anime=""):
        name_database = open("AnimeDatabase/MainAnime.txt", mode="w")
        if(self.check_database(self.refractore_names, anime) != True):
            self.refractore_names.append(anime)
            anime_database = open("AnimeDatabase/" + anime + ".txt", mode="w")
            anime_database.close()
        for str in self.refractore_names:
            name_database.write(str+"\n")
        name_database.close()

    def delete_datebase(self):
        name_database = open("AnimeDatabase/MainAnime.txt", mode="w")
        for i in range(len(self.refractore_names)):
            name_database.seek(i)
            name_database.truncate()
        self.refractore_names = []
        name_database.close()

    def return_database(self):
        return self.refractore_names

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

