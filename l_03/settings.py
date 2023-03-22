logger_config = {
    'version': 1,
    'disable_existing_loggers': False,  # disable or enable loggers listed in key loggers
    'formatters': {
        'std_format': {
            'format': '{asctime} - {levelname} - {name} - {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console'],
            # 'propagate': False,
        }
    },
    # 'filters': {},
    # 'root': {},  # '' : {} - designation root logger
    # 'incremental': True,  # is additional config
}
