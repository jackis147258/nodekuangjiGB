
# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
from .forms import SignUpForm,UserMoveForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import  Group

 # Create your views here.
from .serializers import CourseSerializer,CustomUserSerializer,ebcJiaSuShouYiJiLuSerializer,tokenZhiYaJiShiSerializer ,payTokenSerializer,webInfoSerializer
from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import JsonResponse
from .models import CustomUser,userToken,ebcJiaSuShouYiJiLu ,tokenZhiYaJiShi,payToken 
from .  import nodeKjFenRun  ,ebcUserTuichu 
from django.contrib.auth import get_user_model
# from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from apiV1.DeFi2.ebcTiXian import dfEbcTixian
from config import EbcContractTokenAddress
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

# from mptt.utils import move_to
# from mptt.models import move_to
 
import logging
logger = logging.getLogger(__name__)

import asyncio

from django.contrib.auth import get_user_model
User = get_user_model()

import redis

from django.http import JsonResponse
# from django_redis import get_redis_connection
from datetime import datetime, timedelta


from typing import Optional
from django.db import transaction
from django.utils import timezone

import hashlib
import time
import hmac
 
from eth_account import Account
from eth_account.messages import encode_defunct

from Crypto.Hash import keccak
import eth_abi
from eth_utils import to_bytes
from eth_utils import to_bytes, to_checksum_address

from app1.models import webInfo
from web3 import Web3
from django.db.models import Q

from .decorators import with_lang

from .utils import get_message

# 导入必要的模块

# 矿机属性饲养周期
nodes_att_shengzhang = {  
    "nodeKJ": 365,  # 
}

# 矿机日收益率  %
nodes_att_daily_rate = {  
    "nodeKJ0": 1,  # （矿机）
    "nodeKJ1": 1,  # （矿机）
    "nodeKJ2": 1.5,  # （矿机）
    "nodeKJ3": 1.6,  # （矿机）
    "nodeKJ4": 1.7,  # （矿机）
    "nodeKJ5": 1.8,  # （矿机）
    "nodeKJ6": 1.83,  # （矿机）
    "nodeKJ7": 1.84,  # （矿机）
    "nodeKJ8": 1.85,  # （矿机）
    "nodeKJ9": 1.86,  # （矿机）
    "nodeKJ10": 1.87,  # （矿机）
    "nodeKJ11": 1.88,  # （矿机）
    "nodeKJ12": 1.89,  # （矿机）
    "nodeKJ13": 1.9,  # （矿机）
    "nodeKJ14": 1.91,  # （矿机）
    "nodeKJ15": 1.92,  # （矿机）
    "nodeKJ16": 1.93,  # （矿机）
    "nodeKJ17": 1.94,  # （矿机）
    "nodeKJ18": 1.95,  # （矿机）
    "nodeKJ19": 1.96,  # （矿机）
    "nodeKJ20": 1.97,  # （矿机）
    "nodeKJ21": 1.98,  # （矿机）
    "nodeKJ22": 1.99,  # （矿机）
    "nodeKJ23": 2.0,  # （矿机）
    "nodeKJ24": 2.01,  # （矿机）
    "nodeKJ25": 2.02,  # （矿机）
    "nodeKJ26": 2.03,  # （矿机）
    "nodeKJ27": 2.04,  # （矿机）
    "nodeKJ28": 2.05,  # （矿机）
    "nodeKJ29": 2.06,  # （矿机）
    "nodeKJ30": 2.07,  # （矿机）
}

# 单只矿机饲养成本
nodes_arr_siyang_payment = {  
    "nodeKJ0": 300000,  # （矿机） 金砖
    "nodeKJ1": 1125000,  # （矿机） 金砖
    "nodeKJ2": 2250000,  # （矿机）
    "nodeKJ3": 4500000,  # （矿机）
    "nodeKJ4": 6000000,  # （矿机）
    "nodeKJ5": 15000000,  # （矿机）
    "nodeKJ6": 12000000,  # （矿机）
    "nodeKJ7": 12000000,  # （矿机）
    "nodeKJ8": 12000000,  # （矿机）
    "nodeKJ9": 12000000,  # （矿机）
    "nodeKJ10": 30000000,  # （矿机）
    "nodeKJ11": 15000000,  # （矿机）
    "nodeKJ12": 15000000,  # （矿机）
    "nodeKJ13": 15000000,  # （矿机）
    "nodeKJ14": 15000000,  # （矿机）
    "nodeKJ15": 60000000,  # （矿机）
    "nodeKJ16": 45000000,  # （矿机）
    "nodeKJ17": 45000000,  # （矿机）
    "nodeKJ18": 45000000,  # （矿机）
    "nodeKJ19": 45000000,  # （矿机）
    "nodeKJ20": 90000000,  # （矿机）
    "nodeKJ21": 60000000,  # （矿机）
    "nodeKJ22": 60000000,  # （矿机）
    "nodeKJ23": 60000000,  # （矿机）
    "nodeKJ24": 60000000,  # （矿机）
    "nodeKJ25": 150000000,  # （矿机）
    "nodeKJ26": 90000000,  # （矿机）
    "nodeKJ27": 90000000,  # （矿机）
    "nodeKJ28": 90000000,  # （矿机）
    "nodeKJ29": 90000000,  # （矿机）
    "nodeKJ30": 300000000,  # （矿机）
}

