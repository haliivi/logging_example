import logging.config
from settings import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')

words = ['new house', 'apple', 'ice cream', 3]


def main():
    for item in words:
        try:
            print(item.split(' '))
        except:
            # logger.debug(f'Exception here, {item=}', exc_info=True)  # forward traceback to debug message
            logger.exception(f'Exception here, {item=}')  # forward traceback another way


if __name__ == '__main__':
    main()
