import logging

class ColorFormatter(logging.Formatter):
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"

    def format(self, record):
        message = super().format(record)
        if record.levelno == logging.INFO:
            return f"{self.GREEN}{message}{self.RESET}"
        elif record.levelno == logging.WARNING:
            return f"{self.YELLOW}{message}{self.RESET}"
        elif record.levelno == logging.ERROR:
            return f"{self.RED}{message}{self.RESET}"
        return message

def get_logger(name: str, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)


    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = ColorFormatter("\n[%(asctime)s] %(levelname)s:%(name)s:\n%(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger