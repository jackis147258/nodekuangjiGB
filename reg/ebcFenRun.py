
import asyncio
from django.contrib.auth.models import  Group
from .models import CustomUser,ebcJiaSuShouYiJiLu,tokenZhiYaJiShi
from decimal import Decimal
from itertools import islice
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
import tools
import logging
logger = logging.getLogger(__name__)

from datetime import  timedelta
from django.db import transaction
from decouple import config

 

from django.contrib.auth import get_user_model
User = get_user_model()
from typing import Type
from .  import ebcFenRun

def FenRunUser(userName):
    tokenZhiYaList=tokenZhiYaJiShi.objects.filter(status=0,tokenName=config('TOKEN_NAME2', default=''),uid=userName)
    for tokenZhiYa in tokenZhiYaList:  
        userFenRun(tokenZhiYa)
    return 'ok'

# 通过事务 批量操作 暂停了， 用上面 导入userName 代替
def FenRun():
    tokenZhiYaList=tokenZhiYaJiShi.objects.filter(status=0,tokenName=config('TOKEN_NAME2', default=''))
    for tokenZhiYa in tokenZhiYaList:  
        userFenRun(tokenZhiYa)
    return 'ok'
 


# 单独一个用户 分销返加速  
def userFenRun(tokenZhiYa: Type[tokenZhiYaJiShi]):
    logger.info('start:用户'+str(tokenZhiYa.uid) +'开始分润' )        
    try:
        t_user = User.objects.get(id=tokenZhiYa.uid_id)
    except User.DoesNotExist:
        t_user = None
        logger.info('Failed:用户'+str(tokenZhiYa.uid)+ '不存在' )
        return 'no'
    # 分润方法
    # 获得id, 向上
    #  1. 获取用户id ,根据id 每次减去1，向上处理20个用户，如果到id为0 就停止处理。  
    # 要处理的每个用户， 做如下判断:  先测量向上处理的数字 5个用户以内的 当用户直接子节点节点数量 大于1个，
    # 给每个用户 的fanHuan 字段 加1 ，同上 处理数字大于5 ，要求用户直接子节点数量大于2个，才给用户fanHuan字段加1 ，
    # 否则不加。    
    try:             
        t_jiasu10=0
        layerName=""
        if tokenZhiYa.layer==0:#矿机 计算    
            #  推广入金收益的1.5倍 的百分之一 的 百分之六 人加速        
            t_jiasu10=tokenZhiYa.number*1.5*0.01*0.06  
            layerName="质押矿机" 
        if tokenZhiYa.layer==1:           
            #  layer==1 输入 获取日返还的百分之六 人加速         
            t_jiasu10=tokenZhiYa.number*0.06 
            layerName="单日返利" 
        t_parent_id=t_user.parent_id    
        # t_parent_id=t_user.id    
        for i in range(0, 10, 1): #执行10次 向上找10级        
            # 处理第一个人             
              # 到了顶级 就直接 跳出
            if t_parent_id==1 or t_parent_id==None:
                logger.info('用户id:'+str(t_parent_id) +t_user.username+'到了顶级不进行分润了' )
                break                        
            try:                
                parentUser = CustomUser.objects.get(id=t_parent_id)
                # 执行获取到 parentUser 后的逻辑
            except CustomUser.DoesNotExist:
                # 处理 parentUser 不存在的情况
                continue
            if parentUser.fanHuan is None:
                parentUser.fanHuan=0                    
            children_count = parentUser.get_children().count()  
            # 看是否满足返还条件
            if isFanDai(i,children_count):                 
                try:
                    with transaction.atomic():                        
                        parentUser.fanHuan+=t_jiasu10
                        parentUser.save()
                        # 写入记录     
                        t_ebcJiaSuShouYiJiLu=ebcJiaSuShouYiJiLu ()
                        t_ebcJiaSuShouYiJiLu.uidA=t_user.id   #发送方
                        t_ebcJiaSuShouYiJiLu.uidB=parentUser.id  # 接收方
                        t_ebcJiaSuShouYiJiLu.status=1  #已转
                        t_ebcJiaSuShouYiJiLu.Layer=1  # 0充值 1 代数 2 层数 
                        t_ebcJiaSuShouYiJiLu.fanHuan=t_jiasu10
                        t_ebcJiaSuShouYiJiLu.Remark='代数返加速'+layerName+str(t_jiasu10)      #'返6%'    
                        t_ebcJiaSuShouYiJiLu.save()                          
                except Exception as e:
                    # 处理错误，此时事务已经回滚 
                    result = ["Failed-userFenRun", f"ERROR: {e}"]
                    logger.info(result)
                    # return result
            t_parent_id=parentUser.parent_id                
        logger.info('用户'+str(t_user.id) +t_user.username+'代级分润完成' )
        
        
        logger.info('用户'+str(t_user.id) +t_user.username+'层级分润开始' )
        #  推广入金收益的1%个人加速
        # t_jiasu1=t_user.userStakesB*1.5*0.01*0.01        
        # t_jiasu1=tokenZhiYa.number*1.5*0.01*0.01        
        t_jiasu1=0
        if tokenZhiYa.layer==0:#矿机 计算            
            t_jiasu1=tokenZhiYa.number*1.5*0.01*0.01
        if tokenZhiYa.layer==1:            
            t_jiasu1=tokenZhiYa.number*0.01

        
        # 处理伞下1%
        j=0
        for i in islice(range(t_user.id-1, 0, -1),51): #islice  最多执行30次
            j=j+1
            # 处理第一个人
            # if i==t_user.id-1
            a_nodeUsers = CustomUser.objects.filter(pk=i)
            if not a_nodeUsers.exists():
                continue  
    
            a_nodeUser = a_nodeUsers.first()
            try:
                children_count = a_nodeUser.get_children().count()
            except Exception as e:
                print(f"Error: {e}")
            # children_count = a_nodeUser.get_children().count()   
            # 如果为真 ，那么给用户增加加速值1%
            if isFan(j,children_count): 
                try:
                    with transaction.atomic():                        
                        a_nodeUser.fanHuan+=t_jiasu1
                        a_nodeUser.save()
                        # 增加记录
                        # 写入记录     
                        t_ebcJiaSuShouYiJiLu=ebcJiaSuShouYiJiLu ()
                        t_ebcJiaSuShouYiJiLu.uidA=t_user.id   #发送方
                        t_ebcJiaSuShouYiJiLu.uidB=a_nodeUser.id  # 接收方
                        t_ebcJiaSuShouYiJiLu.status=1  #已转
                        t_ebcJiaSuShouYiJiLu.Layer=2       # 伞下用户                 
                        t_ebcJiaSuShouYiJiLu.fanHuan=t_jiasu1
                        t_ebcJiaSuShouYiJiLu.Remark='层级返加速'+layerName+str(t_jiasu1)    
                        t_ebcJiaSuShouYiJiLu.save()  
                except Exception as e:
                    # 处理错误，此时事务已经回滚 
                    result = ["Failed-userFenRun", f"ERROR: {e}"]
                    logger.info(result)
        # 代数 和 层级 处理后 用户 状态为1 处理完成
        tokenZhiYa.status=1
        tokenZhiYa.save()
        # t_user.status=1
        # t_user.save()
        
        logger.info('用户 id'+str(t_user.id) +t_user.username+'代级层级完成' )
        
    except Exception as e:  
        # self.buyTokensBuildTransaction() # 下一次购买准备
        result = ["Failed-userFenRun", f"ERROR: {e}"]
        print(result)
        # self.getLpPrice()   
    
    return 'ok'

