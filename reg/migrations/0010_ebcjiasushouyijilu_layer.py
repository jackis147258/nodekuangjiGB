# Generated by Django 4.2.3 on 2024-01-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0009_alter_customuser_fanhuan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebcjiasushouyijilu',
            name='Layer',
            field=models.IntegerField(blank=True, db_comment='0充值1代数范润2层级范润', default=0, null=True, verbose_name='类型'),
        ),
    ]
