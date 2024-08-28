# Generated by Django 4.2.3 on 2024-01-02 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0005_alter_customuser_ebccreated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebcjiasushouyijilu',
            name='fanHuan',
            field=models.DecimalField(blank=True, db_comment='每次返还额度', decimal_places=4, default=0, max_digits=30, null=True, verbose_name='每次返还额度'),
        ),
        migrations.AddField(
            model_name='ebcjiasushouyijilu',
            name='leiXing',
            field=models.IntegerField(choices=[(0, '未生效'), (1, '已生效')], db_comment='0,返加速额度', default=0),
        ),
    ]
