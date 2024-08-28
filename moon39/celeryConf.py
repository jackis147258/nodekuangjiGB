#  django项目名/django项目名/celeryConf.py

# # 任务存储
# broker_url = r"redis://127.0.0.1:6379/0"
# # 结果存储
# result_backend = r"redis://127.0.0.1:6379/1"

# CELERY_RESULT_BACKEND = 'django-db'
from kombu import Queue

CELERY_QUEUES = (
    Queue('default', routing_key='task.#'),
    Queue('priority_high', routing_key='high.#'),
)

CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'tasks'
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_DEFAULT_ROUTING_KEY = 'task.default'


# 使用rebbitmq来做消息中间件
# 默认是使用guest账号来登录的
# broker_url = 'amqp://guest:guest@localhost:5672//'
# broker_url = 'amqp://admin:admin@192.168.10.1:5672//'
# result_serializer = 'json'
# 时区
timezone = 'Asia/Shanghai'
# 过期时间
# event_queue_ttl = 5
# celery不回复结果
task_ignore_result = True

# 为防止内存泄漏，一个进程执行过N次之后杀死，建议是100次，我没听
worker_max_tasks_per_child = 10
# 错误 DatabaseWrapper objects created in a thread can only be used in that same thread
CELERY_TASK_ALWAYS_EAGER = True
