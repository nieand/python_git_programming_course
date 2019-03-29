"""
Example file for ipdb exercise.

Find out why logging.info() doesn't print anything!
"""
import logging

logger = logging.getLogger()
logger.addHandler(logging.NullHandler())

logging.basicConfig(format='%(asctime)s %(message)s')

# FIXME this does not print anything to STDOUT, why?
logging.info("Hello World!")
