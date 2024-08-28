# Generated by Django 4.2.3 on 2023-10-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0042_t_quantify1_dlbuynumber_t_quantify1_dlbuytoken_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='t_tokenaddr',
            old_name='DlBuyNumber',
            new_name='BuyNumber',
        ),
        migrations.RenameField(
            model_name='t_tokenaddr',
            old_name='DlBuyTOKEN_price',
            new_name='BuyTOKEN_price',
        ),
        migrations.RenameField(
            model_name='t_tokenaddr',
            old_name='DlSellNumber',
            new_name='SellNumber',
        ),
        migrations.RenameField(
            model_name='t_tokenaddr',
            old_name='DlSellTOKEN_price',
            new_name='SellTOKEN_price',
        ),
        migrations.RemoveField(
            model_name='t_quantify1',
            name='DlTOKEN_ADDRESS',
        ),
        migrations.RemoveField(
            model_name='t_quantify1',
            name='DlTOKEN_private',
        ),
        migrations.AlterField(
            model_name='dengluinfo',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(1, '普通post'), (2, 'post')], db_comment=' 普通post', default=1, null=True, verbose_name='普通post'),
        ),
        migrations.AlterField(
            model_name='t_quantify1',
            name='Dlprice_status',
            field=models.IntegerField(choices=[(0, '全局'), (1, '独立')], db_comment='0 全局,1独立', default=0),
        ),
        migrations.AlterField(
            model_name='t_quantify1',
            name='status',
            field=models.IntegerField(choices=[(0, '关闭'), (1, '运行')], db_comment='0 关闭,1运行中', default=0),
        ),
        migrations.AlterField(
            model_name='t_task',
            name='status',
            field=models.IntegerField(choices=[(0, '停止'), (1, '正常')], db_comment='0 停止,正常', default=1),
        ),
        migrations.AlterField(
            model_name='t_tokenaddr',
            name='status',
            field=models.IntegerField(choices=[(0, '停止'), (1, '正常')], db_comment='0 停止,正常', default=1),
        ),
        migrations.AlterField(
            model_name='t_tokenaddrbak',
            name='status',
            field=models.IntegerField(choices=[(0, '停止'), (1, '正常')], db_comment='0 停止,正常', default=1),
        ),
        migrations.AlterField(
            model_name='t_trade',
            name='status',
            field=models.IntegerField(choices=[(0, '停止'), (1, '正常')], db_comment='0 停止,正常', default=1),
        ),
        migrations.AlterField(
            model_name='t_trade',
            name='tradeStatus',
            field=models.IntegerField(choices=[(1, '卖'), (0, '买'), (2, 'Approved')], db_comment='交易状态', default=1, verbose_name='0 停止,正常'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='paiXu',
            field=models.SmallIntegerField(blank=True, choices=[(1, '存在时间'), (4, 'ROI'), (2, '开始时间'), (3, '利润')], default=1, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='raceTime',
            field=models.CharField(blank=True, choices=[('604800', '1周'), ('43200', '12小时'), ('57600', '16小时'), ('172800', '2天'), ('86400', '1天')], db_comment='raceTime比赛时间', default='86400', max_length=50, null=True, verbose_name='比赛时间'),
        ),
        migrations.AlterField(
            model_name='webinfo',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(1, '企业站'), (2, '功能站')], db_comment=' 类型', default=1, null=True, verbose_name='类型'),
        ),
    ]