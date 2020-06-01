# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
create time '2019/9/16 10:21'

Module usage:
基础中间件
"""


class BaseMiddleWare:

    @staticmethod
    def before_request(request):
        """
        请求之前的处理函数
        """

    @staticmethod
    def after_request(request, response):
        """
        请求处理完成之后的处理函数
        :param response: 原始响应
        :return: 响应
        """
