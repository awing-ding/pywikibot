from pathlib import Path
from configparser import ConfigParser

from src import Data, Bot


def main() -> None:
    config = parse_config()
    path = Path().resolve() / config["CONFIG"]["database_rel_path"]
    db = Data(str(path)).db
    for entry in db:
        bot = Bot(entry, config["CONFIG"]["namespace"], db)
        bot.run()


def parse_config() -> ConfigParser:
    config = ConfigParser()
    config.read("config.ini")
    return config


if __name__ == '__main__':
    main()
