# Generated by Django 4.2.3 on 2024-01-02 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0002_alter_customuser_managers_customuser_ebccreated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ebcjiasushouyijilu',
            name='EbcCreated_at',
        ),
        migrations.RemoveField(
            model_name='ebcjiasushouyijilu',
            name='taskId',
        ),
        migrations.AddField(
            model_name='customuser',
            name='EbcLastFanHuan_at',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='上一次返还时间'),
        ),
        migrations.AddField(
            model_name='ebczhiya',
            name='EbcCreated_at',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='ebczhiya',
            name='EbcLastFanHuan_at',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='上一次返还时间'),
        ),
    ]