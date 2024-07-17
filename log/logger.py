import logging

# https://qna.habr.com/q/728803
# https://realpython.com/python-logging/
logger = logging.getLogger()

file_log = logging.FileHandler('logging.log')
console_out_log = logging.StreamHandler()

logging.basicConfig(handlers=(file_log, console_out_log), 
                    format='[%(asctime)s | %(name)s | %(levelname)s]: %(message)s', 
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)