# 每种矿机属性最大饲养只数
nodes_arr_max_siyang_num = {  
    "nodeKJ": 30,  # （矿机）
}

# 直推用户分红 级别->分红比例
zhitui_fenghong = {
    0: 0,
    1: 0.02,
    2: 0.025,
    3: 0.03,
    4: 0.035,
    5: 0.04,
}

# 间推用户分红 级别->分红比例
jiantui_fenghong = {
    0: 0,
    1: 0.01,
    2: 0.013,
    3: 0.015,
    4: 0.018,
    5: 0.02,
}
# 奖金池 楼层对应->分红比例
jiangJinChi_fenghong = {
    5: 0.1,
    10: 0.2,
    15: 0.3,
    20: 0.4,
    25: 0.6,
    # 30: 0.02,
}

# 楼层高度需要注意
lou_ceng_gao_du = {
    0:'0号矿机:',
    1:'1号矿机:直推2人',
    2:'2号矿机:直推2人',
    3:'3号矿机:直推2人',
    4:'4号矿机:直推2人',
    5:'5号矿机:直推2人',
    6:'6号矿机:直推2人',
    7:'7号矿机:直推2人',
    8:'8号矿机:直推2人',
    9:'9号矿机:直推2人',
    10:'10号矿机:直推2人',   
    11:'11号矿机:直推2人',
    12:'12号矿机:直推2人',
    13:'13号矿机:直推2人',
    14:'14号矿机:直推2人',
    15:'15号矿机:直推2人',
    16:'16号矿机:直推2人',
    17:'17号矿机:直推2人',
    18:'18号矿机:直推2人',
    19:'19号矿机:直推2人',
    20:'20号矿机:直推2人',    
    21:'21号矿机:直推2人',
    22:'22号矿机:直推2人',
    23:'23号矿机:直推2人',
    24:'24号矿机:直推2人',
    25:'25号矿机:直推2人',
    26:'26号矿机:直推2人',
    27:'27号矿机:直推2人',
    28:'28号矿机:直推2人',
    29:'29号矿机:直推2人',
    30:'30号矿机:直推2人',     

}

lou_ceng_tu_di = {
    'nodeKJ1': '1级土地1块',
    'nodeKJ2': '2级土地1块',
    'nodeKJ3': '3级土地1块',
    'nodeKJ4': '3级土地1块',
    'nodeKJ5': '3级土地1块',
    'nodeKJ6': '3级土地1块',
    'nodeKJ7': '3级土地1块',
    'nodeKJ8': '3级土地1块',
    'nodeKJ9': '3级土地1块',
    'nodeKJ10': '3级土地1块',
    'nodeKJ11': '3级土地1块',
    'nodeKJ12': '3级土地1块',
    'nodeKJ13': '3级土地1块',
    'nodeKJ14': '3级土地1块',
    'nodeKJ15': '3级土地1块',
    'nodeKJ16': '3级土地1块',
    'nodeKJ17': '3级土地1块',
    'nodeKJ18': '3级土地1块',
    'nodeKJ19': '3级土地1块',
    'nodeKJ20': '3级土地1块',
    'nodeKJ21': '3级土地1块',
    'nodeKJ22': '3级土地1块',
    'nodeKJ23': '3级土地1块',
    'nodeKJ24': '3级土地1块',
    'nodeKJ25': '3级土地1块',
    'nodeKJ26': '3级土地1块',
    'nodeKJ27': '3级土地1块',
    'nodeKJ28': '3级土地1块',
    'nodeKJ29': '3级土地1块',
    'nodeKJ30': '3级土地1块',
}



