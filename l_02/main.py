import logging

logging.basicConfig()
app_logger = logging.getLogger('app_logger')  # return named logger

console_handler = logging.StreamHandler()  # initialize handler
app_logger.addHandler(console_handler)  # bind handler
f = logging.Formatter(fmt='%(levelname)s - %(name)s - %(message)s')  # init formatter
console_handler.setFormatter(f)  # bind formatter to handler
# print(app_logger.handlers)  # print handlers app_logger
# print(app_logger.parent.handlers)  # print root logger handlers
# # print(app_logger.parent) - print parent logger (root.app_logger)
# # set child logger
# # default level logger equals parent level logger
utils_logger = logging.getLogger('app_logger.utils_logger')
utils_logger.setLevel('DEBUG')  # set level logger
# # utils_logger.propagate = False  # turn off propagation utils_logger
# print(utils_logger.handlers)  # print handlers utils_logger


def main():
    utils_logger.debug('Hello world')


if __name__ == '__main__':
    main()
