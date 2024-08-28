# Generated by Django 4.2.3 on 2023-08-06 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_rename_menonetwo_tcsearch_menonetwos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tcsearch',
            name='paiXu',
            field=models.SmallIntegerField(blank=True, choices=[(2, '开始时间'), (4, 'ROI'), (3, '利润'), (1, '存在时间')], default=1, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='raceTime',
            field=models.SmallIntegerField(blank=True, choices=[(2, '开始时间'), (4, 'ROI'), (3, '利润'), (1, '存在时间')], db_comment='raceTime比赛时间', default=1, null=True, verbose_name='比赛时间'),
        ),
    ]