# 停止矿机激活
#1 根据矿机类型 扣款 2/.购买矿机，保存数据库
@api_view(["POST"])
def buynodeKJStart(request): 
    t_username = request.data.get('username')   
    kuangji = int(request.data.get('kuangji'))     
    now_user = User.objects.filter(username=t_username).first()  # type: Optional[CustomUser] 
    if not now_user:
        return JsonResponse({'valid': False, 'message': '用户不存在'})
      # 得到用户token表
    now_userToken = now_user.usertoken_set.first()     # type: Optional[userToken] 
    if  not now_userToken: 
        return JsonResponse({'valid': False, 'message': '用户token不存在'}) 
    #矿机  
    nowKuangji = tokenZhiYaJiShi.objects.filter(id=kuangji).first()
    if  nowKuangji==None:
        # return JsonResponse({'message': '记录已存在', 'status': 'exists'})
        return JsonResponse({'valid': False, 'message': '号矿机不存在'}) 
   
    #购买n矿机 余额是否足够
    if now_userToken.jzToken<nodes_arr_siyang_payment['nodeKJ'+str(nowKuangji.nodeKjCode)]:
        return JsonResponse({'valid': False, 'message':'用户余额不足'}) 
    # 
   
    try:
        with transaction.atomic():
            #扣除用户燃料包
            # if kuangji != 0:   
            if True:   
                # 扣除卡牌
                if now_user.kapaiA<1:
                    return JsonResponse({'valid': False, 'message': '燃料包不够'})
                # # 直接在数据库层面进行过滤和计数
                # qualified_children_count = now_user.get_children().filter(cengShu__gte=2).count()
                # # 不满足 增加两个 有效人数
                # if kuangji!=1:
                #     list1 = ['',''  ]
                #     if now_user.username not in list1:
                #         if qualified_children_count-now_user.zhiTuiNum<=1:
                #             return JsonResponse({'valid': False, 'message':'不满足增加两个有效人数'})  
                #     now_user.zhiTuiNum= qualified_children_count         #设置当前有效直推人数                         
                now_user.kapaiA=now_user.kapaiA-1                
                now_user.save()
                ebcJiaSuShouYiJiLu.objects.create(
                        uidB=now_user.id,
                        status=1,  
                        fanHuan=1,
                        # liuShuiId=int(value[4][i]),
                        Layer=0, #0代币 充值
                        Remark='扣除燃料包1张'        )
                logger.info('扣除燃料包1张:'+now_user.username ) 
            #扣除用户jz
            now_userToken.jzToken=now_userToken.jzToken-nodes_arr_siyang_payment['nodeKJ'+str(nowKuangji.nodeKjCode)]                   
            now_userToken.save()

            # 记录质押矿机 信息
            nowKuangji.status=0  #启动矿机
            nowKuangji.amountShouYi=0 #收益归零重新计算
            nowKuangji.save()
        
        # 写入记录
            ebcJiaSuShouYiJiLu.objects.create(
                uidB=now_user.id,
                status=1,
                fanHuan=nodes_arr_siyang_payment['nodeKJ'+str(nowKuangji.nodeKjCode)],
                cTime=int(timezone.now().timestamp()),#质押更新时间
                # liuShuiId=int(value[4][i]),
                Layer=0, #质押矿机 
                Remark='重新启动质押:'+str(nowKuangji.nodeKjCode)+'号矿机'  #+config('TOKEN_NAME2', default='') 
            )      
        logger.info('成功重新启动质押:'+str(now_user.username) )
        # 处理分润
        # nodeKjFenRun.FenRunUser(now_user)

        return JsonResponse({'valid': True, 'message': '重新启动质押成功' })
    except Exception as e:
        # 处理异常
        result = ["Failed-everybadyFan", f"ERROR: {e}"]
        print(result)
        logger.info(result)
        return result 


