# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren
All rights reserved
create time '2020/5/27 14:11'
"""
from .base import BaseConfig


class LocalConfig(BaseConfig):
    """开发环境配置"""

    # 日志
    LOGGING_INFO_FILE = '/Users/rgc/project/sanic_frame_demo/log/info.log'
    LOGGING_ERROR_FILE = '/Users/rgc/project/sanic_frame_demo/log/error.log'

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

    WORKERS = 1
