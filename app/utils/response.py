# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
"""

from sanic import response

from .messages import error_message, CodeDict


def json_response(code=200, body=None, message="", extend=None, headers=None):
    """
    通用json响应方法
    :param code: 响应码
    :param body: 响应主体
    :param message: 响应的错误消息
    :param extend: 基础参数扩展
    :type extend: dict
    :param headers: 扩展响应头
    :type headers:dict
    :return: JSON
    """
    result = {
        "respCode": code,
        "respMsg": message,
        "result": body if body is not None else {}
    }

    # 如果追加了其它参数，则合并
    if extend and isinstance(extend, dict):
        result = dict(result, **extend)

    return response.json(body=result, headers=headers)


def json_success_response(body=None, extend=None, headers=None):
    """
    响应内容正确
    :param body: 响应体
    :param extend: 扩展参数
    :param headers: 响应头参数
    """
    return json_response(body=body, message=error_message.get(200, ""),
                         extend=extend, headers=headers)


def json_fail_response(code=CodeDict.fail, message=None, extend=None, headers=None, body=None):
    """
    请求出错的响应
    :param code: 响应错误识别码
    :param message: 错误友好提示内容
    :param extend: 扩展参数
    :param headers: 响应头参数
    :param body:
    :return:
    """
    if not message:
        try:
            message = error_message[code]
        except KeyError:
            code = 20003
            message = error_message.get(code)
    if not body:
        body = {}

    return json_response(code, body=body, message=message,
                         extend=extend, headers=headers)
