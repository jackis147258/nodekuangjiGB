# Generated by Django 4.2.3 on 2023-10-28 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0044_t_quantify1_duration_t_quantify1_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_quantify1',
            name='duration',
            field=models.DurationField(blank=True, help_text='结束时间 和 运行秒数 选一个.', null=True, verbose_name='运行秒数'),
        ),
        migrations.AlterField(
            model_name='t_quantify1',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='t_quantify1',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='t_trade',
            name='tradeStatus',
            field=models.IntegerField(choices=[(0, '买'), (1, '卖'), (2, 'Approved')], db_comment='交易状态', default=1, verbose_name='0 停止,正常'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='gender',
            field=models.SmallIntegerField(blank=True, choices=[(2, '女'), (1, '男')], default=1, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='paiXu',
            field=models.SmallIntegerField(blank=True, choices=[(3, '利润'), (1, '存在时间'), (2, '开始时间'), (4, 'ROI')], default=1, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='raceTime',
            field=models.CharField(blank=True, choices=[('43200', '12小时'), ('86400', '1天'), ('604800', '1周'), ('172800', '2天'), ('57600', '16小时')], db_comment='raceTime比赛时间', default='86400', max_length=50, null=True, verbose_name='比赛时间'),
        ),
        migrations.AlterField(
            model_name='tcsport',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(1, '体育类'), (2, '电竞类')], db_comment=' 比赛类型', default=1, null=True, verbose_name='比赛类型'),
        ),
        migrations.AlterField(
            model_name='webinfo',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(2, '功能站'), (1, '企业站')], db_comment=' 类型', default=1, null=True, verbose_name='类型'),
        ),
    ]