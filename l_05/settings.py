import logging


class NewFunctionFilter(logging.Filter):
    def filter(self, record):
        print(dir(record))  # make sure attribute name_ add
        return record.funcName == 'new_function'


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
            'filters': ['new_filter']
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console'],
            # 'propagate': False,
        }
    },
    'filters': {
        'new_filter': {
            '()': NewFunctionFilter
        }
    },
    # 'root': {},  # '' : {} - designation root logger
    # 'incremental': True,  # is additional config
}
