# Generated by Django 4.2.3 on 2023-08-14 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_tcsearch_menonetwos_alter_tcsearch_paixu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tcsport',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(2, '电竞类'), (1, '体育类')], db_comment=' 比赛类型', default=1, null=True, verbose_name='比赛类型'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='gender',
            field=models.SmallIntegerField(blank=True, choices=[(2, '女'), (1, '男')], default=1, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='paiXu',
            field=models.SmallIntegerField(blank=True, choices=[(3, '利润'), (2, '开始时间'), (1, '存在时间'), (4, 'ROI')], default=1, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='raceTime',
            field=models.SmallIntegerField(blank=True, choices=[(186400, '4周2天'), (86400, '2天'), (48000, '16小时'), (86400, '12小时'), (86400, '1天'), (86400, '1周')], db_comment='raceTime比赛时间', default=1, null=True, verbose_name='比赛时间'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='returnOnInvestmentBig',
            field=models.CharField(blank=True, db_comment='投资汇报率最大值', max_length=255, null=True, verbose_name='投资汇报最大'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='returnOnInvestmentLittle',
            field=models.CharField(blank=True, db_comment='投资汇报率最小值', default=0, max_length=255, null=True, verbose_name='投资汇报最小'),
        ),
    ]
