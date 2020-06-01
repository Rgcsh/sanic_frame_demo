# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
"""
__author__ = 'Rgc'
__time__ = '2019-02-19 10:30'


class CodeDict:
    success = 200
    not_found = 404
    method_not_allow = 405
    fail = 500
    no_field = 1000
    not_unique = 1001
    field_val_err = 1002
    data_repeat = 1003
    db_error = 1004
    no_data = 1005
    redis_err = 1006


error_message = {
    # Base
    200: "请求成功",
    404: "找不到相关资源",
    405: "方式不被允许",
    500: "请求处理失败",

    1000: "参数不存在",
    1001: "数据不唯一错误",
    1002: "参数值错误",
    1003: "数据重复",
    1004: "数据库错误",
    1005: "数据不存在",
    1006: "redis错误",
    1007: "签名错误",
    1008: "签名失效",
    1009: "签名解密失败",

    # message
    20003: "error_message中没有这个code",

}
