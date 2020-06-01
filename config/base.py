# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
create time '2019/9/17 10:18'

"""


class BaseConfig(object):
    """配置基类"""
    DEBUG = False

    # 随机秘钥
    SECRET_KEY = '930kmdio8093ijv0f2e32poej-o=[==3fjpeserds2-09kd0w[v-rt5-4ktnpo2-01%h&b=jfx$x01'

    # 关闭，否则影响server性能
    ACCESS_LOG = False

    # 服务worker数量
    WORKERS = 4

    # 跨域相关
    ENABLE_CORS = False  # 是否启动跨域功能
    CORS_SUPPORTS_CREDENTIALS = True

    # redis
    REDIS = {
        'address': ('127.0.0.1', 6379),
        'db': 8,
        # 'password': 'password',
        # 'ssl': None,
        # 'encoding': None,
        # 'minsize': 1,
        # 'maxsize': 10
    }

    # 日志配置，兼容 sanic内置log库
    LOGGING_INFO_FILE = None
    LOGGING_ERROR_FILE = None
    BASE_LOGGING = {
        'version': 1,
        'loggers': {
            "sanic.root": {"level": "INFO", "handlers": ["console", 'info_file', 'error_file']},
        },
        'formatters': {
            'default': {
                'format': '%(asctime)s | %(levelname)s | %(message)s',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'default',
            },
            'info_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': LOGGING_INFO_FILE,
                'maxBytes': (1 * 1024 * 1024),
                'backupCount': 10,
                'encoding': 'utf8',
                'level': 'INFO',
                'formatter': 'default',
            },
            'error_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': LOGGING_ERROR_FILE,
                'maxBytes': (1 * 1024 * 1024),
                'backupCount': 10,
                'encoding': 'utf8',
                'level': 'ERROR',
                'formatter': 'default',
            },
        },
    }

    def __init__(self):
        if self.LOGGING_INFO_FILE:
            self.BASE_LOGGING['handlers']['info_file']['filename'] = self.LOGGING_INFO_FILE

        if self.LOGGING_ERROR_FILE:
            self.BASE_LOGGING['handlers']['error_file']['filename'] = self.LOGGING_ERROR_FILE