# 购买矿机处理
#1 根据矿机类型 扣款 2/.购买矿机，保存数据库
@api_view(["POST"])
def buynodeKJ(request): 
    t_username = request.data.get('username')   
    kuangji = int(request.data.get('kuangji'))     
    now_user = User.objects.filter(username=t_username).first()  # type: Optional[CustomUser] 
    if not now_user:
        return JsonResponse({'valid': False, 'message': '用户不存在'})
      # 得到用户token表
    now_userToken = now_user.usertoken_set.first()     # type: Optional[userToken] 
    if  not now_userToken: 
        return JsonResponse({'valid': False, 'message': '用户token不存在'}) 
    
    #产看矿机是否已经购买      
    queryset = tokenZhiYaJiShi.objects.filter(uid=now_user, tokenName=str(kuangji) + '号矿机')
    if queryset.exists():
        # return JsonResponse({'message': '记录已存在', 'status': 'exists'})
        return JsonResponse({'valid': False, 'message': str(kuangji) + '号矿机已存在'}) 
    
    #购买n矿机 余额是否足够
    if now_userToken.jzToken<nodes_arr_siyang_payment['nodeKJ'+str(kuangji)]:
        return JsonResponse({'valid': False, 'message':'用户余额不足'}) 
    # 

   
    try:
        with transaction.atomic():

            # 直接在数据库层面进行过滤和计数
            qualified_children_count = now_user.get_children().filter(cengShu__gte=2).count()
             #临时处理 老用户
            if kuangji == 0:   
                if now_user.cengShu==0:
                    now_user.cengShu=1
                    now_user.save()

            #扣除用户燃料包
            if kuangji != 0:   
                # 扣除卡牌
                if now_user.kapaiA<1:
                    return JsonResponse({'valid': False, 'message': '燃料包不够'})
                # 直接在数据库层面进行过滤和计数
                # qualified_children_count = now_user.get_children().filter(cengShu__gte=2).count()
                # qualified_children_count = now_user.get_children().count()
                # 不满足 增加两个 有效人数
                if kuangji!=1:
                    # list1 = ['0xfd9cd5d0cefa797880e1263aa7b705240da58909','0x4b70d2170bf083c89b5bd70289c048c9be783af4'  ]
                    list1 = ['',''  ]
                    if now_user.username not in list1:
                        if qualified_children_count-now_user.zhiTuiNum<=1:
                            return JsonResponse({'valid': False, 'message':'不满足增加两个有效人数'})  
                    now_user.zhiTuiNum= qualified_children_count         #设置当前有效直推人数                         
                now_user.kapaiA=now_user.kapaiA-1
                now_user.cengShu=kuangji+1
                now_user.save()
                ebcJiaSuShouYiJiLu.objects.create(
                        uidB=now_user.id,
                        status=1,  
                        fanHuan=1,
                        # liuShuiId=int(value[4][i]),
                        Layer=0, #0代币 充值
                        Remark='扣除燃料包1张'        )
                logger.info('扣除燃料包1张:'+now_user.username )   
        
          
            # 得到 10% 奖金池
            t_jj10=0
            isjj=False
            if kuangji in [5, 10, 15, 20, 25]:
                now_webid = webInfo.objects.filter(webid=3).first()
                t_jj10=now_webid.jiangJinChi*(jiangJinChi_fenghong[kuangji])
                now_webid.jiangJinChi-=t_jj10
                now_webid.save()    
                isjj=True
            #扣除用户jz
            now_userToken.jzToken=now_userToken.jzToken-nodes_arr_siyang_payment['nodeKJ'+str(kuangji)]
            # 增加奖金池奖金
            now_userToken.jzToken+=t_jj10                 
            now_userToken.save()
            # 需要处理 奖金日志
            if isjj:
                # 写入记录 得到 10% 奖金池
                ebcJiaSuShouYiJiLu.objects.create(
                    uidB=now_user.id,
                    status=1,
                    fanHuan=t_jj10,
                    cTime=int(timezone.now().timestamp()),#质押更新时间
                    # liuShuiId=int(value[4][i]),
                    Layer=11, #得到奖金池 
                    Remark='奖金池奖励:'+str(t_jj10)+' :'+str(int(jiangJinChi_fenghong[kuangji]*100))+'%'  #+config('TOKEN_NAME2', default='') 
                )


            # 记录质押矿机 信息
            new_tokenZhiYaJiShi =tokenZhiYaJiShi.objects.create(
                tokenName=str(kuangji)+'号矿机',
                nodeKjCode=kuangji,
                number=1, #质押台数 1台
                amount=nodes_arr_siyang_payment['nodeKJ'+str(kuangji)],#质押每台额度 
                amountType='jz',#质押使用类型 usdt  jz  mrb
                status=0,
                Layer=0, #0 是矿机  非零 是 各类卡牌
                uid=now_user,
                zhiYaTime=int(timedelta(days=365).total_seconds())   ,     #质押时间
                kaiShiTime=int(timezone.now().timestamp()),#质押开始时间
                uTime=int(timezone.now().timestamp()),#质押更新时间
                Remark=str(now_user.id)+'质押矿机,直推人数:'+str(qualified_children_count)
            )
        
        # 写入记录
            ebcJiaSuShouYiJiLu.objects.create(
                uidB=now_user.id,
                status=1,
                fanHuan=nodes_arr_siyang_payment['nodeKJ'+str(kuangji)],
                cTime=int(timezone.now().timestamp()),#质押更新时间
                # liuShuiId=int(value[4][i]),
                Layer=0, #质押矿机 
                Remark='质押:'+str(kuangji)+'号矿机'  #+config('TOKEN_NAME2', default='') 
            )
          
      
        logger.info('成功质押矿机:'+str(now_user.username) )
        # 处理分润
        # nodeKjFenRun.FenRunUser(now_user)

        return JsonResponse({'valid': True, 'message': '矿机质押成功' })

 
        # isOk,message=nodeKjFenRun.userFenRun(now_user,new_tokenZhiYaJiShi.amount,0,nodes_att_daily_rate['nodeKJ'+str(kuangji)])
        # if isOk:
        #     return JsonResponse({'valid': True, 'message': '矿机质押成功'+'分润成功'})
        # else:
        #     return JsonResponse({'valid': False, 'message':'矿机质押成功'+'分润问题:'+ message})
        
    except Exception as e:
        # 处理异常
        result = ["Failed-everybadyFan", f"ERROR: {e}"]
        print(result)
        logger.info(result)
        # return result 
        return JsonResponse({'valid': False, 'message': {e} })



