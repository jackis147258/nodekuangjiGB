# Generated by Django 4.2.3 on 2023-10-20 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0039_t_quantify1_dlbuynumber_t_quantify1_dlbuytoken_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_tokenaddr',
            name='DlBuyNumber',
            field=models.IntegerField(blank=True, db_comment='购买数量', default=0, null=True, verbose_name='购买数量'),
        ),
        migrations.AddField(
            model_name='t_tokenaddr',
            name='DlBuyTOKEN_price',
            field=models.CharField(blank=True, db_comment='购买价格', max_length=255, null=True, verbose_name='购买价格'),
        ),
        migrations.AddField(
            model_name='t_tokenaddr',
            name='DlSellNumber',
            field=models.IntegerField(blank=True, db_comment='出售数量', default=0, null=True, verbose_name='出售数量'),
        ),
        migrations.AddField(
            model_name='t_tokenaddr',
            name='DlSellTOKEN_price',
            field=models.CharField(blank=True, db_comment='出售价格', max_length=255, null=True, verbose_name='出售价格'),
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
            model_name='tcsearch',
            name='gender',
            field=models.SmallIntegerField(blank=True, choices=[(2, '女'), (1, '男')], default=1, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='paiXu',
            field=models.SmallIntegerField(blank=True, choices=[(1, '存在时间'), (2, '开始时间'), (4, 'ROI'), (3, '利润')], default=1, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='raceTime',
            field=models.CharField(blank=True, choices=[('86400', '1天'), ('43200', '12小时'), ('604800', '1周'), ('57600', '16小时'), ('172800', '2天')], db_comment='raceTime比赛时间', default='86400', max_length=50, null=True, verbose_name='比赛时间'),
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