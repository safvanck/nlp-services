
# importing module
import logging
import sys

logger = logging.getLogger('MAIN LOGGER')
log_level = logging.DEBUG
# log_filename = datetime.now().strftime('%Y-%m-%d') + '.log'
logger.setLevel(log_level)
formatter = logging.Formatter('%(asctime)s - [%(levelname)8s] - %(name)s - %(message)s')

fh = logging.FileHandler(filename="log/service.log")
fh.setLevel(log_level)
fh.setFormatter(formatter)
logger.addHandler(fh)

sh = logging.StreamHandler(sys.stdout)
sh.setLevel(log_level)
sh.setFormatter(formatter)
logger.addHandler(sh)

# Debug messages
logger.debug("Here is debug Message")
# Debug messages
logger.info("This is just an information")
# Warning messages
logger.warning("Oops ! Its a Warning")
# Error message
logger.error("Did you try to reach out of bound index ")
# critical message
logger.critical("Server went down")