# 购买燃料包 一次购买1个 100U一个 加入 A卡 1张
#1 根据矿机类型 扣款 2/.购买矿机，保存数据库
@api_view(["POST"])
def buyRanLiaoBao(request): 
    t_username = request.data.get('username')   
    # kuangji = int(request.data.get('kuangji'))     
    now_user = User.objects.filter(username=t_username).first()  # type: Optional[CustomUser] 
    if not now_user:
        return JsonResponse({'valid': False, 'message': '用户不存在'})
      # 得到用户token表
    now_userToken = now_user.usertoken_set.first()     # type: Optional[userToken] 
    if  not now_userToken: 
        return JsonResponse({'valid': False, 'message': '用户token不存在'}) 
    
    # #产看矿机是否已经购买      
    # queryset = tokenZhiYaJiShi.objects.filter(uid=now_user, tokenName=str(kuangji) + '号矿机')
    # if queryset.exists():
    #     # return JsonResponse({'message': '记录已存在', 'status': 'exists'})
    #     return JsonResponse({'valid': False, 'message': str(kuangji) + '号矿机已存在'}) 
    
    #购买n矿机 余额是否足够
    if now_userToken.usdtToken<100:
        return JsonResponse({'valid': False, 'message':'用户USDT不足'}) 
   
    try:
        with transaction.atomic():
           
            #扣除用户usdt
            now_userToken.usdtToken=now_userToken.usdtToken-100
            now_userToken.save()
            # 增加一个燃料包
            now_user.kapaiA+=1   
            now_user.save()     
        
        # 写入记录
            ebcJiaSuShouYiJiLu.objects.create(
                uidB=now_user.id,
                status=1,
                fanHuan=100,
                cTime=int(timezone.now().timestamp()),#质押更新时间
                # liuShuiId=int(value[4][i]),
                Layer=4, # 4.购买燃料包  
                Remark='购买燃料包1个:' #+config('TOKEN_NAME2', default='') 
            )
        logger.info('成功购买燃料包1个:'+str(now_user.username) )
        # 处理分润
        # nodeKjFenRun.FenRunUser(now_user)
        return JsonResponse({'valid': True, 'message': '成功购买燃料包'})
 
        # isOk,message=nodeKjFenRun.userFenRun(now_user,new_tokenZhiYaJiShi.amount,0,nodes_att_daily_rate['nodeKJ'+str(kuangji)])
        # if isOk:
        #     return JsonResponse({'valid': True, 'message': '矿机质押成功'+'分润成功'})
        # else:
        #     return JsonResponse({'valid': False, 'message':'矿机质押成功'+'分润问题:'+ message})
        
    except Exception as e:
        # 处理异常
        result = ["Failed-everybadyFan", f"ERROR: {e}"]
        print(result)
        logger.info(result)
        return result 



