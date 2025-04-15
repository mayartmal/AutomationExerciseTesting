import logging
from colorama import Fore, Style


class ColorFormatter(logging.Formatter):
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    RED = Fore.RED
    BLUE = Fore.BLUE
    RESET = Style.RESET_ALL

    def format(self, record):
        message = super().format(record)
        if record.levelno == logging.INFO:
            return f"{self.GREEN}{message}{self.RESET}"
        elif record.levelno == logging.DEBUG:
            return f"{self.BLUE}{message}{self.RESET}"
        elif record.levelno == logging.WARNING:
            return f"{self.YELLOW}{message}{self.RESET}"
        elif record.levelno == logging.ERROR:
            return f"{self.RED}{message}{self.RESET}"
        return message


def get_logger(name: str = "my_app", level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("api_logs")
    console_formatter = ColorFormatter(
        fmt="[%(asctime)s] %(levelname)s: %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_formatter = logging.Formatter(
        fmt="[%(asctime)s] %(levelname)s: %(name)s: %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(console_formatter)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger
