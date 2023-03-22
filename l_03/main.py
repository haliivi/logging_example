import logging.config
from settings import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')

# print(logging.DEBUG)  # print number const 'DEBUG'
# logger = logging.getLogger('app_logger')
# logger.setLevel('DEBUG')  # change default level logger
#
# console_handler = logging.StreamHandler()  # init handler printing to console
#
# # init handler printing to file
# # apply properties mode
# file_handler = logging.FileHandler('debug.log', mode='w')
#
# logger.addHandler(console_handler)  # bind handler
# logger.addHandler(file_handler)
# # print(console_handler.level)  # print level handler
# std_format = logging.Formatter(fmt='{asctime} - {levelname} - {name} - {message}', style='{')  # init formatter
# console_handler.setFormatter(std_format)  # bind formatter
# file_handler.setFormatter(std_format)  # bind formatter


def main():
    logger.debug('Enter in to the main()')


if __name__ == '__main__':
    main()