class userTokenZhiYaJiShiListView(viewsets.ModelViewSet):
    queryset = tokenZhiYaJiShi.objects.all() 
    serializer_class = tokenZhiYaJiShiSerializer
    # lookup_field = 'uidB'  # 设置使用 username 字段来查找对象 
    # 已经质押矿机列表
    @action(detail=False, methods=['get'] )
    def listkj(self, request):
        # 获取查询参数          zztoken = request.data.get('zztoken')   request.query_params.get('userid', None)

        userid_param = request.query_params.get('userid', None)
        # layer_param = request.query_params.get('layer', None)
        # status_param = request.query_params.get('status', None)
        # 构造过滤条件
        filter_conditions = {}
        if userid_param is not None:
            filter_conditions['uid'] = userid_param
            filter_conditions['Layer'] = 0 #0 代表质押的是矿机
            filter_conditions['status'] = 0 #0 代表质押中 1 以释放
        else:
            return Response("用户名为空")            
        # if layer_param is not None:
        #     filter_conditions['Layer'] = 0 #0 代表质押的是矿机

        # if layer_param is not None:
        #     filter_conditions['Layer'] = 0 #0 代表质押的是矿机    
        # 如果有查询参数，根据条件过滤数据
        if filter_conditions:
            queryset = tokenZhiYaJiShi.objects.filter(**filter_conditions).order_by('-id')
        else:
            # 如果没有查询参数，返回全部数据
            queryset = tokenZhiYaJiShi.objects.all()

        # 序列化数据
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
     # 已经停止质押矿机列表
    @action(detail=False, methods=['get'] )
    def listkjStop(self, request):
        # 获取查询参数          zztoken = request.data.get('zztoken')   request.query_params.get('userid', None)

        userid_param = request.query_params.get('userid', None)
        # layer_param = request.query_params.get('layer', None)
        # status_param = request.query_params.get('status', None)
        # 构造过滤条件
        filter_conditions = {}
        if userid_param is not None:
            filter_conditions['uid'] = userid_param
            filter_conditions['Layer'] = 0 #0 代表质押的是矿机
            filter_conditions['status'] = 1 #0 代表质押中 1 以释放
        else:
            return Response("用户名为空")            
        # if layer_param is not None:
        #     filter_conditions['Layer'] = 0 #0 代表质押的是矿机

        # if layer_param is not None:
        #     filter_conditions['Layer'] = 0 #0 代表质押的是矿机    
        # 如果有查询参数，根据条件过滤数据
        if filter_conditions:
            queryset = tokenZhiYaJiShi.objects.filter(**filter_conditions).order_by('-id')
        else:
            # 如果没有查询参数，返回全部数据
            queryset = tokenZhiYaJiShi.objects.all()

        # 序列化数据
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    


#矿机得到 当日返还
@api_view(["POST"])
@with_lang

def getKJDayFanHuan(request):

    # lang_value = request.headers.get('lang')
    # # zh-TC ,zh-CN,en
    # if lang_value ==None:
    #     lang_value="zh-CN"

            # 直接使用装饰器设置的 lang 值
    lang_value = request.lang   # zh-TC ,zh-CN,en
   

    
    # t_username = request.data.get('username') 
    t_kuangJiId = request.data.get('kuangJiId') 
    
    t_kuangJi = tokenZhiYaJiShi.objects.filter(id=t_kuangJiId).first()

    now_user = User.objects.filter(username=t_kuangJi.uid).first()  
    if not now_user:
        return JsonResponse({'valid': False, 'message': '用户不存在'})
      # 得到用户token表
    now_userToken = now_user.usertoken_set.first()     # type: Optional[userToken] 
    if  not now_userToken: 
        # return JsonResponse({'valid': False, 'message': '用户token不存在'}) 
        return JsonResponse({'valid': False, 'message': get_message(lang_value, 'token_not_exist')})

    

    
    if t_kuangJi.uTime < 1704038400 or t_kuangJi.uTime is None : #时间小于 2024-1-1 日 代表还没有同步到链上时间 
         # logger.info(result)
        return JsonResponse({'valid': False, 'message': "更新时间出错，请联系网管"})
    

    if tokenZhiYaJiShi.get_kuangjiList_by_uid(now_user) != None:
        # logger.info('用户id:'+str(t_parent_id) +t_user.username+'有矿机停止质押,请重新质押' )
        # return JsonResponse({'valid': False, 'message': "有矿机停止质押,请重新质押"})
        return JsonResponse({'valid': False, 'message': get_message(lang_value, 'kuangji_stop')})





    
        # 获取当前时间戳   1711685804
    current_timestamp = int(timezone.now().timestamp())
    print(current_timestamp) 
    if t_kuangJi.uTime > current_timestamp   : #时间小于当前时间 已经领取
        return JsonResponse({'valid': False, 'message': '当日已领取'}) 

    # 矿机限制提现
    if t_kuangJi.statusTiXian==1: # 被限制提现
         # logger.info(result)
        return JsonResponse({'valid': False, 'message': "被限制提现，请联系网管"})
    
   

    if t_kuangJi and t_kuangJi.status == 0 :   # 0 质押中,1已释放
        # isF,t_re=nodeKjFenRun.everybadyFan(t_kuangJi)
        # 矿机 当天收益时间 加一天， 用户得到当日收益 并保存

         # 矿机质押 * 对应利润
        t_liRun=t_kuangJi.amount * nodes_att_daily_rate['nodeKJ'+str(t_kuangJi.nodeKjCode)]/100

         # 返利超过2倍 矿机停止
        if t_kuangJi.amountShouYi ==None:
            t_kuangJi.amountShouYi=0

        if float(t_kuangJi.amountShouYi) > float(t_kuangJi.amount)*3 :
            t_kuangJi.status=1  #1已释放
            t_kuangJi.amountShouYi+=t_liRun
            t_kuangJi.save()
            return JsonResponse({'valid': False, 'message': '矿机质押到期请重新质押'}) 
    



     
        one_day_timestamp = 24 * 60 * 60
        print(one_day_timestamp)
        # t_jiasu15=0
        t_kuangJi.uTime=t_kuangJi.uTime+int(one_day_timestamp)
        t_kuangJi.amountShouYi+=t_liRun
        t_kuangJi.save()

       
        # now_userToken.jzToken+=t_liRun
        # now_userToken.save()

        now_user.fanHuan+=t_liRun
        now_user.save()
           
        # 写入记录     
        t_ebcJiaSuShouYiJiLu=ebcJiaSuShouYiJiLu ()
        # t_ebcJiaSuShouYiJiLu.uidA=t_user   #发送方
        t_ebcJiaSuShouYiJiLu.uidB=now_user.id  # 接收方
        t_ebcJiaSuShouYiJiLu.status=1  #已转
        t_ebcJiaSuShouYiJiLu.Layer=3  #提现到账 日志        
        t_ebcJiaSuShouYiJiLu.fanHuan=t_liRun
        t_ebcJiaSuShouYiJiLu.Remark='当日反润'+str(t_liRun )
        t_ebcJiaSuShouYiJiLu.save() 

        isOk,message=nodeKjFenRun.userFenRun(now_user,t_liRun,1,nodes_att_daily_rate['nodeKJ'+str(t_kuangJi.nodeKjCode)])

        if isOk:
            return JsonResponse({'valid': True, 'message': '当日反润成功'+'分润成功'})
        else:
            return JsonResponse({'valid': False, 'message':'当日反润成功'+ message}) 
    else:
        return JsonResponse({'valid': False, 'message': '矿机已结束质押'})


