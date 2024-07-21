import src.data.sqlite as data
from pathlib import Path


def main() -> None:
    path = Path().absolute().as_posix()
    db = data.Data(path)
    for entry in db.db :
        print(entry)




if __name__ == '__main__':
    main()
