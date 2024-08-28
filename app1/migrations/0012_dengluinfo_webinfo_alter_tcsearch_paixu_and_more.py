# Generated by Django 4.2.3 on 2023-08-15 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_tcsearch_gender_alter_tcsearch_paixu_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='dengLuInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(blank=True, db_comment='用户ID', null=True)),
                ('name', models.CharField(blank=True, db_comment='名称', max_length=50, null=True, verbose_name='登录名')),
                ('passWord', models.CharField(blank=True, db_comment='名称', max_length=50, null=True, verbose_name='密码')),
                ('remember_me', models.CharField(blank=True, db_comment='remember_me', max_length=50, null=True)),
                ('commit', models.CharField(blank=True, db_comment='commit', max_length=50, null=True)),
                ('utf8', models.CharField(blank=True, db_comment='utf8', max_length=50, null=True)),
                ('post1', models.CharField(blank=True, db_comment='名称', max_length=50, null=True)),
                ('post2', models.CharField(blank=True, db_comment='名称', max_length=50, null=True)),
                ('post3', models.CharField(blank=True, db_comment='名称', max_length=50, null=True)),
                ('token', models.CharField(blank=True, db_comment='获得的token信息', max_length=50, null=True, verbose_name='token')),
                ('status', models.IntegerField(db_comment='0 未开,1开', default=1)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('webid', models.IntegerField(blank=True, db_comment='站点id', default=0, null=True)),
                ('cn_memo', models.CharField(blank=True, db_comment='中文备注', max_length=200, null=True)),
                ('type', models.SmallIntegerField(blank=True, choices=[(1, '普通post'), (2, 'post')], db_comment=' 普通post', default=1, null=True, verbose_name='普通post')),
            ],
            options={
                'db_table': 'dengLuInfo',
                'db_table_comment': '登录信息设置',
            },
        ),
        migrations.CreateModel(
            name='webInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(blank=True, db_comment='用户ID', null=True)),
                ('name', models.CharField(blank=True, db_comment='名称', max_length=50, null=True, verbose_name='登录名')),
                ('webName', models.CharField(blank=True, db_comment='webName', max_length=50, null=True, verbose_name='网站名称')),
                ('domain', models.CharField(blank=True, db_comment='domain ', max_length=50, null=True, verbose_name='域名')),
                ('status', models.IntegerField(db_comment='0 未开,1开', default=1)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('webid', models.IntegerField(blank=True, db_comment='站点id', default=0, null=True)),
                ('cn_memo', models.CharField(blank=True, db_comment='中文备注', max_length=200, null=True)),
                ('type', models.SmallIntegerField(blank=True, choices=[(2, '功能站'), (1, '企业站')], db_comment=' 类型', default=1, null=True, verbose_name='类型')),
            ],
            options={
                'db_table': 'webInfo',
                'db_table_comment': '站点信息设置',
            },
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='paiXu',
            field=models.SmallIntegerField(blank=True, choices=[(2, '开始时间'), (4, 'ROI'), (3, '利润'), (1, '存在时间')], default=1, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='raceTime',
            field=models.CharField(blank=True, choices=[('48000', '16小时'), ('86400', '12小时'), ('86400', '2天'), ('86400', '1天'), ('186400', '4周2天'), ('86400', '1周')], db_comment='raceTime比赛时间', default='86400', max_length=50, null=True, verbose_name='比赛时间'),
        ),
        migrations.AlterField(
            model_name='tcsport',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(1, '体育类'), (2, '电竞类')], db_comment=' 比赛类型', default=1, null=True, verbose_name='比赛类型'),
        ),
    ]