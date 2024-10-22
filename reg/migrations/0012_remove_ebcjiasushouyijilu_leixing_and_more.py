# Generated by Django 4.2.3 on 2024-01-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0011_remove_ebcjiasushouyijilu_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ebcjiasushouyijilu',
            name='leiXing',
        ),
        migrations.AddField(
            model_name='ebcjiasushouyijilu',
            name='liuShuiId',
            field=models.IntegerField(blank=True, db_comment='流水ID 合约同步', default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ebcjiasushouyijilu',
            name='Layer',
            field=models.IntegerField(blank=True, db_comment='0充值1代数范润2层级范润3平台日返1.5%', default=0, null=True, verbose_name='类型'),
        ),
    ]
