import logging


class MegaHandler(logging.Handler):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def emit(self, record):
        msg = self.format(record)
        with open(self.filename, 'w') as file:
            file.write(msg + '\n')


logger_config = {
    'version': 1,
    'disable_existing_loggers': False,  # disable or enable loggers listed in key loggers
    'formatters': {
        'std_format': {
            'format': '{asctime} - {levelname} - {name} {module}:{funcName}:{lineno} - {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
        },
        'file': {
            '()': MegaHandler,
            'level': 'DEBUG',
            'filename': 'debug.log',
            'formatter': 'std_format',
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            # 'propagate': False,
        }
    },
    # 'filters': {},
    # 'root': {},  # '' : {} - designation root logger
    # 'incremental': True,  # is additional config
}
