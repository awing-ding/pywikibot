from datetime import datetime
from .colors import Colors


class File:
    """
    A class to handle file operations for logging.
    """

    def __init__(self):
        """
        Initializes the File class with a default log file path.
        """
        self.path = "log.log"

    def log(self, message: str) -> None:
        """
        Appends a log message to the log file.

        Args:
            message (str): The log message to be written to the file.
        """
        with open(self.path, 'a', encoding='utf-8') as file:
            file.write(message + '\n')

    def create_file(self) -> None:
        """
        Creates a new log file and writes the initial log entry with the current timestamp.
        """
        with open(self.path, "w", encoding='utf-8') as file:
            file.write(datetime.now().strftime('%d.%m.%Y %H:%M:%S') + " Starting logging.\n\n")


def init_logging() -> None:
    """
    Initializes the logging by creating a new log file.
    """
    File().create_file()


def log(message: str) -> None:
    """
    Logs a message with the current timestamp.

    Args:
        message (str): The log message to be written to the file.
    """
    File().log("[" + str(datetime.now()) + "] " + message)


def warn(message: str) -> None:
    """
    Logs a warning message with the current timestamp and prints it to the console.

    Args:
        message (str): The warning message to be logged and printed.
    """
    File().log("[" + str(datetime.now()) + "] WARNING:" + message)
    print(f"{Colors.BROWN} WARNING: {message}{Colors.END}")


def error(message: str) -> None:
    """
    Logs an error message with the current timestamp and prints it to the console.

    Args:
        message (str): The error message to be logged and printed.
    """
    File().log("[" + str(datetime.now()) + "] ERROR:" + message)
    print(f"{Colors.RED} ERROR: {message}{Colors.END}")


def info(message: str) -> None:
    """
    Logs an informational message with the current timestamp and prints it to the console.

    Args:
        message (str): The informational message to be logged and printed.
    """
    File().log("[" + str(datetime.now()) + "] INFO:" + message)
    print(f"{Colors.BLUE} INFO: {message}{Colors.END}")
