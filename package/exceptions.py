import logging

class PackageUpdaterException(Exception):
    def __init__(self, error, title):
        log_message = "For {title}, {error_type}: {error}".format(
            title=title, error_type=type(error), error=error
        )
        logging.critical(log_message)
        logging.exception(error)