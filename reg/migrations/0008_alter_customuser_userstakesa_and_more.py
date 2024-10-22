# Generated by Django 4.2.3 on 2024-01-07 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0007_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='userStakesA',
            field=models.DecimalField(blank=True, db_comment='用户质押A数量', decimal_places=4, default=0, max_digits=30, null=True, verbose_name='用户质押A数量'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='userStakesB',
            field=models.DecimalField(blank=True, db_comment='用户质押B数量', decimal_places=4, default=0, max_digits=30, null=True, verbose_name='用户质押B数量'),
        ),
        migrations.AlterField(
            model_name='ebcjiasushouyijilu',
            name='uidA',
            field=models.DecimalField(blank=True, db_comment='用户A-发送方', decimal_places=4, default=0, max_digits=30, null=True, verbose_name='用户A-发送方'),
        ),
        migrations.AlterField(
            model_name='ebcjiasushouyijilu',
            name='uidB',
            field=models.DecimalField(blank=True, db_comment='用户B-接收方', decimal_places=4, default=0, max_digits=30, null=True, verbose_name='用户B-接收方'),
        ),
    ]
