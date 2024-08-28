from django.db import models
# Create your models here. 
 
from django.contrib.auth.models import AbstractUser
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import Group,Permission
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import UserManager
from mptt.managers import TreeManager

class CustomUserManager(TreeManager, UserManager):
    # 如果需要，您可以在这里添加自定义方法或覆盖现有方法
    pass

class CustomUser(MPTTModel, AbstractUser):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    # userStakesA= models.BigIntegerField(db_comment='用户质押A数量',blank=True, null=True,default=0)
    # userStakesB= models.BigIntegerField(db_comment='用户质押B数量',blank=True, null=True,default=0)
    
    userStakesA= models.FloatField(db_comment='用户质押A数量',verbose_name="用户质押A数量", blank=True, null=True,default=0)
    userStakesB= models.FloatField(db_comment='用户质押B数量',verbose_name="用户质押B数量", blank=True, null=True,default=0)
    
    
    # buyPrice = models.DecimalField(verbose_name="购买价格",  blank=True, null=True)

    userStakesBfanHuan= models.FloatField(db_comment='返还用户B数量',verbose_name="返还用户B数量", blank=True, null=True,default=0)
    fanHuan= models.FloatField(db_comment='可以返还用户B数量',verbose_name="可以返还用户B数量", blank=True, null=True,default=0)
    EbcCreated_at = models.BigIntegerField(verbose_name="创建时间",blank=True, null=True,default=0)
    EbcLastFanHuan_at = models.BigIntegerField(verbose_name="上一次返还时间",blank=True, null=True,default=0)
    # EbcFanHuanDay_at = models.BigIntegerField(verbose_name="上一次返还时间",blank=True, null=True)

    status_choices=[
        (0,"未生效"),
        (1,"已生效"),       
    ]
    status = models.IntegerField(db_comment='0 未生效,1已生效:不可购买矿机',choices=status_choices,default=0)
    
    kapaiA = models.IntegerField(db_comment='A卡数量',blank=True, null=True,default=0)

    kapaiB = models.IntegerField(db_comment='B卡卡数量',blank=True, null=True,default=0)

    kapaiC = models.IntegerField(db_comment='C卡卡数量',blank=True, null=True,default=0)

    
    kapaiLevel = models.IntegerField(db_comment='0 买A卡,1买B卡 2 买C卡',blank=True, null=True,default=0)

    userLevel = models.IntegerField(db_comment='用户等级',blank=True, null=True,default=0)

    tuanduiLevel = models.IntegerField(db_comment='团队等级',blank=True, null=True,default=0)

    cengShu = models.IntegerField(db_comment='当前矿机code',blank=True, null=True,default=1)

    zhiTuiNum = models.IntegerField(db_comment='暂存直推人数',blank=True, null=True,default=0)

    statusTiXian_choices=[
        (0,"正常提现"),
        (1,"不可提现"),       
    ]
    statusTiXian = models.IntegerField(db_comment='0 正常提现,不可提现',choices=statusTiXian_choices,default=0)



     
    # 添加自定义用户管理器
    objects = CustomUserManager()
    
    # 添加自定义的related_name以解决冲突
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="customuser_set",  # 自定义related_name
        related_query_name="customuser",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="customuser_permission_set",  # 自定义related_name
        related_query_name="customuser",
    )
    

    class MPTTMeta:
        order_insertion_by = ['username']
    class Meta:
        db_table = 'T_custom_user'  # 自定义的表名
        db_table_comment = '用户列表'

        verbose_name_plural = "用户列表"  # 设置 admin 界面上模型的显示名称



