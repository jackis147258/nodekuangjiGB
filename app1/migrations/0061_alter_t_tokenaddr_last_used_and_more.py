# Generated by Django 4.2.3 on 2024-06-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0060_webinfo_jiangjinchi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_tokenaddr',
            name='last_used',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='t_tokenaddrbak',
            name='last_used',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
