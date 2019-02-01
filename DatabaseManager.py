from json import dump, load
from os import remove


class DatabaseManager:

    def __init__(self, path: str):
        self.__content = {}
        self.__template = ["Name", "Number of episodes",
                           "Last episode", "Kind", "Quality", "Note"]
        self.__path = path

    def add(self, data: list) -> None:
        temp = {}
        for i in range(len(self.__template)):
            if len(self.__template) == len(data):
                temp[self.__template[i]] = ""
            else:
                temp[self.__template[i]] = data[i]

        self.__content[len(self.__content)] = temp

    def delete_data(self) -> None:
        self.__content = {}
        self.remove_database()

    def save(self) -> None:
        try:
            dump(self.__path, self.__content)
        except FileNotFoundError as e:
            print(e)

    def load(self) -> None:
        self.__content = load(self.__path, strict=False)

    def remove_database(self) -> None:
        remove(self.__path)

    def reload(self) -> None:
        self.save()
        self.load()
