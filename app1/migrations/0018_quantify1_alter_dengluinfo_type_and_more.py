# Generated by Django 4.2.3 on 2023-09-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_alter_tcsearch_gender_alter_tcsearch_paixu_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quantify1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TRADE_TOKEN_ADDRESS', models.CharField(blank=True, db_comment='代币地址', default=0, max_length=255, null=True, verbose_name='代币地址')),
                ('USDT_TOKEN_ADDRESS', models.CharField(blank=True, db_comment='Usdt地址', default='0x55d398326f99059fF775485246999027B3197955', max_length=255, null=True, verbose_name='Usdt地址')),
                ('WBNB_ADDRESS', models.CharField(blank=True, db_comment='Wbnb地址', default='0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c', max_length=255, null=True, verbose_name='Wbnb地址')),
                ('LP_ymiiUsdt_ADDRESS', models.CharField(blank=True, db_comment='LP地址', default='0x6b6b2D8166D13b58155b8d454F239AE3691257A6', max_length=255, null=True, verbose_name='LP地址')),
                ('Tools_lpPrice_ADDRESS', models.CharField(blank=True, db_comment='获取代币价格合约地址', default='0x02Fa571EdAd13043EE3f3676E65092c5000E3Ad0', max_length=255, null=True, verbose_name='获取代币价格合约地址')),
                ('PANCAKE_ROUTER_ADDRESS', models.CharField(blank=True, db_comment='pancakeRouter地址', default='0x10ED43C718714eb63d5aA57B78B54704E256024E', max_length=255, null=True, verbose_name='pancakeRouter地址')),
                ('Bnb_TokenGas', models.CharField(blank=True, db_comment='投资汇报率最小值', default=0, max_length=255, null=True, verbose_name='发币私钥地址')),
                ('buyNumberTotal', models.IntegerField(blank=True, db_comment='购买总数销量', default=0, null=True, verbose_name='购买总数销量')),
                ('buyPrice', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='购买价格')),
                ('sellPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='销售价格')),
                ('coinsRecharge', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='不足充币')),
                ('AmountBuy0', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='购买区间0')),
                ('AmountBuy1', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='购买区间1')),
                ('AmountSell0', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='销售区间0')),
                ('AmountSell1', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='销售区间1')),
                ('PercentBuy', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='下调 百分比')),
                ('PercenttSell', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='上调 百分比')),
                ('Token_Transaction_Time', models.IntegerField(blank=True, db_comment='交易等待秒数', default=0, null=True, verbose_name='交易等待秒数')),
                ('status', models.IntegerField(db_comment='0 关闭,1运行中', default=1)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('webid', models.IntegerField(blank=True, db_comment='站点id', default=0, null=True)),
                ('cn_memo', models.CharField(blank=True, db_comment='中文备注', max_length=200, null=True)),
            ],
            options={
                'db_table': 'Quantify1',
                'db_table_comment': '量化交易方案1',
            },
        ),
        migrations.AlterField(
            model_name='dengluinfo',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(2, 'post'), (1, '普通post')], db_comment=' 普通post', default=1, null=True, verbose_name='普通post'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='gender',
            field=models.SmallIntegerField(blank=True, choices=[(1, '男'), (2, '女')], default=1, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='paiXu',
            field=models.SmallIntegerField(blank=True, choices=[(2, '开始时间'), (1, '存在时间'), (4, 'ROI'), (3, '利润')], default=1, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='tcsearch',
            name='raceTime',
            field=models.CharField(blank=True, choices=[('43200', '12小时'), ('86400', '1天'), ('604800', '1周'), ('57600', '16小时'), ('172800', '2天')], db_comment='raceTime比赛时间', default='86400', max_length=50, null=True, verbose_name='比赛时间'),
        ),
        migrations.AlterField(
            model_name='tcsport',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(2, '电竞类'), (1, '体育类')], db_comment=' 比赛类型', default=1, null=True, verbose_name='比赛类型'),
        ),
        migrations.AlterField(
            model_name='webinfo',
            name='type',
            field=models.SmallIntegerField(blank=True, choices=[(2, '功能站'), (1, '企业站')], db_comment=' 类型', default=1, null=True, verbose_name='类型'),
        ),
    ]
