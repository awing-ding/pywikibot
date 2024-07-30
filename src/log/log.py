from datetime import datetime


class File:
    def __init__(self):
        self.path = log.log

    def log(self, message: str) -> None:
        with open(self.path, 'a') as file:
            file.write(message + '\n')


def log(message: str) -> None:
    File().log("[" + str(datetime.now()) + "] " + message)