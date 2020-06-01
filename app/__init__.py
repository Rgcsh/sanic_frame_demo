# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
create time '2019/9/16 10:21'

Module usage:
初始化app及各种配置，拓展，中间件，蓝图的地方
"""
import importlib
import logging.config
import os

from sanic import Sanic
from sanic_cors import CORS

import app.core as core
from app import controllers
from app.middleware import MIDDLEWARE
from config import get_config


def configure_extensions(sanic_app):
    """
    Register All of Extensions
    :param sanic_app: sanic app
    :return:
    """
    for extension in core.__all__:
        obj = getattr(core, extension)
        if hasattr(obj, 'init_app'):
            obj.init_app(sanic_app)

    # cors
    if sanic_app.config.get('ENABLE_CORS'):
        CORS(sanic_app)


def configure_blueprints(sanic_app):
    """
    Register BluePrints for sanic
    通过文件夹灵活导入蓝图，只要在 app.controllers.__init__.py 文件中添加新的蓝图名即可
    :param sanic_app: sanic的实例
    :return:
    """
    controller_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'controllers')

    for module_name in controllers.__all__:
        module_path = os.path.join(controller_dir, module_name)

        assert os.path.isdir(module_path) and not module_name.startswith('__'), \
            f'{module_name} 不是有效的文件夹, 无法导入模块'

        # 预导入所有接口文件
        for file_name in os.listdir(module_path):
            if file_name.endswith('.py') and not file_name.startswith('__'):
                module = importlib.import_module(
                    f'app.controllers.{module_name}.{file_name[:-3]}')
        # 导入模块并注册蓝图
        module = importlib.import_module(f'app.controllers.{module_name}.base')
        sanic_app.register_blueprint(
            getattr(module, module_name), url_prefix=('/' + module_name))


def configure_middleware(sanic_app):
    """
    Register middleware for sanic
    通过app的 register_middleware() 注册中间件，此次分别在request和reponse时进行注册
    新增中间件，只需在 app.middleware.__init__.py 文件中添加中间件类名即可
    :param sanic_app: sanic app
    """
    for middle in MIDDLEWARE:
        sanic_app.register_middleware(middle.before_request, attach_to='request')
        sanic_app.register_middleware(middle.after_request, attach_to='response')


def create_app(env=None):
    """
    Create an app with config file
    生成app，并配置各种插件等等
    :return: sanic App
    """
    # init a sanic app
    app = Sanic(__name__)
    config = get_config(env)

    # 配置日志
    logging.config.dictConfig(config.BASE_LOGGING)

    # 加载sanic的配置内容
    app.config.from_object(config)

    # 配置所有的sanic扩展
    configure_extensions(app)

    # 配置蓝图
    configure_blueprints(app)

    # 配置中间件
    configure_middleware(app)

    return app
