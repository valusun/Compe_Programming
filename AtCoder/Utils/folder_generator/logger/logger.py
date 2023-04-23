import logging


# NOTE: 使ってないけど備忘のため残す
def get_logger() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    format_setting = "%(asctime)s [%(levelname)s] %(message)s"
    formatter = logging.Formatter(format_setting)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