# Layer= 0充值 1 代数 2 层数 3 #提现到账 日志  8.提现记录
class ebcJiaSuShouYiJiLu(models.Model):  
    uidA = models.FloatField(db_comment='用户A-发送方', verbose_name="用户A-发送方", blank=True, null=True, default=0.0)
    uidB = models.FloatField(db_comment='用户B-接收方',verbose_name="用户B-接收方", blank=True, null=True,default=0) 
    status_choices=[
        (0,"未生效"),
        (1,"已生效"),       
    ]
    status = models.IntegerField(db_comment='0 未生效,1已生效:反润生效',choices=status_choices,default=0) 
    created_at = models.DateTimeField(verbose_name="创建时间",blank=True, null=True,auto_now_add=True)  
    # 同时代表amount
    fanHuan= models.FloatField(db_comment='每次返还额度',verbose_name="每次返还额度", blank=True, null=True,default=0)
    liuShuiId = models.IntegerField(db_comment='流水ID 合约同步',blank=True, null=True,default=0) 
    Remark = models.CharField(verbose_name="备注",max_length=255,blank=True, null=True, db_comment='task备注')
    Layer = models.IntegerField(verbose_name="类型",db_comment='0充值 1 代数 2 层数 3 #提现到账 日志 4.购买燃料包  11.得到奖金池',blank=True, null=True,default=0)
    tokenZhiYaJiShiId = models.IntegerField(db_comment='质押表ID',blank=True, null=True,default=0) 

    cTime = models.BigIntegerField(db_comment='操作时间',blank=True, null=True,default=0)   
    hash = models.CharField(verbose_name="链上hash",max_length=255,blank=True, null=True, db_comment='链上hash')

 


    
    # def __str__(self):
    #     return f"EbcJiaSuShouYiJiLu {self.id}"
 
    class Meta:      
        db_table = 't_ebcJiaSuShouYiJiLu'
        db_table_comment = '加速收益记录'
        # verbose_name="task地址"
        verbose_name_plural = "加速收益记录"  # 设置 admin 界面上模型的显示名称


#  每个需要分润的记录 都保存在质押表  status 0 质押中,1 已释放 layer 0 矿机 1日返利   非0 由于不需要运算所以未记录（链上含义 1,2,3  =a b c 卡牌 ）
class tokenZhiYaJiShi(models.Model): 
    
    tokenName  = models.CharField(verbose_name="质押名称",max_length=255,blank=True, null=True, db_comment='质押名称')        
    nodeKjCode = models.IntegerField(verbose_name="矿机Code",db_comment='矿机Code',blank=True, null=True,default=0)

    #在使用 节点矿机暂时不使用， 默认是1个矿机
    number= models.FloatField(db_comment='质押数量',verbose_name="质押数量",  blank=True, null=True)
    zhiYaTime= models.BigIntegerField(db_comment='质押100天',blank=True, null=True,) 
    kaiShiTime = models.BigIntegerField(verbose_name="开始质押时间",blank=True, null=True)
    uTime = models.BigIntegerField(verbose_name="更新时间",blank=True, null=True)
    status_choices=[
        (0,"质押中"),
        (1,"已释放"),       
    ]
    status = models.IntegerField(db_comment='0 质押中,已释放',choices=status_choices,default=0)    
    created_at = models.DateTimeField(verbose_name="创建时间",blank=True, null=True,auto_now_add=True)  
    uid = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Remark = models.CharField(verbose_name="备注",max_length=255,blank=True, null=True, db_comment='task备注')
    Layer = models.IntegerField(verbose_name="类型",db_comment='0 矿机质押,1日返利 其他非零 是卡牌  ',blank=True, null=True,default=0)

    amount= models.FloatField(db_comment='质押额度',verbose_name="质押额度",  blank=True, null=True)
    amountType = models.CharField(verbose_name="质押类型",max_length=255,blank=True, null=True, db_comment='质押类型')

    amountShouYi= models.FloatField(db_comment='质押收益',verbose_name="质押收益",  blank=True, null=True)

    statusTiXian_choices=[
        (0,"正常提现"),
        (1,"不可提现"),       
    ]
    statusTiXian = models.IntegerField(db_comment='0 正常提现,不可提现',choices=statusTiXian_choices,default=0)



    @staticmethod
    def get_kuangjiList_by_uid(t_user):
        # 过滤 uid 等于 parent_user 且 status 等于 1 的记录
        t_kuangji = tokenZhiYaJiShi.objects.filter(uid=t_user, status=1).first()
        if t_kuangji:
            return t_kuangji
        return None




    class Meta:      
        db_table = 't_ymiiZhiYaJiShi'
        db_table_comment = '质押代币时间'
        # verbose_name="task地址"
        verbose_name_plural = "质押代币时间"  # 设置 admin 界面上模型的显示名称


