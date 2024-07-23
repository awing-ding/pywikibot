import unittest
from src.data.sqlite import Data
import pathlib


class MyTestCase(unittest.TestCase):
    def test_connection(self):
        path = pathlib.Path().resolve().parent.parent / "data" / "database_linguistique.db"
        print(str(path))
        bdd = Data(str(path))
        self.assertIsNotNone(bdd.connection)
        self.assertIsNotNone(bdd.cursor)
        self.assertIsNotNone(bdd.db)


if __name__ == '__main__':
    unittest.main()