SECRET_KEY = '0x9ba61124ddeb2c0c444ac5b643833bf24421d97eed3c9ede44a771319054bc9d'

# @api_view(["POST"])
# def generate_signature(request):
#     user_address = request.data.get('username')
#     amount = request.data.get('amount')
#     timestamp = int(time.time())
#     data = f"{user_address}{amount}{timestamp}"
#     signature = hmac.new(SECRET_KEY.encode(), data.encode(), hashlib.sha256).hexdigest()
    
#     result = [signature, timestamp]
#     return JsonResponse({'valid': True, 'message': result}) 

#     return signature, timestamp


# 提现
@api_view(["POST"])
def generate_signature(request):
    user_address = request.data.get('username')
    amount = int(request.data.get('amount'))
    timestamp = int(time.time())

     # 确保 amount 是正整数且不为零
    try:
        amount = int(amount)
        if amount <= 0:
            return JsonResponse({'valid': False, 'message': 'Amount 必须大于0'})
    except ValueError:
        return JsonResponse({'valid': False, 'message': 'Amount 必须为 integer'})


    try:

        now_user = User.objects.filter(username=user_address).first()   # type: Optional[CustomUser] 
        if not now_user:
            return JsonResponse({'valid': False, 'message': '用户不存在'})
        # 得到用户token表
        now_userToken = now_user.usertoken_set.first()     # type: Optional[userToken] 
        if  not now_userToken: 
            return JsonResponse({'valid': False, 'message': '用户token不存在'}) 
        

        # amount10 = float(amount) / (10 ** 18)
        # if amount10 > now_userToken.jzToken:
        #     return JsonResponse({'valid': False, 'message': '余额不足'}) 

        amount10 = float(amount) / (10 ** 18)
        if amount10 > float(now_user.fanHuan):
            return JsonResponse({'valid': False, 'message': '可返还余额不足'}) 

        # 个别限制 用户状态
        if now_user.statusTiXian==1:
            return JsonResponse({'valid': False, 'message': ''})



        # 将地址编码为bytes 
        user_addressCheck=Web3.to_checksum_address(user_address)   

        encoded_data = eth_abi.encode(['address', 'uint256', 'uint256'], [user_addressCheck, amount, timestamp])   
    
        # encoded_data = eth_abi.encode([ 'uint256','uint256'], [ amount,timestamp])    
        # 使用 Keccak256 进行哈希
        hasher = keccak.new(digest_bits=256)
        hasher.update(encoded_data)
        message_hash = hasher.digest()
        message_hash_hex = message_hash.hex() 
        print(f"Python 生成的 message_hash: {message_hash_hex}")
        # 使用生成的私钥
        private_key = '0x9ba61124ddeb2c0c444ac5b643833bf24421d97eed3c9ede44a771319054bc9d'
        signed_message = Account.sign_message(encode_defunct(hexstr=message_hash_hex), private_key)

        signature = signed_message.signature.hex()


    


        # 写入记录     
        t_payToken=payToken ()
        # t_payToken.uidA=t_user   #发送方
        t_payToken.uidB=now_user.id  # 接收方
        t_payToken.status=0  # 
        t_payToken.Layer=0        
        t_payToken.amount=amount10
        t_payToken.tiXianWallter=user_address
        t_payToken.HashId=message_hash_hex
        t_payToken.Remark='用户提现'    
        t_payToken.save()  
        # 扣费
        now_user.fanHuan-=amount10
        now_user.save()
        # now_userToken.jzToken-=amount10
        # now_userToken.save()
        # 10% 记录到 奖金池
        # 计入奖金池
        now_webid = webInfo.objects.filter(webid=3).first()     

        
        now_webid.jiangJinChi=now_webid.jiangJinChi+(amount10*0.1)
        now_webid.save()

        result = {
            'signature': signature,
            'timestamp': timestamp,
            'hash': message_hash_hex
        }        
        return JsonResponse({'valid': True, 'message': result})
    except Exception as e:
        # 处理异常
        result = ["Failed-everybadyFan", f"ERROR: {e}"]      
        logger.info(result)
        return JsonResponse({'valid': False, 'message': result})  




