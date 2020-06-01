# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren
All rights reserved
create time '2020/5/25 18:29'
异步redis的二层封装函数
"""
from app.core import redis


async def redis_get(name):
    """
    获取某个key的值
    :param name:
    :return:
    """
    with await redis.conn as r:
        return await r.get(name)


async def redis_llen(name):
    """
    获取list长度
    :param name:
    :return:
    """
    with await redis.conn as r:
        return await r.llen(name)


async def redis_lrange(name, start, end):
    """
    获取list范围数据
    :param name:
    :param start:
    :param end:
    :return:
    """
    with await redis.conn as r:
        return await r.lrange(name, start, end)


async def redis_rpush(name, val):
    """
    list中尾部添加新数据
    :param name:
    :param val:
    :return:
    """
    with await redis.conn as r:
        return await r.rpush(name, val)


async def redis_del(key):
    """
    删除某个key
    :param key:
    :return:
    """
    with await redis.conn as r:
        return await r.delete(key)
