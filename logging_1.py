import logging
from logging.handlers import RotatingFileHandler

# create logger
logger = logging.getLogger('simple_example')
#logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = RotatingFileHandler(filename='example.log', mode='a', maxBytes=2, backupCount=5,encoding=None, delay=False)
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')