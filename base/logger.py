import logging

logging.basicConfig(filename='example.log', format='%(levelname)s: %(asctime)s -- %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filemode='w',level=logging.DEBUG)
logging.debug('this message should go to file')
logging.info('and this')
logging.warning('and this')
# logging.log(level=logging.DEBUG)
#test
