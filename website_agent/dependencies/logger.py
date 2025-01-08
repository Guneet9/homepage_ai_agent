import logging


logger = logging.getLogger("HOMEPAGE_ANALYSIS_API")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Console handler to display logs in the terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Log INFO and above to the console
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