@api_view(["POST"])
def verify_signature(request):
    # 从请求中获取数据
    user_address = request.data.get('username')
    amount = int(request.data.get('amount'))
    timestamp = int(request.data.get('timestamp'))
    signature = request.data.get('signature')

    # user_address='0x606adb6c2b7d415e0fd58b7d9cff6b71e5139ceb'
    user_address=Web3.to_checksum_address(user_address)   


    # 使用 eth_abi 编码数据
    encoded_data = eth_abi.encode(['address'],['uint256', 'uint256'], [user_address, amount, timestamp])
    
    # 使用 Keccak256 进行哈希
    hasher = keccak.new(digest_bits=256)
    hasher.update(encoded_data)
    message_hash = hasher.digest()
    message_hash_hex = message_hash.hex()
    print(f"Python 生成的 message_hash: {message_hash_hex}")

    # 构建签名消息
    eth_signed_message = encode_defunct(hexstr=message_hash_hex)

    # 使用公钥验证签名
    recovered_address = Account.recover_message(eth_signed_message, signature=signature)

    # 预期的签名者地址
    expected_address = '0x1C4329990c5E14d74e13ACF68815d45b130ae225'

    # 验证签名是否有效
    valid_signature = (recovered_address.lower() == expected_address.lower())

    result = {
        'valid_signature': valid_signature,
        'recovered_address': recovered_address,
        'expected_address': expected_address,
        'hash': message_hash_hex
    }

    return JsonResponse({'valid': valid_signature, 'message': result})



 

@api_view(["GET"])
def generate_key(request):

    account = Account.create()
    private_key = account.key.hex()  # 使用 'key' 而不是 'privateKey'
    address = account.address
    
    result = {
        'private_key': private_key,
        'address': address
    }

    # account = Account.create()
    # private_key = account.privateKey.hex()
    # address = account.address
    
    # result = {
    #     'private_key': private_key,
    #     'address': address
    # }
    
    return JsonResponse({'valid': True, 'message': result})



def fanTiXian(request):
    id = request.GET.get('id','')
    t_payToken=payToken.objects.filter(id=id ).order_by('-id').first()    
    if not payToken==None:
        now_user = User.objects.filter(id=t_payToken.uidB).first()  # type: Optional[CustomUser]
        if not now_user:
            return JsonResponse({'valid': False, 'message': '用户不存在'})
        # 得到用户token表
        # now_userToken = now_user.usertoken_set.first()     # type: Optional[userToken] 
        # if  not now_userToken: 
        #     return JsonResponse({'valid': False, 'message': '用户token不存在'}) 
        
        # 用户返款
        now_user.fanHuan+=t_payToken.amount
        now_user.save()
        t_payToken.status=1 #返还 提现
        t_payToken.Remark+='-提现退回'
        t_payToken.save()
    return redirect('/admin/reg/paytoken/') 