# 是否返代级收益
def isFanDai(j,children_count):
    if j <= 0 and children_count >= 1:
        return True
    elif j <= 1 and children_count >= 2:
        return True
    elif j <= 2 and children_count >= 3:
        return True
    elif j <= 3 and children_count >= 4:
        return True      
    elif j <= 4 and children_count >= 5:
        return True
    elif j <= 5 and children_count >= 6:
        return True
    elif j <= 6 and children_count >= 7:
        return True
    elif j <= 7 and children_count >= 8:
        return True      
    elif j <= 8 and children_count >= 9:
        return True
    elif j <= 9 and children_count >= 10:
        return True  
    else:
        return False

# 是否返层级收益
def isFan(j,children_count):
    if j <= 5 and children_count >= 1:
        return True
    elif j <= 10 and children_count >= 2:
        return True
    elif j <= 15 and children_count >= 3:
        return True
    elif j <= 20 and children_count >= 4:
        return True
    elif j <= 25 and children_count >= 5:
        return True
    elif j <= 30 and children_count >= 6:
        return True
    elif j <= 35 and children_count >= 7:
        return True
    elif j <= 40 and children_count >= 8:
        return True
    elif j <= 45 and children_count >= 9:
        return True
    elif j <= 50 and children_count >= 10:
        return True
    else:
        return False
    


