# Generated by Django 4.2.3 on 2023-09-28 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0028_alter_dengluinfo_type_alter_t_task_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dengluinfo',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(1, '普通post'), (2, 'post')], db_comment=' 普通post', default=1, null=True, verbose_name='普通post'),
        ),
        migrations.AlterField(
            model_name='t_task',
            name='status',
            field=models.IntegerField(choices=[(1, '正常'), (0, '停止')], db_comment='0 停止,正常', default=1),
        ),
        migrations.AlterField(
            model_name='t_tokenaddr',
            name='status',
            field=models.IntegerField(choices=[(1, '正常'), (0, '停止')], db_comment='0 停止,正常', default=1),
        ),
        migrations.AlterField(
            model_name='t_tokenaddr',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='t_trade',
            name='status',
            field=models.IntegerField(choices=[(1, '正常'), (0, '停止')], db_comment='0 停止,正常', default=1),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='gender',
            field=models.SmallIntegerField(blank=True, choices=[(2, '女'), (1, '男')], default=1, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='paiXu',
            field=models.SmallIntegerField(blank=True, choices=[(1, '存在时间'), (4, 'ROI'), (2, '开始时间'), (3, '利润')], default=1, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='raceTime',
            field=models.CharField(blank=True, choices=[('57600', '16小时'), ('172800', '2天'), ('86400', '1天'), ('604800', '1周'), ('43200', '12小时')], db_comment='raceTime比赛时间', default='86400', max_length=50, null=True, verbose_name='比赛时间'),
        ),
        migrations.AlterField(
            model_name='webinfo',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(1, '企业站'), (2, '功能站')], db_comment=' 类型', default=1, null=True, verbose_name='类型'),
        ),
    ]