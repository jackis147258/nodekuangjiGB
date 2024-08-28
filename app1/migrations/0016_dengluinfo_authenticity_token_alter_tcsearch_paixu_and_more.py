# Generated by Django 4.2.3 on 2023-08-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_alter_dengluinfo_cookie_alter_dengluinfo_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dengluinfo',
            name='authenticity_token',
            field=models.CharField(blank=True, db_comment='获得的authenticity_token信息', max_length=250, null=True, verbose_name='authenticity_token'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='paiXu',
            field=models.SmallIntegerField(blank=True, choices=[(4, 'ROI'), (1, '存在时间'), (2, '开始时间'), (3, '利润')], default=1, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='raceTime',
            field=models.CharField(blank=True, choices=[('57600', '16小时'), ('43200', '12小时'), ('172800', '2天'), ('604800', '1周'), ('86400', '1天')], db_comment='raceTime比赛时间', default='86400', max_length=50, null=True, verbose_name='比赛时间'),
        ),
        migrations.AlterField(
            model_name='tcsport',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(1, '体育类'), (2, '电竞类')], db_comment=' 比赛类型', default=1, null=True, verbose_name='比赛类型'),
        ),
    ]