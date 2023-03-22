import logging.config
from settings import logger_config


logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


def new_function():
    name = 'Oleg'
    logger.debug('Enter in to the new_function()', extra={'name_': name})  # set dict with extra parameter


def main():
    logger.debug('Enter in to the main()')


if __name__ == '__main__':
    main()
    new_function()
