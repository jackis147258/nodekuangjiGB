import json
import uuid
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from datetime import datetime, timedelta

class DynamicPeriodicTask:

    def __init__(self):
        pass

    @staticmethod
    def create_task(seconds, task_path, args, start_time=None, end_time=None, duration=None):
    # def create_task(seconds, task_path, args):
        # 创建或获取调度
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=seconds,
            period=IntervalSchedule.SECONDS,
        )

        # 生成唯一的任务名
        unique_name = f"Task_{uuid.uuid4()}"
        
           
         # 如果没有提供开始时间, 默认为当前时间
        if start_time is None:
            start_time = datetime.now()

        # 如果没有提供结束时间但提供了时长, 计算结束时间
        if end_time is None and duration is not None:
            end_time = start_time + timedelta(seconds=duration)
          # 创建任务
        PeriodicTask.objects.create(
            interval=schedule,
            name=unique_name,
            task=task_path,
            args=json.dumps(args),
            start_time=start_time,   # 设置开始时间
            # expire_time=end_time     # 设置结束时间
            )


        return unique_name  # 返回任务名，以便以后可以查询、修改或删除任务

    @staticmethod
    def modify_task(task_name, new_args):
        # 查询并修改任务
        try:
            task = PeriodicTask.objects.get(name=task_name)
            task.args = json.dumps(new_args)
            task.save()
            return True
        except PeriodicTask.DoesNotExist:
            return False

    @staticmethod
    def delete_task(task_name):
        # 查询并删除任务
        try:
            task = PeriodicTask.objects.get(name=task_name)
            task.delete()
            return True
        except PeriodicTask.DoesNotExist:
            return False
