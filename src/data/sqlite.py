import sqlite3


class Data:

    def __init__(self, path: str) -> None:
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        self.db = self.cursor.execute("""SELECT  francais,
                                                 pierrick,
                                                 phonétique,
                                                 classe,
                                                 commentaire,
                                                 définition,
                                                 étymologie,
                                                 cyrilic,
                                                 hangeul
                                        FROM dictionnaire""").fetchall()



