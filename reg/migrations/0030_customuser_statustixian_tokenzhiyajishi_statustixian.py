# Generated by Django 4.2.3 on 2024-07-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0029_ebcjiasushouyijilu_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='statusTiXian',
            field=models.IntegerField(choices=[(0, '正常提现'), (1, '不可提现')], db_comment='0 正常提现,不可提现', default=0),
        ),
        migrations.AddField(
            model_name='tokenzhiyajishi',
            name='statusTiXian',
            field=models.IntegerField(choices=[(0, '正常提现'), (1, '不可提现')], db_comment='0 正常提现,不可提现', default=0),
        ),
    ]
