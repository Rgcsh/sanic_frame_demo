# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren
All rights reserved
create time '2020/2/27 13:02'
"""

from app.utils import json_success_response, point_queue, redis_del
from .base import blueprint_api
from ...core import logger


@blueprint_api.route("/redis/clean", methods=['POST'])
async def blueprint_api_redis_clean(request):
    """
    清空redis test 的相关队列数据
    :param request:
    :return:
    """
    logger.info('开始清空redis 队列数据')
    test_result = await redis_del(point_queue.format('test'))
    return json_success_response(f'清空结果 test:{test_result},test:{test_result}')
