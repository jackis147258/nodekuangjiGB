# Generated by Django 4.2.3 on 2023-08-14 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_tcsport_type_alter_tcsearch_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tcsearch',
            name='gender',
            field=models.SmallIntegerField(blank=True, choices=[(1, '男'), (2, '女')], default=1, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='paiXu',
            field=models.SmallIntegerField(blank=True, choices=[(1, '存在时间'), (4, 'ROI'), (3, '利润'), (2, '开始时间')], default=1, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='raceTime',
            field=models.CharField(blank=True, choices=[('86400', '2天'), ('86400', '12小时'), ('186400', '4周2天'), ('86400', '1天'), ('86400', '1周'), ('48000', '16小时')], db_comment='raceTime比赛时间', default='86400', max_length=50, null=True, verbose_name='比赛时间'),
        ),
    ]