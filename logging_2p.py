import logging
# `logging.warning('Watch out!')  # will print a message to the console
# logging.info('I told you so')  # will not print anything`

#################################################################################################################

# logging.basicConfig(filename='example_test_2nd.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

#################################################################################################################

# logging.basicConfig(format='%(asctime)s:%(name)s:%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.debug('This message should appear on the console')
# logging.info('So should this')
# logging.warning('And this, too')


###########################################################################################

# Capturing Stack Traces:
# Exception information can be captured if the exc_info parameter is passed as True

# import logging

# a = 5
# b = 0

# try:
#   c = a / b
# except Exception as e:
#   logging.error("Exception occurred", exc_info=True)


# calling logging.exception() is like calling logging.error(exc_info=True)

# import logging

# a = 5
# b = 0
# try:
#   c = a / b
# except Exception as e:
#   logging.exception("Exception occurred")


#Handler 

import logging

#create custom logger 
logger = logging.getLogger(__name__)

#create handler 
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

#create formatters and add it to handlers

c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

#Add handlers to the logger 
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is warning')
logger.error('This is an error')


