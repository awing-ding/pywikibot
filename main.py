import src.data.sqlite as data
from pathlib import Path


def main() -> None:
    path = Path().resolve() / "data" / "database_linguistique.db"
    db = data.Data(str(path))




if __name__ == '__main__':
    main()
