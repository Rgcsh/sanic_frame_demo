# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
"""


class ApiException(Exception):
    """项目的API处理时的基础异常"""

    def __init__(self, code=500, message=None):
        super().__init__(message)
        self.code = code
        self.message = message
