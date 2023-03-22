import logging
import requests

logging.basicConfig(level='DEBUG', filename='mylog.log')
logger = logging.getLogger()
# print(logging.getLogger('urllib3')) - print specific logger
logging.getLogger('urllib3').setLevel('CRITICAL')  # turn off other logger
# logger.setLevel('DEBUG') - set level logger
# print(logger.level)      - print level logger
# print(logger.handlers)   - print handlers logger
# [print(logger_) for logger_ in logging.Logger.manager.loggerDict] - print all logger


def main(name):
    logger.debug(f'Enter in the main() function: name = {name}')
    r = requests.get('https://www.google.ru')


if __name__ == '__main__':
    main('Oleg')
