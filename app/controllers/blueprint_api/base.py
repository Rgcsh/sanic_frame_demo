# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
Usge:
蓝图级别的异常处理模块，通过 装饰器的方式定义
"""
import traceback

from sanic import Blueprint
from sanic.exceptions import NotFound

from app.core import logger
from app.utils import ApiException, json_fail_response, CodeDict

blueprint_api = Blueprint('blueprint_api', __name__)


@blueprint_api.exception(ApiException)
async def exception_handler(request, exception):
    """
    代码内部手动报出错误
    :param request:
    :param exception:
    :return:
    """
    return json_fail_response(exception.code, exception.message)


@blueprint_api.exception(NotFound)
async def exception_handler(request, exception):
    """
    404错误
    :param request:
    :param exception:
    :return:
    """
    return json_fail_response(CodeDict.not_found)


@blueprint_api.exception(Exception)
async def exception_handler(request, exception):
    """
    意外错误
    :param request:
    :param exception:
    :return:
    """
    logger.error(traceback.format_exc())
    return json_fail_response()
