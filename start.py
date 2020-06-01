# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren blueprint_api
All rights reserved
create time '2019/9/16 10:21'

Module usage:

"""

from app import create_app
from app.core import logger

app = create_app()
workers = app.config.get('WORKERS')
app.debug = app.config.get('DEBUG')

if __name__ == '__main__':
    logger.info("""
       _____             _         _____ _             _     _ 
      / ____|           (_)       / ____| |           | |   | |
     | (___   __ _ _ __  _  ___  | (___ | |_ __ _ _ __| |_  | |
      \___ \ / _` | '_ \| |/ __|  \___ \| __/ _` | '__| __| | |
      ____) | (_| | | | | | (__   ____) | || (_| | |  | |_  |_|
     |_____/ \__,_|_| |_|_|\___| |_____/ \__\__,_|_|   \__| (_)
    """)
    app.run(host="0.0.0.0", port=5000, workers=workers, auto_reload=False)