# 接收用户 接收充值
def createEbcUser(value):
    password='147258369'
    logger.info('开始记录充值流水:'+str(len(value[0]))  +'-个' )

    # 添加几条用户数据
    for i in  range(0, len(value[0]), 1)  :        
        
        logger.info('用户:'+str(value[0][i])  +' layer:'+str(value[2][i])+' time:'+str(value[3][i]) +' amount:'+str(value[1][i]) )

        # logger.info('用户:'+value[0][i]  +'layer:'+value[2][i]+'time:'+value[3][i] +'amount:'+value[1][i] )
        
        # 流水重复限制         
        liuShuiIdNumber=int(value[4][i]) #得到 流水id 
        liuShuiIdObj=ebcJiaSuShouYiJiLu.objects.filter(liuShuiId=liuShuiIdNumber).first()
        # 表示已经处理过流水
        if liuShuiIdObj:
            result = ["test", f"重复流水跳过"]
            logger.info(result)
            continue
        now_user = User.objects.filter(username=value[0][i]).first()

        # logger.info('用户:'+value[0][i]  +'layer:'+int(value[2][i])+'time:'+value[3][i] +'amount:'+value[1][i] )
        # CustomUser:now_user =  User.objects.filter(username=value[0][i]).first()

        # parent_user = User.objects.filter(username=value[1][i]).first()
        # parentId=1
        # if parent_user:
        #     parentId=parent_user.id        
        try:          
            amount = tools.blockchain_number_to_float(value[1][i]) # 获得 amount
            
            layer = int(value[2][i]) # 获得 layer  来自 链上 0矿机   非0 是卡牌 1 2 3

            # 如果转换成功，表示是可以进行数学运算的数字
            t_userStakesBfanHuan = amount * 1.5
            # print(f"The result is: {t_userStakesBfanHuan}")

        except ValueError:
            # 如果转换失败，表示不是一个有效的 Decimal 值
            print("不是一个有效的 Decimal 值")
        
            
        
                        
        # 表示 用户已经存在 那么修改 用户的属性
        if now_user: 
                            
            if layer==0: # 是矿机
                try:
                    with transaction.atomic():
                        now_user.userStakesB=amount
                        now_user.userStakesBfanHuan=t_userStakesBfanHuan
                        now_user.status=1          #改变状态 1 不可以在次购买矿机
                        now_user.EbcCreated_at=value[3][i] #得到矿机运行时间
                        now_user.EbcLastFanHuan_at=value[3][i]
                        now_user.kapaiLevel=now_user.kapaiLevel+1
                        now_user.save()
                        # 记录质押矿机 信息
                        tokenZhiYaJiShi.objects.create(
                            tokenName=config('TOKEN_NAME2', default=''),
                            number=tools.blockchain_number_to_float(value[1][i]),
                            status=0,
                            layer=0, #0 是矿机  非零 是 各类卡牌
                            uid=now_user,
                            zhiYaTime=int(timedelta(days=100).total_seconds())   ,     
                            kaiShiTime=value[3][i], #int(timezone.now().timestamp()),
                            Remark=str(now_user.id)+'质押矿机'
                        )
                    
                    # 写入记录
                        ebcJiaSuShouYiJiLu.objects.create(
                            uidB=now_user.id,
                            status=1,
                            fanHuan=tools.blockchain_number_to_float(value[1][i]),
                            liuShuiId=int(value[4][i]),
                            Layer=0, #代币充值 
                            Remark='充值矿机'   #+config('TOKEN_NAME2', default='') 
                        )
                    logger.info('成功质押矿机:'+str(now_user.username) )

                except Exception as e:
                    # 处理异常
                    result = ["Failed-everybadyFan", f"ERROR: {e}"]
                    print(result)
                    logger.info(result)
                    return result
                # 处理分润
                ebcFenRun.FenRunUser(now_user)
                continue

            else:
                try:
                    with transaction.atomic():
                        # 处理卡牌购买
                        strName='A'
                        kapaiNumber=0
                        kapaiLevel=0
                        if layer==1:#A卡
                            strName='A'
                            kapaiNumber=10  
                            kapaiLevel=1   
                            now_user.kapaiA+=kapaiNumber           
                        if layer==2:#B卡
                            strName='B'
                            kapaiNumber=8   
                            kapaiLevel=20  
                            now_user.kapaiB+=kapaiNumber           
                        if layer==3:#C卡
                            strName='C'
                            kapaiNumber=6
                            kapaiLevel=30
                            now_user.kapaiC+=kapaiNumber
                        # now_user.userStakesA+=kapaiNumber
                        # now_user.kapaiA+=kapaiNumber
                        now_user.kapaiLevel=kapaiLevel
                        now_user.save() 
                                    # +config('TOKEN_NAME1', default='')
                        ebcJiaSuShouYiJiLu.objects.create(
                            uidB=now_user.id,
                            status=1,  
                            fanHuan=tools.blockchain_number_to_float(value[1][i]),
                            liuShuiId=int(value[4][i]),
                            Layer=0, #0代币 充值
                            Remark='充值卡牌'+strName        )
                        logger.info('成功购买卡牌:'+now_user.username )
                except Exception as e:
                    # 处理异常
                    result = ["Failed-everybadyFan", f"ERROR: {e}"]
                    print(result)
                    logger.info(result)
                    return result
            # continue
    logger.info('结束记录充值流水:'+str(len(value[0]))  +'个' )
    return 'ok'

