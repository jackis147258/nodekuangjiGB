from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext as _
# from django.contrib.auth.models import User, Group
import django.utils.timezone as timezone


from django.contrib.auth import get_user_model

User = get_user_model()

CATEGORY_CHOICES = (
    (1, _('Handbooks and manuals by discipline')),
    (2, _('Business books')),
    (3, _('Books of literary criticism')),
    (4, _('Books about literary theory')),
    (5, _('Books about literature')),
)

# Create your models here.

class TcOneTwo(models.Model):
    uid = models.IntegerField(db_comment='用户ID',blank=True, null=True,)
    noStr = models.CharField(max_length=255,blank=True, null=True, db_comment='TcOneTwo编号str')
    noInt = models.IntegerField(blank=True, null=True,db_comment='TcOneTwo编号int')
    name = models.CharField(max_length=50, db_comment='名称')
    status = models.IntegerField(db_comment='0 为开,1开',default=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    webid = models.IntegerField(blank=True, null=True,default=0,db_comment='站点id')   
    cn_memo = models.CharField(max_length=200,blank=True, null=True,db_comment='中文备注')
    def __str__(self):
        return self.name
    class Meta:      
        db_table = 'TcOneTwo'
        db_table_comment = 'TcOneTwo各种站点信息'
        verbose_name='TcOneTwo两门三门'
        verbose_name_plural='两门三门plural'

class TcWeb(models.Model):
    uid = models.IntegerField(db_comment='用户ID',blank=True, null=True,)
    noStr = models.CharField(max_length=255,blank=True, null=True, db_comment='tcWeb编号str')
    noInt = models.IntegerField(blank=True, null=True,db_comment='tcWeb编号int')
    name = models.CharField(max_length=50, db_comment='名称')
    status = models.IntegerField(db_comment='0 为开,1开',default=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    webid = models.IntegerField(blank=True, null=True,default=0,db_comment='站点id')   
    cn_memo = models.CharField(max_length=200,blank=True, null=True,db_comment='中文备注')
               
    def __str__(self):
        return self.name
    class Meta:      
        db_table = 'TcWeb'
        db_table_comment = 'tcWeb各种站点信息'
        verbose_name='tc网站'
        verbose_name_plural='tc网站plural'

class TcSport(models.Model):
    uid = models.IntegerField(db_comment='用户ID',blank=True, null=True,)
    noStr = models.CharField(max_length=255,blank=True, null=True, db_comment='TcSports编号str')
    noInt = models.IntegerField(blank=True, null=True,db_comment='TcSports编号int')
    name = models.CharField(max_length=50, db_comment='名称')
    status = models.IntegerField(db_comment='0 未开,1开',default=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    webid = models.IntegerField(blank=True, null=True,default=0,db_comment='站点id')   
    cn_memo = models.CharField(max_length=200,blank=True, null=True,db_comment='中文备注')
    
    type_choices=[
        (1,"体育类"),
        (2,"电竞类"),
    ]
    type=models.SmallIntegerField(verbose_name="比赛类型",choices=type_choices,blank=True, null=True,default=1,db_comment=' 比赛类型')


    def __str__(self):
        return self.name
    
    class Meta:      
        db_table = 'TcSports'
        db_table_comment = 'TcSports各种运动信息'

class TcSearch(models.Model):
    uid = models.IntegerField(blank=True, null=True,db_comment='用户ID')
    paiXu_choices=[
        (1,"存在时间"),
        (2,"开始时间"),
        (3,"利润"),
        (4,"ROI"),
    ]
    # paiXu = models.CharField(max_length=255,blank=True, null=True, db_comment='tcWeb编号str')
    paiXu=models.SmallIntegerField(verbose_name="排序",choices=paiXu_choices,blank=True, null=True,default=1)

    # menOneTwo = models.CharField(max_length=255,blank=True, null=True, db_comment='tcWeb编号str')
    profitRangeLittle = models.CharField(verbose_name="利润最小",max_length=255,blank=True, null=True, db_comment='利润范围最小值',default=0)
    profitRangeBig = models.CharField(verbose_name="利润最大",max_length=255,blank=True, null=True, db_comment='利润范围最大值',default=0)

    returnOnInvestmentLittle = models.CharField(verbose_name="投资汇报最小",max_length=255,blank=True, null=True, db_comment='投资汇报率最小值',default=0)
    returnOnInvestmentBig = models.CharField(verbose_name="投资汇报最大",max_length=255,blank=True, null=True, db_comment='投资汇报率最大值')

    raceTime_choices=[
      
        ("43200","12小时"),
        ("57600","16小时"),
        ("86400","1天"),
        ("172800","2天"),
        ("604800","1周"),
        # ("1382400","2周2天"),
        ]
    raceTime=models.CharField(verbose_name="比赛时间",max_length=50,choices=raceTime_choices,blank=True, null=True,default="86400",db_comment='raceTime比赛时间')
    # raceTime=models.SmallIntegerField(verbose_name="比赛时间",choices=raceTime_choices,blank=True, null=True,default=1,db_comment='raceTime比赛时间')
    # raceTime = models.SmallIntegerField(blank=True, null=True,db_comment='raceTime比赛时间',default=0)

    # tcWebs = models.CharField(max_length=50,blank=True, null=True,  db_comment='tcwebs选择')
    # tcSports = models.CharField(max_length=50,blank=True, null=True, db_comment='tcSports选择')
    moreSearch = models.CharField(max_length=50,blank=True, null=True, db_comment='高级选项-多选内容')

    status = models.IntegerField(db_comment='0 未开,1开',default=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    webid = models.IntegerField(blank=True, null=True,default=0,db_comment='站点id')   
    cn_memo = models.CharField(max_length=200,blank=True, null=True,db_comment='中文备注')

    
    gender_choices=[
        (1,"男"),
        (2,"女"),
    ]
    gender=models.SmallIntegerField(verbose_name="性别",choices=gender_choices,blank=True, null=True,default=1)

    tcWebs = models.ManyToManyField(TcWeb)
    tcSports = models.ManyToManyField(TcSport)
    menOneTwos = models.ManyToManyField(TcOneTwo,verbose_name="两门",)



    # categories = MultiSelectField(choices=CATEGORY_CHOICES,
                                
    #                               # default='1,5')
    #                               default=1)
    class Meta:      
        db_table = 'TcSearch'
        db_table_comment = 'TcSearch个人搜索条件'


class dengLuInfo(models.Model):
    uid = models.IntegerField(db_comment='用户ID',blank=True, null=True,)
    
    name = models.CharField(verbose_name="登录名",max_length=50,blank=True, null=True, db_comment='名称')
    passWord = models.CharField(verbose_name="密码",max_length=50, blank=True, null=True,db_comment='名称')
    remember_me = models.CharField(max_length=50,blank=True, null=True, db_comment='remember_me')
    commit = models.CharField(max_length=50, blank=True, null=True,db_comment='commit')
    utf8 = models.CharField(max_length=50, blank=True, null=True,db_comment='utf8')
    post1 = models.CharField(max_length=50, blank=True, null=True,db_comment='名称')
    post2 = models.CharField(max_length=50, blank=True, null=True,db_comment='名称')
    post3 = models.CharField(max_length=50, blank=True, null=True,db_comment='名称')
    
    token = models.CharField(verbose_name="token",max_length=200,blank=True, null=True, db_comment='获得的token信息')
    cookie = models.TextField(verbose_name="cookie",blank=True, null=True, db_comment='获得的cookie信息')

    
    status = models.IntegerField(db_comment='0 未开,1开',default=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    webid = models.IntegerField(blank=True, null=True,default=0,db_comment='站点id')   
    cn_memo = models.CharField(max_length=200,blank=True, null=True,db_comment='中文备注')
    authenticity_token = models.CharField(verbose_name="authenticity_token",max_length=250,blank=True, null=True, db_comment='获得的authenticity_token信息')
    
    
    type_choices=[      
        (1,"普通post"),
        (2,"post"),
    ]
    type=models.SmallIntegerField(verbose_name="普通post",choices=type_choices,blank=True, null=True,default=1,db_comment=' 普通post')

    def __str__(self):
        return self.name    
    class Meta:      
        db_table = 'dengLuInfo'
        db_table_comment = '登录信息设置'

class webInfo(models.Model):
    uid = models.IntegerField(db_comment='用户ID',blank=True, null=True,)    
    name = models.CharField(verbose_name="登录名",max_length=50,blank=True, null=True, db_comment='名称')    
    webName = models.CharField(verbose_name="网站名称",max_length=50,blank=True, null=True, db_comment='webName')    
    domain  = models.CharField(verbose_name="域名",max_length=50,blank=True, null=True, db_comment='domain ')
    status = models.IntegerField(db_comment='0 未开,1开',default=1)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    webid = models.IntegerField(blank=True, null=True,default=0,db_comment='站点id')   
    cn_memo = models.CharField(max_length=200,blank=True, null=True,db_comment='中文备注')    
    type_choices=[      
        (1,"企业站"),
        (2,"功能站"),
    ]
    type=models.SmallIntegerField(verbose_name="类型",choices=type_choices,blank=True, null=True,default=1,db_comment=' 类型')
    
    number1 = models.IntegerField(db_comment='number1',blank=True, null=True,default=1)
    number2 = models.IntegerField(db_comment='number1',blank=True, null=True,default=1)
    number3 = models.IntegerField(db_comment='number1',blank=True, null=True,default=1)
    number4 = models.IntegerField(db_comment='number1',blank=True, null=True,default=1)
    number5 = models.IntegerField(db_comment='number1',blank=True, null=True,default=1)
    number6 = models.IntegerField(db_comment='number1',blank=True, null=True,default=1)
    number7 = models.IntegerField(db_comment='number1',blank=True, null=True,default=1)
    number8 = models.IntegerField(db_comment='number1',blank=True, null=True,default=1)
    number9 = models.IntegerField(db_comment='number1',blank=True, null=True,default=1)
    number10 = models.IntegerField(db_comment='number1',blank=True, null=True,default=1)
    number11 = models.IntegerField(db_comment='number1',blank=True, null=True,default=1)
    
    Str1 = models.CharField(max_length=255,blank=True, null=True, db_comment='str')
    Str2 = models.CharField(max_length=255,blank=True, null=True, db_comment='str')
    Str3 = models.CharField(max_length=255,blank=True, null=True, db_comment='str')
    Str4 = models.CharField(max_length=255,blank=True, null=True, db_comment='str')
    Str5 = models.CharField(max_length=255,blank=True, null=True, db_comment='str')
    Str6 = models.CharField(max_length=255,blank=True, null=True, db_comment='str')
    Str7 = models.CharField(max_length=255,blank=True, null=True, db_comment='str')
    Str8 = models.CharField(max_length=255,blank=True, null=True, db_comment='str')
    Str9 = models.CharField(max_length=255,blank=True, null=True, db_comment='str')
    Str10 = models.CharField(max_length=255,blank=True, null=True, db_comment='str')

    # 站点 奖金池
    jiangJinChi= models.FloatField(db_comment='奖金池',verbose_name="奖金池", blank=True, null=True,default=0)




    def __str__(self):
        return self.name
    
    class Meta:      
        db_table = 'webInfo'
        db_table_comment = '站点信息设置'


class T_Quantify1(models.Model): 
# 设置 地址 
    # menOneTwo = models.CharField(max_length=255,blank=True, null=True, db_comment='tcWeb编号str')
    TRADE_TOKEN_ADDRESS = models.CharField(verbose_name="代币地址",max_length=255,blank=True, null=True, db_comment='代币地址',default='0x768a62a22b187EB350637e720ebC552D905c0331')
    USDT_TOKEN_ADDRESS = models.CharField(verbose_name="Usdt地址",max_length=255,blank=True, null=True, db_comment='Usdt地址',default='0x55d398326f99059fF775485246999027B3197955')
    WBNB_ADDRESS = models.CharField(verbose_name="Wbnb地址",max_length=255,blank=True, null=True, db_comment='Wbnb地址',default='0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c')
    LP_ymiiUsdt_ADDRESS = models.CharField(verbose_name="LP地址",max_length=255,blank=True, null=True, db_comment='LP地址',default='0x6b6b2D8166D13b58155b8d454F239AE3691257A6')
    Tools_lpPrice_ADDRESS = models.CharField(verbose_name="获取代币价格合约地址",max_length=255,blank=True, null=True, db_comment='获取代币价格合约地址',default='0x02Fa571EdAd13043EE3f3676E65092c5000E3Ad0')
    PANCAKE_ROUTER_ADDRESS = models.CharField(verbose_name="pancakeRouter地址",max_length=255,blank=True, null=True, db_comment='pancakeRouter地址',default='0x10ED43C718714eb63d5aA57B78B54704E256024E')
    Bnb_TokenGas = models.CharField(verbose_name="发币私钥地址",max_length=255,blank=True, null=True, db_comment='投资汇报率最小值',default=0)
    
    
    buyNumberTotal = models.IntegerField(verbose_name="购买总数销量",blank=True, null=True,default=0,db_comment='购买总数销量') 
    
    
    buyPrice = models.DecimalField(verbose_name="购买价格",max_digits=10, decimal_places=4, blank=True, null=True)
    sellPrice = models.DecimalField(verbose_name="出售价格-选择独立Token后不起作用",max_digits=10, decimal_places=4, blank=True, null=True)
    coinsRecharge = models.DecimalField(verbose_name="不足充币",max_digits=10, decimal_places=4, blank=True, null=True)

    AmountBuy0 = models.DecimalField(verbose_name="购买区间0",max_digits=10, decimal_places=4, blank=True, null=True)
    AmountBuy1 = models.DecimalField(verbose_name="购买区间1",max_digits=10, decimal_places=4, blank=True, null=True)
    
    AmountSell0 = models.DecimalField(verbose_name="销售区间0",max_digits=10, decimal_places=4, blank=True, null=True)
    AmountSell1 = models.DecimalField(verbose_name="销售区间1",max_digits=10, decimal_places=4, blank=True, null=True)

    PercentBuy = models.DecimalField(verbose_name="下调 百分比",max_digits=10, decimal_places=4, blank=True, null=True)
    PercenttSell = models.DecimalField(verbose_name="上调 百分比",max_digits=10, decimal_places=4, blank=True, null=True)
    Token_Transaction_Time = models.IntegerField(verbose_name="交易等待秒数",blank=True, null=True,default=20,db_comment='交易等待秒数') 
    Token_Price_Time = models.IntegerField(verbose_name="读取价格等待秒数",blank=True, null=True,default=10,db_comment='读取价格等待秒数') 
    start_time = models.DateTimeField(verbose_name="开始时间",null=True, blank=True)
    end_time = models.DateTimeField(verbose_name="结束时间",null=True, blank=True)
    duration = models.DurationField(verbose_name="运行秒数",null=True, blank=True, help_text="结束时间 和 运行秒数 选一个.")

    
       
       
    status_choices=[
        (0,"关闭"),
        (1,"运行"),
       
    ]    
    # paiXu=models.SmallIntegerField(verbose_name="排序",choices=paiXu_choices,blank=True, null=True,default=1)

 
    status = models.IntegerField(db_comment='0 关闭,1运行中',choices=status_choices,default=0)
    
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True) 
    updated_at = models.DateTimeField(blank=True, null=True,default=timezone.now)
    webid = models.IntegerField(blank=True, null=True,default=0,db_comment='站点id')   
    cn_memo = models.CharField(max_length=200,blank=True, null=True,db_comment='中文备注')

    uid = models.ForeignKey(User,on_delete=models.CASCADE)

#    单个账户 字段设置 Dl 独立账户

    Dlprice_choices=[
            (0,"全局"),
            (1,"独立"),
        ] 
    
    
    Dlprice_status = models.IntegerField(db_comment='0 全局,1独立',choices=Dlprice_choices,default=0)    
    # DlTOKEN_ADDRESS = models.CharField(verbose_name="独立地址",max_length=255,blank=True, null=True, db_comment='独立地址')
    # DlTOKEN_private = models.CharField(verbose_name="private",max_length=255,blank=True, null=True, db_comment='private')

    DlBuyNumber= models.IntegerField(verbose_name="限制购买数量",blank=True, null=True,default=0,db_comment='购买数量')  
    DlBuyTOKEN_price = models.CharField(verbose_name="限制购买价格",max_length=255,blank=True, null=True, db_comment='购买价格')
    DlSellNumber= models.IntegerField(verbose_name="限制出售数量",blank=True, null=True,default=0,db_comment='出售数量')  
    DlSellTOKEN_price = models.CharField(verbose_name="限制出售价格",max_length=255,blank=True, null=True, db_comment='出售价格')
 





    # tcSports = models.ManyToManyField(TcSport)
    # menOneTwos = models.ManyToManyField(TcOneTwo,verbose_name="两门",)



    # categories = MultiSelectField(choices=CATEGORY_CHOICES,
                                
    #                               # default='1,5')
    #                               default=1)
    class Meta:      
        db_table = 'T_Quantify1'
        db_table_comment = '设置量化'
        # verbose_name="量化方案一"        
        verbose_name_plural = "设置量化"  # 设置 admin 界面上模型的显示名称


class CategoryToken(models.Model):
    name = models.CharField(max_length=100)    
    uid = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table_comment = 'Token分类'
        db_table = 'T_CategoryToken'
        # verbose_name="量化方案一"        
        verbose_name_plural = "Token分类"  # 设置 admin 界面上模型的显示名称

class T_TokenAddr(models.Model): 
# 设置 地址 

    # menOneTwo = models.CharField(max_length=255,blank=True, null=True, db_comment='tcWeb编号str')
    TOKEN_ADDRESS = models.CharField(verbose_name="代币地址",max_length=255,blank=True, null=True, db_comment='代币地址')
    TOKEN_private = models.CharField(verbose_name="private",max_length=255,blank=True, null=True, db_comment='private')
    TOKEN_public = models.CharField(verbose_name="public",max_length=255,blank=True, null=True, db_comment='public')
    TOKEN_price = models.CharField(verbose_name="bnb余额",max_length=255,blank=True, null=True, db_comment='bnb余额')
    TOKEN_otherPrice = models.CharField(verbose_name="代币余额",max_length=255,blank=True, null=True, db_comment='代币余额')

    TOKEN_bak = models.CharField(verbose_name="中文备注",max_length=255,blank=True, null=True, db_comment='中文备注')
         
    status_choices=[
        (0,"停止"),
        (1,"正常"),
       
    ]
    status = models.IntegerField(db_comment='0 停止,正常',choices=status_choices,default=1)
    
    created_at = models.DateTimeField(verbose_name="创建时间",blank=True, null=True,auto_now_add=True) 
    updated_at = models.DateTimeField(verbose_name="修改时间",blank=True, null=True,default=timezone.now)

    QuantifyId= models.IntegerField(verbose_name="量化Id",blank=True, null=True,default=0,db_comment='量化Id')   
    

    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    last_used = models.DateTimeField(blank=True, null=True,auto_now=True)


    BuyNumber= models.IntegerField(verbose_name="购买数量",blank=True, null=True,default=0,db_comment='购买数量')  
    BuyTOKEN_price = models.CharField(verbose_name="购买价格",max_length=255,blank=True, null=True, db_comment='购买价格')
    SellNumber= models.IntegerField(verbose_name="出售数量",blank=True, null=True,default=0,db_comment='出售数量')  
    SellTOKEN_price = models.CharField(verbose_name="出售价格",max_length=255,blank=True, null=True, db_comment='出售价格')
    
    category = models.ForeignKey(CategoryToken, on_delete=models.SET_NULL, null=True, blank=True)
 
    class Meta:      
        db_table = 'T_TokenAddr'
        db_table_comment = '我的钱包'
        # verbose_name="Token地址"
        verbose_name_plural = "我的钱包"  # 设置 admin 界面上模型的显示名称
        



class T_TokenAddrBak(models.Model): 
# 设置 地址 
    # menOneTwo = models.CharField(max_length=255,blank=True, null=True, db_comment='tcWeb编号str')
    TOKEN_ADDRESS = models.CharField(verbose_name="代币地址",max_length=255,blank=True, null=True, db_comment='代币地址')
    TOKEN_private = models.CharField(verbose_name="private",max_length=255,blank=True, null=True, db_comment='private')
    TOKEN_public = models.CharField(verbose_name="public",max_length=255,blank=True, null=True, db_comment='public')
    TOKEN_bak = models.CharField(verbose_name="中文备注",max_length=255,blank=True, null=True, db_comment='中文备注')
    TOKEN_otherPrice = models.CharField(verbose_name="代币余额",max_length=255,blank=True, null=True, db_comment='代币余额')
     
    status_choices=[
        (0,"停止"),
        (1,"正常"),]
    status = models.IntegerField(db_comment='0 停止,正常',choices=status_choices,default=1)
    
    created_at = models.DateTimeField(verbose_name="创建时间",blank=True, null=True,auto_now_add=True) 
    updated_at = models.DateTimeField(verbose_name="修改时间",blank=True, null=True,default=timezone.now)

    QuantifyId= models.IntegerField(verbose_name="量化Id",blank=True, null=True,default=0,db_comment='量化Id')   
    

    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    last_used = models.DateTimeField(blank=True, null=True,auto_now=True)
    
    BuyNumber= models.IntegerField(verbose_name="购买数量",blank=True, null=True,default=0,db_comment='购买数量')  
    BuyTOKEN_price = models.CharField(verbose_name="购买价格",max_length=255,blank=True, null=True, db_comment='购买价格')
    SellNumber= models.IntegerField(verbose_name="出售数量",blank=True, null=True,default=0,db_comment='出售数量')  
    SellTOKEN_price = models.CharField(verbose_name="出售价格",max_length=255,blank=True, null=True, db_comment='出售价格')
    
    category = models.ForeignKey(CategoryToken, on_delete=models.SET_NULL, null=True, blank=True)
 
    class Meta:      
        db_table = 'T_TokenAddrBak'
        db_table_comment = 'T_TokenAddrBak地址'
        verbose_name="T_TokenAddrBak地址"
        


class T_task(models.Model): 
  
    taskId = models.CharField(verbose_name="taskId",max_length=255,blank=True, null=True, db_comment='taskId')
    status_choices=[
        (0,"停止"),
        (1,"正常"),
       
    ]
    status = models.IntegerField(db_comment='0 停止,正常',choices=status_choices,default=1)
    
    created_at = models.DateTimeField(verbose_name="创建时间",blank=True, null=True,auto_now_add=True) 
    updated_at = models.DateTimeField(verbose_name="修改时间",blank=True, null=True,default=timezone.now)

    QuantifyId= models.IntegerField(verbose_name="量化Id",blank=True, null=True,default=0,db_comment='量化Id')  
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    taskRemark = models.CharField(verbose_name="task备注",max_length=255,blank=True, null=True, db_comment='task备注')
 
    class Meta:      
        db_table = 'T_task'
        db_table_comment = '运行中'
        # verbose_name="task地址"
        verbose_name_plural = "运行中"  # 设置 admin 界面上模型的显示名称

        



class T_trade(models.Model):     
    tradeToken = models.CharField(verbose_name="交易者钱包",max_length=255,blank=True, null=True, db_comment='交易者钱包')
    TOKEN_ADDRESS = models.CharField(verbose_name="代币地址",max_length=255,blank=True, null=True, db_comment='代币地址')
  
    taskId = models.CharField(verbose_name="taskId",max_length=255,blank=True, null=True, db_comment='taskId')
    
    tradeStatus_choices=[
        (0,"买"),
        (1,"卖"),
        (2,"Approved"),       
    ]
    tradeStatus = models.IntegerField(verbose_name='0 停止,正常',choices=tradeStatus_choices,default=1,db_comment='交易状态')
    Price = models.DecimalField(verbose_name="交易价格",max_digits=6, decimal_places=4, blank=True, null=True, db_comment='交易价格')
    tradeAmount = models.BigIntegerField(verbose_name="交易量" , blank=True, null=True, db_comment='交易量')
    tradeHash = models.CharField(verbose_name="hash值",max_length=255,blank=True, null=True, db_comment='hash值')

    status_choices=[
        (0,"停止"),
        (1,"正常"),       
    ]
    status = models.IntegerField(db_comment='0 停止,正常',choices=status_choices,default=1)
    
    created_at = models.DateTimeField(verbose_name="创建时间",blank=True, null=True,auto_now_add=True) 
    updated_at = models.DateTimeField(verbose_name="修改时间",blank=True, null=True,default=timezone.now)

    QuantifyId= models.IntegerField(verbose_name="量化Id",blank=True, null=True,default=0,db_comment='量化Id')  
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    taskRemark = models.CharField(verbose_name="task备注",max_length=255,blank=True, null=True, db_comment='task备注')

    status_Tip=[
        (0,"未收取"),
        (1,"已收取"),       
    ]
    statusTip = models.IntegerField(verbose_name="小费",db_comment='0 未收取,1 已收取',choices=status_Tip,default=0)
    tipNumber = models.CharField(verbose_name="小费值",max_length=255,blank=True, null=True, db_comment='小费值')

    
    class Meta:      
        db_table = 'T_trade'
        db_table_comment = '交易表'
        # verbose_name="交易表"
        verbose_name_plural = "交易表"  # 设置 admin 界面上模型的显示名称