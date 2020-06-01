# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren
All rights reserved
create time '2020/5/27 14:03'
"""
import json

from app.core import logger


class LogMiddleware:
    """
    日志中间件
    """

    @staticmethod
    def before_request(request):
        # 获取请求参数
        request_params = request.args
        if request.method == "POST":
            request_params = request.form
        if not request_params:
            try:
                request_params = request.json
            except Exception:
                request_params = {}

        log_info = {
            'request_params': request_params,
            'request_header': dict(request.headers),
            "url": request.url,
            "ip": request.ip,
            "method": request.method,
        }
        logger.info(log_info)

    @staticmethod
    def after_request(request, response):

        # 获取响应数据
        try:
            response_data = json.loads(response.body.decode('utf-8'))
        except Exception:
            response_data = response.body

        log_info = {
            "response_body": str(response_data)[:5000] or "UnKnown Response Data",
            'response_header': dict(response.headers),
            "url": request.url,
            "path": request.path,
            "method": request.method,
            'http_state': response.status,
        }
        logger.info(log_info)
