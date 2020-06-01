# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren
All rights reserved
create time '2020/5/26 09:33'
"""
import uuid


def str2byte(_str):
    """
    str to bytes
    :param _str:
    :return:
    """
    return bytes(_str, encoding='utf8')


def byte2str(_bytes):
    """
    bytes to str
    :param _str:
    :return:
    """
    return str(_bytes, encoding="utf-8")
