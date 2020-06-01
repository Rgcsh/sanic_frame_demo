# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren
All rights reserved
create time '2020/5/28 09:53'
"""
import time


async def current_timestamp(is_int=False):
    """
    生成当前日期的时间戳
    """
    if not is_int:
        return time.time()
    return int(time.time())
