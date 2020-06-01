# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
create time '2019/9/16 10:21'

Module usage:
各种中间件
"""
from .log import LogMiddleware

MIDDLEWARE = [LogMiddleware]
