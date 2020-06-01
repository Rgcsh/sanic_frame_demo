# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
create time '2020/2/27 13:02'
"""

from app.utils import json_success_response, json_fail_response, CodeDict, try_str, redis_lrange, \
    str2byte, redis_rpush, check_blueprint_api_type, point_queue, check_sign
from .base import blueprint_api
from ...core import logger


@blueprint_api.route("/redis/add", methods=['POST'])
async def blueprint_api_redis_queue_add(request):
    """
    添加redis queue的新值
    :param request:
    :return:
    """
    params = request.json
    if not params:
        return json_fail_response(CodeDict.field_val_err, '请在body中传json数据')
    uuid = params.get('uuid')
    blueprint_api_type = params.get('blueprint_api_type')  # test值  必传
    # 判断参数是否存在
    if not uuid:
        return json_fail_response(CodeDict.no_field)

    # 判断参数值是否为str
    uuid = try_str(uuid)

    # 判断参数是否传输
    check_blueprint_api_type(blueprint_api_type)

    blueprint_api_type_point_queue = point_queue.format(blueprint_api_type)

    # 签名校验
    await check_sign(params, ['uuid', 'blueprint_api_type', 'time_stamp'])

    # 检查数据是否重复
    res_list = await redis_lrange(blueprint_api_type_point_queue, 0, - 1)
    logger.info(f'获取{blueprint_api_type_point_queue} 所有数据为:{res_list}')
    this_num = str2byte(uuid)
    if this_num in res_list:
        logger.error(f'获取{blueprint_api_type_point_queue} 所有数据为:{res_list}')
        return json_fail_response(CodeDict.data_repeat)

    # 新增数据
    logger.info(f'新增redis数据为:{uuid}')
    res = await redis_rpush(blueprint_api_type_point_queue, uuid)
    if res:
        return json_success_response()
    return json_fail_response(CodeDict.redis_err)
