# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
create time '2019/6/27 10:18'
Usage:
各种第三方插件 通过 init_app() 注册的方式 都集中此地
"""
import logging.config

from sanic_redis import SanicRedis

# Log
logger = logging.getLogger("sanic.root")

# redis
redis = SanicRedis()

__all__ = ['logger', 'redis']
