# Generated by Django 4.2.3 on 2023-10-05 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0033_t_tokenaddr_last_used_t_tokenaddrbak_last_used_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_quantify1',
            name='Token_Price_Time',
            field=models.IntegerField(blank=True, db_comment='读取价格等待秒数', default=10, null=True, verbose_name='读取价格等待秒数'),
        ),
        migrations.AlterField(
            model_name='t_quantify1',
            name='Token_Transaction_Time',
            field=models.IntegerField(blank=True, db_comment='交易等待秒数', default=20, null=True, verbose_name='交易等待秒数'),
        ),
        migrations.AlterField(
            model_name='t_quantify1',
            name='status',
            field=models.IntegerField(choices=[(0, '关闭'), (1, '运行')], db_comment='0 关闭,1运行中', default=0),
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
            model_name='t_tokenaddrbak',
            name='status',
            field=models.IntegerField(choices=[(1, '正常'), (0, '停止')], db_comment='0 停止,正常', default=1),
        ),
        migrations.AlterField(
            model_name='t_trade',
            name='status',
            field=models.IntegerField(choices=[(1, '正常'), (0, '停止')], db_comment='0 停止,正常', default=1),
        ),
        migrations.AlterField(
            model_name='t_trade',
            name='tradeStatus',
            field=models.IntegerField(choices=[(0, '买'), (1, '卖')], db_comment='交易状态', default=1, verbose_name='0 停止,正常'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='gender',
            field=models.SmallIntegerField(blank=True, choices=[(1, '男'), (2, '女')], default=1, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='paiXu',
            field=models.SmallIntegerField(blank=True, choices=[(1, '存在时间'), (3, '利润'), (2, '开始时间'), (4, 'ROI')], default=1, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='raceTime',
            field=models.CharField(blank=True, choices=[('604800', '1周'), ('86400', '1天'), ('172800', '2天'), ('57600', '16小时'), ('43200', '12小时')], db_comment='raceTime比赛时间', default='86400', max_length=50, null=True, verbose_name='比赛时间'),
        ),
        migrations.AlterField(
            model_name='tcsport',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(2, '电竞类'), (1, '体育类')], db_comment=' 比赛类型', default=1, null=True, verbose_name='比赛类型'),
        ),
        migrations.AlterField(
            model_name='webinfo',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(2, '功能站'), (1, '企业站')], db_comment=' 类型', default=1, null=True, verbose_name='类型'),
        ),
    ]