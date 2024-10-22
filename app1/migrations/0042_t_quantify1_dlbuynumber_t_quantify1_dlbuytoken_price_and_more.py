# Generated by Django 4.2.3 on 2023-10-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0041_remove_t_quantify1_dlbuynumber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_quantify1',
            name='DlBuyNumber',
            field=models.IntegerField(blank=True, db_comment='购买数量', default=0, null=True, verbose_name='限制购买数量'),
        ),
        migrations.AddField(
            model_name='t_quantify1',
            name='DlBuyTOKEN_price',
            field=models.CharField(blank=True, db_comment='购买价格', max_length=255, null=True, verbose_name='限制购买价格'),
        ),
        migrations.AddField(
            model_name='t_quantify1',
            name='DlSellNumber',
            field=models.IntegerField(blank=True, db_comment='出售数量', default=0, null=True, verbose_name='限制出售数量'),
        ),
        migrations.AddField(
            model_name='t_quantify1',
            name='DlSellTOKEN_price',
            field=models.CharField(blank=True, db_comment='出售价格', max_length=255, null=True, verbose_name='限制出售价格'),
        ),
        migrations.AlterField(
            model_name='t_quantify1',
            name='Dlprice_status',
            field=models.IntegerField(choices=[(1, '独立'), (0, '全局')], db_comment='0 全局,1独立', default=0),
        ),
        migrations.AlterField(
            model_name='t_quantify1',
            name='status',
            field=models.IntegerField(choices=[(1, '运行'), (0, '关闭')], db_comment='0 关闭,1运行中', default=0),
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
            field=models.IntegerField(choices=[(0, '买'), (2, 'Approved'), (1, '卖')], db_comment='交易状态', default=1, verbose_name='0 停止,正常'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='gender',
            field=models.SmallIntegerField(blank=True, choices=[(2, '女'), (1, '男')], default=1, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='paiXu',
            field=models.SmallIntegerField(blank=True, choices=[(4, 'ROI'), (1, '存在时间'), (3, '利润'), (2, '开始时间')], default=1, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='raceTime',
            field=models.CharField(blank=True, choices=[('57600', '16小时'), ('172800', '2天'), ('86400', '1天'), ('43200', '12小时'), ('604800', '1周')], db_comment='raceTime比赛时间', default='86400', max_length=50, null=True, verbose_name='比赛时间'),
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
