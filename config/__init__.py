# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
create time '2019/9/17 10:18'
Usage:
配置类 模块
"""

import os

from .base import BaseConfig
from .develop import DevelopConfig
from .product import ProductConfig

try:
    from .local import LocalConfig
except ImportError:
    # 其他环境不需要编写本地配置文件
    LocalConfig = None

ConfigMap = {
    'LOCAL': LocalConfig,
    'DEV': DevelopConfig,
    'PROD': ProductConfig,
}

# 设置环境变量
SANIC_ENV = os.environ.get('SANIC_ENV', 'LOCAL')


def get_config(env=None) -> BaseConfig:
    if not env:
        # 获取环境变量, 默认使用本地环境
        env = SANIC_ENV
    env = env.upper()

    config_cls = ConfigMap.get(env)
    if not config_cls:
        raise EnvironmentError(
            '环境配置错误, 默认使用 LOCAL 环境, 需要 config/local.py 文件.'
            '若要切换其他环境的配置, 需设置环境变量, 如 SANIC_ENV=TEST.')
    return config_cls()
