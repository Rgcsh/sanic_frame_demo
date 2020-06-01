# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren
All rights reserved
create time '2020/5/25 17:30'
"""

from .exceptions import ApiException
from .messages import CodeDict
from .response import json_fail_response


def try_str(val):
    """
    尝试把值转为str,失败 则直接 raise错误
    :param val:
    :return:
    """
    if not val:
        return val
    try:
        return str(val)
    except Exception:
        raise json_fail_response(CodeDict.field_val_err)


def check_blueprint_api_type(blueprint_api_type):
    """
    blueprint_api_type必传，而且值范围固定
    :param blueprint_api_type:
    :return:
    """
    if blueprint_api_type not in ['test']:
        raise ApiException(CodeDict.field_val_err, 'blueprint_api_type参数值错误')
