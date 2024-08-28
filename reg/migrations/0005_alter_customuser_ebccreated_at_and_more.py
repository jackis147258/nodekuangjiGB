# Generated by Django 4.2.3 on 2024-01-02 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0004_remove_customuser_buyprice_alter_customuser_fanhuan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='EbcCreated_at',
            field=models.BigIntegerField(blank=True, default=0, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='EbcLastFanHuan_at',
            field=models.BigIntegerField(blank=True, default=0, null=True, verbose_name='上一次返还时间'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='fanHuan',
            field=models.DecimalField(blank=True, db_comment='可以返还用户B数量', decimal_places=4, default=0, max_digits=30, null=True, verbose_name='可以返还用户B数量'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='userStakesA',
            field=models.BigIntegerField(blank=True, db_comment='用户质押A数量', default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='userStakesB',
            field=models.BigIntegerField(blank=True, db_comment='用户质押B数量', default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='userStakesBfanHuan',
            field=models.DecimalField(blank=True, db_comment='返还用户B数量', decimal_places=4, default=0, max_digits=30, null=True, verbose_name='返还用户B数量'),
        ),
    ]
