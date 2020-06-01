# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
create time '2019/9/17 10:18'
"""
from .base import BaseConfig


class DevelopConfig(BaseConfig):
    """开发环境配置"""
    # 日志
    LOGGING_INFO_FILE = '/xxx/log/info.log'
    LOGGING_ERROR_FILE = '/xxx/log/error.log'

    # redis
    REDIS = {
        'address': ('127.0.0.1', 6379),
        'db': 8,
        'password': 'xxx',
        # 'ssl': None,
        # 'encoding': None,
        # 'minsize': 1,
        # 'maxsize': 10
    }

    WORKERS = 4
