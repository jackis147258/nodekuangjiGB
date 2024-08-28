# /django项目名/django项目名/init.py

# 使用celery的设置
from __future__ import absolute_import, unicode_literals

# 使用pymysql必须的设置
# import pymysql

# pymysql.version_info = (1, 4, 0, "final", 0)
# pymysql.install_as_MySQLdb()

# 自动导入Django的app下面的tasks文件内的函数
__all__ = ['celery_app']
