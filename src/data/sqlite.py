import sqlite3


class Data:
    """
    A class to interact with a SQLite database, specifically designed to work with a dictionary database.

    Attributes:
        index (int): A counter to keep track of the current page of results.
        connection (sqlite3.Connection): A SQLite connection object to the database.
        cursor (sqlite3.Cursor): A cursor object used to execute SQL queries.
        db (list): A list of tuples containing the rows fetched from the database.

    Methods:
        get_next_page(): Returns the next page of results from the database.
    """

    def __init__(self, path: str, debug=False, limit: int = None, offset: int = None) -> None:
        """
        Initializes the Data class by connecting to the SQLite database and fetching all rows from the 'dictionnaire' table.

        Parameters:
            path (str): The file path to the SQLite database.
        """
        self.index = 0
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        if debug:
            self.db = self.cursor.execute(f"""SELECT francais, pierrick, phonétique, classe, commentaire,
                                                définition, étymologie, cyrilic, hangeul
                                         FROM dictionnaire
                                         LIMIT ${limit} OFFSET ${offset}""").fetchall()
        else:
            self.db = self.cursor.execute("""SELECT francais, pierrick, phonétique, classe, commentaire,
                                                définition, étymologie, cyrilic, hangeul
                                             FROM dictionnaire""").fetchall()

    def get_next_page(self) -> tuple[str] | bool:
        """
        Increments the index and returns the next row from the database.

        Returns:
            tuple[str]: A tuple containing the data of the next row in the database.
            False: If there are no more rows to fetch.
        """
        if self.index >= len(self.db):
            return False
        self.index += 1
        return self.db[self.index - 1]