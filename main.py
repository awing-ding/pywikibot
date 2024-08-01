from pathlib import Path
from configparser import ConfigParser

from src import Data, Bot


def main() -> None:
    config = parse_config()
    namespace = config["CONFIG"]["namespace"]
    namespace_id = int(config["CONFIG"]["namespace_id"])
    path = Path().resolve() / config["CONFIG"]["database_rel_path"]
    if config["CONFIG"]["debug"] == "True":
        db = Data(str(path), True, int(config["CONFIG"]["limit"]), int(config["CONFIG"]["offset"]))
        Bot(namespace, namespace_id, db).treat_pages()
    else:
        db = Data(str(path)).db
        Bot(namespace, namespace_id, db).treat_pages()


def parse_config() -> ConfigParser:
    config = ConfigParser()
    config.read("config.ini")
    return config


if __name__ == '__main__':
    main()