#  获得每日奖励 并返现
def everybadyFan(user):
    try:   
        # 获取当前时间戳   1711685804
        current_timestamp = int(timezone.now().timestamp())
        print(current_timestamp)
        
        # 获取一天的时间戳
        one_day_timestamp = 24 * 60 * 60
        print(one_day_timestamp)
        t_jiasu15=0

        


        
        # 如果 当前时间 小于 最后一次 加1.5% 的时间 那么应该 增加 并 扩展一天时间戳  接收时间戳 是毫秒级 转秒级
        if user.EbcLastFanHuan_at <current_timestamp:
            
            try:
                with transaction.atomic():                        
                    #  推广入金收益的1%个人加速
                    t_jiasu15=user.userStakesB *0.015
                    user.fanHuan+=t_jiasu15
                    user.EbcLastFanHuan_at+=int(one_day_timestamp)
                    # user.EbcLastFanHuan_at+=one_day_timestamp,    
                    # 回复分润状态
                    # user.status=0
                    # t_user.save()    
                    user.save()
                    
                    # 写入记录     
                    t_ebcJiaSuShouYiJiLu=ebcJiaSuShouYiJiLu ()
                    # t_ebcJiaSuShouYiJiLu.uidA=t_user   #发送方
                    t_ebcJiaSuShouYiJiLu.uidB=user.id  # 接收方
                    t_ebcJiaSuShouYiJiLu.status=1  #已转
                    t_ebcJiaSuShouYiJiLu.Layer=3  #提现到账 日志
                    
                    t_ebcJiaSuShouYiJiLu.fanHuan=t_jiasu15

                    t_ebcJiaSuShouYiJiLu.Remark='日返1.5%'    
                    t_ebcJiaSuShouYiJiLu.save() 
                    
                    # 增加向上返利记录
                    tokenZhiYaJiShi.objects.create(
                        tokenName=config('TOKEN_NAME2', default=''),
                        number=t_jiasu15,
                        status=0,#0 未分配利润  1  已分配
                        layer=1,# 0默认质押矿机  1 日返
                        uid=user,
                        zhiYaTime=int(timedelta(days=100).total_seconds())   ,     
                        kaiShiTime=int(timezone.now().timestamp()),
                        Remark=str(user.id)+'日加速收益'
                    )
                    return True, "返"+str(t_jiasu15)                
            except Exception as e:
                # 处理异常
                result = ["Failed-获得每日奖励", f"ERROR: {e}"]
                print(result)
                return result
                
        return False, "当天已返"
    except Exception as e:  
            # self.buyTokensBuildTransaction() # 下一次购买准备
            result = ["Failed-everybadyFan", f"ERROR: {e}"]
            print(result)
            return result
            # self.getLpPrice()   



