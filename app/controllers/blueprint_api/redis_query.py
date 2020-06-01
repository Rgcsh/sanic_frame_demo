# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
create time '2020/2/27 13:02'
"""

from app.utils import json_success_response, try_str, redis_lrange, str2byte, point_queue, check_blueprint_api_type, check_sign
from .base import blueprint_api
from ...core import logger


@blueprint_api.route("/redis/query", methods=['POST'])
async def blueprint_api_redis_queue_query(request):
    """
    查询当前uuid在 redis list中第几位
    使用RSA进行前端加密后端解密
    :param request:
    :return:
    """
    params = request.json
    uuid = params.get('uuid')
    blueprint_api_type = params.get('blueprint_api_type')  # test参数值  必传

    # 判断参数值是否为str
    logger.info('开始参数校验')
    uuid = try_str(uuid)

    # 判断参数是否传输
    check_blueprint_api_type(blueprint_api_type)

    # 签名校验
    await check_sign(params, ['uuid', 'blueprint_api_type', 'time_stamp'])

    blueprint_api_type_point_queue = point_queue.format(blueprint_api_type)
    res_list = await redis_lrange(blueprint_api_type_point_queue, 0, - 1)
    len_res_list = len(res_list)
    logger.info(f'获取{blueprint_api_type_point_queue} 所有数据为:{res_list}')

    # 查询前面排队人数
    this_num = str2byte(uuid)
    if this_num and this_num in res_list:
        query_num = res_list.index(this_num)
        logger.info(f'查询结果为{query_num},uuid为：{uuid}')

    # 获取当前app的配置
    _dict = request.app.config.get('blueprint_api_WORKER_COUNT_DICT')
    return json_success_response({'all_len': len_res_list,  # 队列所有数据长度
                                  'queue_len': len_res_list - _dict.get(
                                      blueprint_api_type),  # 需要排队的队列长度
                                  })
