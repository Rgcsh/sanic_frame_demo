# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
create time "2020/5/7 21:49"

Module usage:
RSA加密解密函数
"""
import base64
import traceback

from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA

from .exceptions import ApiException
from .timer import current_timestamp
from .transform import str2byte
from ..core import logger


async def decrypt_str(cipher_text):
    """
    解密
    :param cipher_text:
    :return:
    """
    with open("master-private.pem") as f:
        key = f.read()
    try:
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        # text = cipher.decrypt(cipher_text, random_generator)
        # 使用base64解密，(在前端js加密时自动是base64加密)
        text = cipher.decrypt(base64.b64decode(cipher_text), Random.new().read)
    except Exception as _:
        logger.error(traceback.format_exc())
        raise ApiException(1009)
    return text


async def encrypt_str(_str):
    """
    加密字符串
    :param _str:
    :return:
    """
    # 被加密的数据
    message = str2byte(_str)
    # 打开公钥文件
    with open("master-public.pem") as f:
        key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    # 加密时使用base64加密
    cipher_text = base64.b64encode(cipher.encrypt(message))
    # cipher_text = cipher.encrypt(message)
    return cipher_text


async def check_sign(params, field_order):
    """
    检查签名是否合法
    对 field_order参数值按照顺序拼接后的数据 和 sign参数值解密后的数据比较是否想等，并且 time_stamp 值必须在最近60s内
    :param params:
    :param field_order:需要校验的参数排序
    :return:
    """
    logger.info("开始检查签名是否合法")
    user_input_sign = params.pop("sign")
    user_input_time = params.get("time_stamp")
    # 拼接用户输入的值
    result_list = []
    for key in field_order:
        result_list.append(str(params[key]))
    user_input_val_str = str2byte("_".join(result_list))

    # 解码并查看签名是否正确
    decrypt_result = await decrypt_str(user_input_sign)
    logger.info(f"解码结果:{decrypt_result},拼接结果:{user_input_val_str}")
    if user_input_val_str != decrypt_result or str2byte(str(user_input_time)) not in decrypt_result:
        raise ApiException(1007)

    # 查看时间戳是否过长
    this_time = await current_timestamp()
    if this_time - int(user_input_time) > 60:
        raise ApiException(1008)
