# Generated by Django 4.2.3 on 2024-06-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0027_alter_ebcjiasushouyijilu_layer_alter_paytoken_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokenzhiyajishi',
            name='amountShouYi',
            field=models.FloatField(blank=True, db_comment='质押收益', null=True, verbose_name='质押收益'),
        ),
    ]