# 提现扣除数据库 数据
def isTiXian(amount,tixianwallter):    
    now_user = User.objects.filter(username=tixianwallter).first()
    if now_user:
        # if now_user.fanHuan<0 or now_user.fanHuan<Decimal(amount):
        if now_user.fanHuan<0  :
            result=['返回金额小于0']
            return False 
        if now_user.userStakesBfanHuan<=0:
            result=['返还余额小于0']
            return False        
        # # 判断 总共要返还的数量小于 要返还的数量 那么取走剩余。重置用户.
        # if now_user.userStakesBfanHuan<amount:
        #     amount=now_user.userStakesBfanHuan            
        # # now_user.fanHuan=now_user.fanHuan-Decimal(amount)
        # now_user.fanHuan=0
        # now_user.userStakesBfanHuan=now_user.userStakesBfanHuan-Decimal(amount)
        # now_user.save()
        return True
    return False


# 提现扣除数据库 数据
def tiXianOksql(amount,tixianwallter):    
    now_user = User.objects.filter(username=tixianwallter).first()
    if now_user:
        # if now_user.fanHuan<0 or now_user.fanHuan<Decimal(amount):
        if now_user.fanHuan<0  :
            return False
        if now_user.userStakesBfanHuan<=0:
            return False
        # 判断 总共要返还的数量小于 要返还的数量 那么取走剩余。重置用户.
        if now_user.userStakesBfanHuan<amount:
            amount=now_user.userStakesBfanHuan            
        # now_user.fanHuan=now_user.fanHuan-Decimal(amount)
        now_user.fanHuan=0
        now_user.userStakesBfanHuan=now_user.userStakesBfanHuan-amount
        now_user.save()
        return True
    return False
    
        
# 提现扣除数据库 数据
def tuanDuiRenShu(username):
    try: 
        # 如果 当前时间 小于 最后一次 加1.5% 的时间 那么应该 增加 并 扩展一天时间戳
        user = User.objects.filter(username=username).first()
        if user:
            #获得直推人数 
            children = user.get_children()     
            # 提取用户集合的名字
            # children_names = [child.username for child in children if child.status == 1]              
            # children_names = [child.username for child in children ]  
            children_names = [
                (child.username, "已开挖" if child.cengShu >=2 else "未挖矿") 
                for child in children
            ]            
            children_count = user.get_children().count()   
            # 获得全部后代人数
            get_descendants = user.get_descendants()     
            # 提取用户集合的名字          
            descendants_names = [
                (child.username, "已开挖" if child.cengShu >=2 else "未挖矿") 
                for child in get_descendants
            ]
            get_descendants_count=user.get_descendants().count()
            # total_records = len(get_descendants)

            # 获得包括自己的全部祖先节点
            # 共享人数
            userLast = CustomUser.objects.order_by('-id').first()
            gongXiangRenShu=userLast.id-user.id

            
            # 将变量保存到字典中
            result_dict = {
                'valid': True,
                'children_count': children_count,
                'children_names': children_names,  # 将用户集合的名字添加到字典
                'get_descendants': get_descendants_count,   #获得全部后代人数
                'descendants_names': descendants_names,  # 将用户集合的名字添加到字典
                'gongXiangRenShu':gongXiangRenShu,   #共享人数          
            }
        
            # t_js=JsonResponse({'valid': True, 'children_count': children_count,'get_descendants': get_descendants,'get_ancestors_include_self': get_ancestors_include_self,}) 
 
        return True, result_dict
    except Exception as e:  
            # self.buyTokensBuildTransaction() # 下一次购买准备
            result = ["Failed-everybadyFan", f"ERROR: {e}"]
            print(result)            
            return False , result
            # self.getLpPrice()   
     