# # 没用 过一段删掉
# class ebcZhiYa(models.Model): 
  
#     userStakesA= models.BigIntegerField(db_comment='用户质押A数量',blank=True, null=True,)
#     userStakesB= models.BigIntegerField(db_comment='用户质押B数量',blank=True, null=True,)
#     userStakesBfanHuan= models.FloatField(db_comment='返还用户B数量',verbose_name="返还用户B数量",  blank=True, null=True)
#     fanHuan= models.FloatField(db_comment='可以返还用户B数量',verbose_name="可以返还用户B数量",  blank=True, null=True)


#     # uidA = models.CharField(verbose_name="用户A用户名",max_length=255,blank=True, null=True, db_comment='代币地址')
#     # uidB = models.CharField(verbose_name="用户B用户名",max_length=255,blank=True, null=True, db_comment='代币地址')
#     status_choices=[
#         (0,"未生效"),
#         (1,"已生效"),       
#     ]
#     status = models.IntegerField(db_comment='0 未生效,1已生效',choices=status_choices,default=0)
    
#     created_at = models.DateTimeField(verbose_name="创建时间",blank=True, null=True,auto_now_add=True) 
#     # updated_at = models.DateTimeField(verbose_name="修改时间",blank=True, null=True,default=timezone.now)
#     EbcCreated_at = models.BigIntegerField(verbose_name="创建时间",blank=True, null=True)
#     EbcLastFanHuan_at = models.BigIntegerField(verbose_name="上一次返还时间",blank=True, null=True)

#     # QuantifyId= models.IntegerField(verbose_name="量化Id",blank=True, null=True,default=0,db_comment='量化Id')  
#     uid = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
#     Remark = models.CharField(verbose_name="备注",max_length=255,blank=True, null=True, db_comment='task备注')
 
#     class Meta:      
#         db_table = 't_ebcZhiYa'
#         db_table_comment = '加速收益记录'
#         # verbose_name="task地址"
#         verbose_name_plural = "加速收益记录"  # 设置 admin 界面上模型的显示名称



# 提现
class payToken(models.Model):  
    uidA = models.IntegerField(db_comment='用户A-发送方', verbose_name="用户A-发送方", blank=True, null=True, default=0)
    uidB = models.IntegerField(db_comment='用户B-接收方',verbose_name="用户B-接收方", blank=True, null=True,default=0) 
    status_choices=[
        (0,"未生效"),
        (1,"返还"),  
        (2,"hash验证失败"), 
        (3,"hash验证成功"),      
    ]
    status = models.IntegerField(db_comment='0 未生效,1,返回hash ,2 hash验证失败,3hash验证成功',choices=status_choices,default=0) 
    created_at = models.DateTimeField(verbose_name="创建时间",blank=True, null=True,auto_now_add=True)  
    amount= models.FloatField(db_comment='每次返还额度',verbose_name="每次返还额度", blank=True, null=True,default=0)
    liuShuiId = models.IntegerField(db_comment='流水ID 合约同步',blank=True, null=True,default=0) 
    Remark = models.CharField(verbose_name="备注",max_length=255,blank=True, null=True, db_comment='task备注')
    Layer = models.IntegerField(verbose_name="类型",db_comment='0提现',blank=True, null=True,default=0)    
    tiXianWallter = models.CharField(verbose_name="提现钱包",max_length=255,blank=True, null=True, db_comment='提现钱包')
    TxHash = models.CharField(verbose_name="交易hash",max_length=255,blank=True, null=True, db_comment='交易hash')    
    hashInfo = models.CharField(verbose_name="hash信息",max_length=255,blank=True, null=True, db_comment='hash信息') 
    tiBiADDRESS = models.CharField(verbose_name="提取代币地址",max_length=255,blank=True, null=True, db_comment='提取代币地址')    
    AdminUser = models.IntegerField(db_comment='管理账号ID', verbose_name="管理账号ID", blank=True, null=True, default=0)

    HashId = models.CharField(verbose_name="唯一hashId",max_length=255,blank=True, null=True, db_comment='唯一hashId')    


    
    # def __str__(self):
    #     return f"EbcJiaSuShouYiJiLu {self.id}"
 
    class Meta:      
        db_table = 't_payToken'
        db_table_comment = '提现流水'
        # verbose_name="task地址"
        verbose_name_plural = "提现流水"  # 设置 admin 界面上模型的显示名称



