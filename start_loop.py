# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren
All rights reserved
create time '2020/6/1 14:15'
"""
import asyncio
from signal import signal, SIGINT

import uvloop

from app import create_app
from app.core import logger

app = create_app()
workers = app.config.get('WORKERS')
app.debug = app.config.get('DEBUG')
serv_coro = app.create_server(host="0.0.0.0", port=5001, return_asyncio_server=True)

# 设置uvloop相关
asyncio.set_event_loop(uvloop.new_event_loop())
loop = asyncio.get_event_loop()
serv_task = asyncio.ensure_future(serv_coro, loop=loop)
signal(SIGINT, lambda s, f: loop.stop())
server = loop.run_until_complete(serv_task)
server.after_start()

logger.info("""
       _____             _         _____ _             _     _ 
      / ____|           (_)       / ____| |           | |   | |
     | (___   __ _ _ __  _  ___  | (___ | |_ __ _ _ __| |_  | |
      \___ \ / _` | '_ \| |/ __|  \___ \| __/ _` | '__| __| | |
      ____) | (_| | | | | | (__   ____) | || (_| | |  | |_  |_|
     |_____/ \__,_|_| |_|_|\___| |_____/ \__\__,_|_|   \__| (_)
    """)

try:
    loop.run_forever()
except KeyboardInterrupt as e:
    loop.stop()
finally:
    server.before_stop()

    # Wait for server to close
    close_task = server.close()
    loop.run_until_complete(close_task)

    # Complete all tasks on the loop
    for connection in server.connections:
        connection.close_if_idle()
    server.after_stop()
    logger.info('sanic stop!')
