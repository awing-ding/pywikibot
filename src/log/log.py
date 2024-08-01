from datetime import datetime


class File:
    def __init__(self):
        self.path = "log.log"

    def log(self, message: str) -> None:
        with open(self.path, 'a', encoding='utf-8') as file:
            file.write(message + '\n')

    def create_file(self) -> None:
        with open(self.path, "w", encoding='utf-8') as file:
            file.write(datetime.now().strftime('%d.%m.%Y %H:%M:%S') + " Starting logging.\n\n")


def log(message: str) -> None:
    File().log("[" + str(datetime.now()) + "] " + message)