class buyNode(models.Model):  
    uid = models.IntegerField(db_comment='用户',blank=True, null=True,default=0) 
    status_choices=[
        (0,"未生效"),
        (1,"已生效"),       
    ]
    status = models.IntegerField(db_comment='0 未生效,1已生效:反润生效',choices=status_choices,default=0) 
    cTime = models.BigIntegerField(db_comment='操作时间',blank=True, null=True,default=0)   
    uTime =models.BigIntegerField(db_comment='更新时间',blank=True, null=True,default=0)  
    amount= models.FloatField(db_comment='购买价格',verbose_name="购买价格", blank=True, null=True,default=0)
    lianShangId = models.IntegerField(db_comment='链上ID 合约同步',blank=True, null=True,default=0) 
    NodeName = models.CharField(verbose_name="购买矿机名称",max_length=255,blank=True, null=True, db_comment='购买矿机名称')    
    Remark = models.CharField(verbose_name="备注",max_length=255,blank=True, null=True, db_comment='task备注')
    Layer = models.IntegerField(verbose_name="类型",db_comment='0节点矿机',blank=True, null=True,default=0)
    # def __str__(self):
    #     return f"EbcJiaSuShouYiJiLu {self.id}"
 
    class Meta:      
        db_table = 't_buyNode'
        db_table_comment = '购买节点矿机'
        # verbose_name="task地址"
        verbose_name_plural = "购买节点矿机"  # 设置 admin 界面上模型的显示名称

class userToken(models.Model):  

    status_choices=[
        (0,"未生效"),
        (1,"已生效"),       
    ]
    status = models.IntegerField(db_comment='0 未生效,1已生效',choices=status_choices,default=0) 
    cTime = models.IntegerField(db_comment='操作时间',blank=True, null=True,default=0)   
    uTime =models.IntegerField(db_comment='更新时间',blank=True, null=True,default=0)  
    usdtToken= models.FloatField(db_comment='usdtToken',verbose_name="usdtToken", blank=True, null=True,default=0)
    ylToken= models.FloatField(db_comment='ylToken',verbose_name="ylToken", blank=True, null=True,default=0)
    jzToken= models.FloatField(db_comment='jzToken',verbose_name="jzToken", blank=True, null=True,default=0)
    oneToken= models.FloatField(db_comment='oneToken',verbose_name="oneToken", blank=True, null=True,default=0)
    towToken= models.FloatField(db_comment='towToken',verbose_name="towToken", blank=True, null=True,default=0)
    Remark = models.CharField(verbose_name="备注",max_length=255,blank=True, null=True, db_comment='task备注')
    uid = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"EbcJiaSuShouYiJiLu {self.id}"
 
    class Meta:      
        db_table = 't_userToken'
        db_table_comment = '用户Token'
        # verbose_name="task地址"
        verbose_name_plural = "用户Token"  # 设置 admin 界面上模型的显示名称

