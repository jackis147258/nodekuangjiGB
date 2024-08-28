
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

from app1.models import TcSearch,webInfo
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
from .models import CustomUser,ebcJiaSuShouYiJiLu ,tokenZhiYaJiShi,payToken,userToken
from .  import ebcFenRun  ,ebcUserTuichu 
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

from django.utils import timezone
from typing import Optional
from .decorators import with_lang


"""四、 DRF的视图集viewsets"""


class TcSearchViewSet(viewsets.ModelViewSet):
    queryset = TcSearch.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    # def perform_create(self, serializer):
    #     serializer.save(teacher=self.request.user)

@api_view(["GET", "POST"])
def get_user(request):
    if request.method == 'GET':
        usid = request.GET.get('usid','')
        if usid=='':
            return JsonResponse({'code':100101,'msg':'用户id不能为空'})
        if usid=='1':
            return JsonResponse({'code':100200,'msg':'查询成功','data':{'usid':1,'name':'james','age':36}})
        else:
            return JsonResponse({'code':100102,'msg':'未查询到用户数据'})

    else:
        return JsonResponse({'code': 100103, 'msg': '请求方法错误'})





"""一、 函数式编程 Function Based View"""





class CourseList(APIView):
    permission_classes = (IsAuthenticated,)  # settings.py中已设置，此处是多余的

    def get(self, request):
        """
        :param request:
        :return:
        """
        queryset = TcSearch.objects.all()
        s = CourseSerializer(instance=queryset, many=True)  # 这里是instance = xx
        # s = CourseSerializer(instance=queryset.first())
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        :param request:
        :return:
        """
        s = CourseSerializer(data=request.data)  # 这里是data = xx, return前要先调用.is_valid()
        if s.is_valid():
            s.save()
            # 分别是<class 'django.http.request.QueryDict'> <class 'rest_framework.utils.serializer_helpers.ReturnDict'>
            print(type(request.data), type(s.data))
            return Response(data=s.data, status=status.HTTP_201_CREATED)
        return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)

def ifToken(zztoken):
    return True

# @api_view(["GET","POST"])

# @authentication_classes((BasicAuthentication, SessionAuthentication, TokenAuthentication))
# @permission_classes((IsAuthenticated,))
@api_view(["POST"])
def ifTokenApi(request):
    """
    获取所有课程信息或新增一个课程
    :param request:
    :return:
    """
    if request.method == "POST":        
        zztoken = request.data.get('zztoken') 
        # data = request.json()
        # zztoken = data.get('zztoken', 'your-default-token-value')       
       

        # 在这里进行 zztoken 的验证逻辑
        if ifToken(zztoken):
            return JsonResponse({'valid': True, 'message': 'ok token 可以'})
        else:
            return JsonResponse({'valid': False, 'message': 'Invalid zztoken'})

        return JsonResponse({'error': 'Invalid request method'})

# 处理 Ebc 定时计算
@api_view(["POST"])
def ebc1(request):
    """
    获取所有课程信息或新增一个课程
    :param request:
    :return:
    """
    if request.method == "POST":        
        zztoken = request.data.get('zztoken') 
        # data = request.json()
        # zztoken = data.get('zztoken', 'your-default-token-value')       
       

        # 在这里进行 zztoken 的验证逻辑
        if ifToken(zztoken):
            return JsonResponse({'valid': True, 'message': 'ok token 可以'})
        else:
            return JsonResponse({'valid': False, 'message': 'Invalid zztoken'})

        return JsonResponse({'error': 'Invalid request method'})

 
# 接口 Ebc 方面  CustomUser,ebcJiaSuShouYiJiLu

# @permission_classes((IsAuthenticated,))
# class CustomUserListCreateView(generics.ListCreateAPIView):

class CustomUserListCreateView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'username'  # 设置使用 username 字段来查找对象


# 处理GET 事件
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            lang_value = request.headers.get('lang')  # 从请求头中获取 lang 值
            serializer = self.get_serializer(instance, context={'lang': lang_value})
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)


    # 不起作用
    def get(self, request, *args, **kwargs):
        try:
            lang_value = request.lang   # zh-TC ,zh-CN,en
            instance = self.get_object()         
            lang_value = request.headers.get('lang')  # 从请求头中获取 lang 值
            serializer = self.get_serializer(instance, context={'lang': lang_value})

            return Response(serializer.data)
        except instance.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

    
    # 这个视图对应的路径是 /customusers/{pk}/custom_detail_view/，其中 {pk} 是用户的主键
    @action(detail=True, methods=['get'])
    def custom_detail_view(self, request, pk=None):
        custom_user = self.get_object()
        # 在这里添加自定义逻辑，例如返回特定信息
        data = {'custom_detail_info': 'Some custom information'}
        return Response(data)
    

class ebcJiaSuShouYiJiLuView(viewsets.ModelViewSet):
    queryset = ebcJiaSuShouYiJiLu.objects.all()
    serializer_class = ebcJiaSuShouYiJiLuSerializer
    # lookup_field = 'uidB'  # 设置使用 username 字段来查找对象 
    
    @action(detail=False, methods=['get'] )
    def listlog(self, request):
        # 获取查询参数          zztoken = request.data.get('zztoken')   request.query_params.get('userid', None)

        userid_param = request.query_params.get('userid', None)
        layer_param = request.query_params.get('layer', None)

        # 构造过滤条件
        filter_conditions = {}
        if userid_param is not None:
            filter_conditions['uidB'] = userid_param
        if layer_param is not None:
            filter_conditions['Layer'] = layer_param

        # 如果有查询参数，根据条件过滤数据
        if filter_conditions:
            queryset = ebcJiaSuShouYiJiLu.objects.filter(**filter_conditions).order_by('-id')
        else:
            # 如果没有查询参数，返回全部数据
            queryset = ebcJiaSuShouYiJiLu.objects.all()

        # 序列化数据
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    


class ebcPayTokenView(viewsets.ModelViewSet):
    queryset = payToken.objects.all()
    serializer_class =  payTokenSerializer
    # lookup_field = 'uidB'  # 设置使用 username 字段来查找对象 
    
    @action(detail=False, methods=['get'] )
    def listlog(self, request):
        # 获取查询参数          zztoken = request.data.get('zztoken')   request.query_params.get('userid', None)

        userid_param = request.query_params.get('userid', None)
        layer_param = request.query_params.get('layer', None)
        status_param = request.query_params.get('status', None)

        # 构造过滤条件
        filter_conditions = {}
        if userid_param is not None:
            filter_conditions['uidB'] = userid_param
        if layer_param is not None:
            filter_conditions['Layer'] = layer_param
        if status_param is not None:
            filter_conditions['status'] = status_param

        # 如果有查询参数，根据条件过滤数据
        if filter_conditions:
            queryset = payToken.objects.filter(**filter_conditions)
        else:
            # 如果没有查询参数，返回全部数据
            queryset = payToken.objects.all()

        # 序列化数据
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
    # 这个视图对应的路径是 /customusers/{pk}/custom_detail_view/，其中 {pk} 是用户的主键
    @action(detail=True, methods=['get'])
    def custom_detail_view(self, request, pk=None):
        custom_user = self.get_object()
        # 在这里添加自定义逻辑，例如返回特定信息
        data = {'custom_detail_info': 'Some custom information'}
        return Response(data)


# class ebcJiaSuShouYiJiLuListCreateView(generics.ListCreateAPIView):
#     queryset = ebcJiaSuShouYiJiLu.objects.all()
#     serializer_class = ebcJiaSuShouYiJiLuSerializer

@api_view(["POST"])
def getDayFanHuan(request):
    
    t_username = request.data.get('username') 
    
    t_user = User.objects.filter(username=t_username).first()
    
    if t_user.EbcLastFanHuan_at < 1704038400 or t_user.EbcLastFanHuan_at is None : #时间小于 2024-1-1 日 代表还没有同步到链上时间 
        result = ["Failed", f"等待链上同步处理"]
        # logger.info(result)
        return JsonResponse({'valid': False, 'message': t_re})

    if t_user and t_user.status == 1 :   # 1 表示 质押状态
        isF,t_re=ebcFenRun.everybadyFan(t_user)
        #当天成功返还
        if isF:
            # t_user.status=0
            # t_user.save()
            result = ["success", f"用户修改状态"]
            logger.info(result)
            ebcFenRun.FenRunUser(t_user)
            # ebcFenRun.userFenRun(t_user)
            return JsonResponse({'valid': True, 'message': t_re})
        else:
            result = ["Failed", f"用户日返回失败"]
            logger.info(result)
            return JsonResponse({'valid': False, 'message': t_re})
            
    else:
        return JsonResponse({'valid': False, 'message': t_re})
    

@api_view(["POST"])
def ebcTiXian(request):
    
    # return JsonResponse({'valid': True, 'message': '临时暂定'})
    amount = int(request.data.get('amount') )
    tiXianWallter = request.data.get('tixianwallter')     
    if(amount<=0):
        return JsonResponse({'valid': True, 'message': '不能为0'}) 
    
    now_user = User.objects.filter(username=tiXianWallter).first()
    if now_user:
        # if now_user.fanHuan<0 or now_user.fanHuan<Decimal(amount): 
        if now_user.fanHuan<=0  :
           
            return JsonResponse({'valid': True, 'message': '返回金额小于0'}) 
        if now_user.userStakesBfanHuan<=0:
             
            return JsonResponse({'valid': True, 'message': '返还余额小于0'})  
        # 如果提现金额 大于 可返回 ，amount  为 可返还 最大值
        if now_user.userStakesBfanHuan<=amount:
            amount=now_user.userStakesBfanHuan 
        
         # 写入记录     
        t_payToken=payToken ()
        # t_payToken.uidA=t_user   #发送方
        t_payToken.uidB=now_user.id  # 接收方
        t_payToken.status=3  # 已到账
        t_payToken.Layer=0        
        t_payToken.amount=amount
        t_payToken.tiXianWallter=tiXianWallter
        t_payToken.Remark='用户提现'    
        t_payToken.save()  
        
        # 扣费
        ebcFenRun.tiXianOksql(t_payToken.amount,t_payToken.tiXianWallter)
        return JsonResponse({'valid': True, 'message': '已提交'})
    
        # ebc 合约地址
        # contractTokenAddress=EbcContractTokenAddress
        # t_re=dfEbcTixian(int(amount),tiXianWallter,contractTokenAddress)        
        # if '成功转入:' in t_re[1]:
        #     t_ebcJiaSuShouYiJiLu.Remark+="-提现成功"
        #     t_ebcJiaSuShouYiJiLu.save() 
        #     if ebcFenRun.tiXianOksql(amount,tiXianWallter):
        #         t_ebcJiaSuShouYiJiLu.Remark+="-减少数据成功"
        #         t_ebcJiaSuShouYiJiLu.status=1  #已转
        #         t_ebcJiaSuShouYiJiLu.save() 
        #         print("包含成功转入")
        #         return JsonResponse({'valid': True, 'message': t_re})
        #     else:
        #         t_ebcJiaSuShouYiJiLu.Remark+="-减少数据失败"
        #         t_ebcJiaSuShouYiJiLu.save() 
        #         print("包含成功转入")
        #         return JsonResponse({'valid': True, 'message': t_re})                
        # else:
        #     t_ebcJiaSuShouYiJiLu.Remark+=''.join(t_re)
        #     t_ebcJiaSuShouYiJiLu.status=0  #失败
        #     t_ebcJiaSuShouYiJiLu.save() 
        #     return JsonResponse({'valid': False, 'message': t_re})
    else:
        return JsonResponse({'valid': False, 'message': '用户不存在'})
        

@api_view(["POST"])
def ebcTuanDui(request):    
    t_username = request.data.get('username')       
    t_is,t_js =ebcFenRun.tuanDuiRenShu(t_username) 
    if t_js :
        return JsonResponse(t_js,safe=False)

@api_view(["POST"])
def ebcUserTuiChuView(request):    
    t_username = request.data.get('username')      
    # 合约退出  
    # msg =ebcUserTuichu.userTuichu(t_username) 
    
    # 数据库改变状态
    now_user = User.objects.filter(username=t_username).first()
    if now_user:
    # if now_user.fanHuan<0 or now_user.fanHuan<Decimal(amount): 
        now_user.status=0
        now_user.save()        
        return JsonResponse({'valid': True, 'message': '成功退出'})    
        # result = ["ok-userTuichu", f"msg:成功退出 "]
    else:         
       return JsonResponse({'valid': False, 'message': '用户不存在'})    
    
    
    # return JsonResponse(msg)
    



class tokenZhiYaJiShiView(viewsets.ModelViewSet):
    queryset = tokenZhiYaJiShi.objects.all() 
    serializer_class = tokenZhiYaJiShiSerializer
    # lookup_field = 'uidB'  # 设置使用 username 字段来查找对象 
    
    @action(detail=False, methods=['get'] )
    def listlog(self, request):
        # 获取查询参数          zztoken = request.data.get('zztoken')   request.query_params.get('userid', None)

        userid_param = request.query_params.get('userid', None)
        # layer_param = request.query_params.get('layer', None)

        # 构造过滤条件
        filter_conditions = {}
        if userid_param is not None:
            filter_conditions['uid'] = userid_param
        else:
            return Response("用户名为空")
            
        # if layer_param is not None:
        #     filter_conditions['Layer'] = layer_param
        
     

        # 如果有查询参数，根据条件过滤数据
        if filter_conditions:
            queryset = tokenZhiYaJiShi.objects.filter(**filter_conditions).order_by('-id')
        else:
            # 如果没有查询参数，返回全部数据
            queryset = tokenZhiYaJiShi.objects.all()

        # 序列化数据
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# 改变用户父级
def changFuLeiview(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        fuid = request.POST.get('fuid')
        t_pass = request.POST.get('fuids')

        if t_pass != '147258':       
            return JsonResponse({'valid': True, 'message': '。。。。'})    
        
        # 在这里执行你的自定义操作，使用 parameter
        # 获取要修改的节点实例
        userid_modify = User.objects.get(id=userid)

        # 修改节点的父节点
        fuid_node = User.objects.get(id=fuid)        
        
        sss=fuid_node.get_children()  
        
        userid_modify.move_to(fuid_node)

        # fuid_node.moveto()
        # userid_modify.parent = fuid_node

        # # 保存更改
        # userid_modify.save()
        
        
        # 获取要移动的节点和新的父节点
        # node_to_move = YourModel.objects.get(id=1)
        # new_parent = YourModel.objects.get(id=2)

        # 将节点移动到新的位置（作为新父节点的最后一个子节点）
        # move_to(userid_modify, fuid_node)



        # return HttpResponse(f'Custom Action Executed with Parameter: {parameter}')

    return render(request, 'changFuLei.html')
    # return render(request, 'signup.html', {'form': form})

    
# 测试接口
@api_view(["POST"])
def ebcTest(request):    
    t_username = request.data.get('username')       
    t_js =ebcFenRun.FenRun() 
    # t_is,t_js =ebcFenRun.FenRun() 
    if t_js :
        return JsonResponse(t_js)
    

# 注册用户
@api_view(["POST"])
def regUser(request):    
    t_username = request.data.get('username')  
    
    
    now_user = User.objects.filter(username=t_username).first()
    if now_user:
        serializer = CustomUserSerializer(now_user)  # 使用 CustomUserSerializer 对象序列化用户对象
        serialized_data = serializer.data  # 获取序列化后的数据

        # 判断用户token 是否存在 不存在 补充
        now_userToken = now_user.usertoken_set.first()     # type: Optional[userToken] 
        if  not now_userToken: 
            current_timestamp = int(timezone.now().timestamp())
            now_userToken = userToken.objects.create(uid=now_user,cTime=current_timestamp)
            # return JsonResponse({'valid': False, 'message': '用户token不存在'}) 
        
        return Response(serialized_data)  # 返回序列化后的 JSON 数据
        # return JsonResponse({'valid': False, 'message': '用户存在'})
    
    new_user = CustomUser()    
    new_user.is_active=True #是否激活状态
    new_user.is_staff=True #是否工作人员状态 是否可登录后台
    
    new_user.username=t_username
    new_user.password=make_password('147258')
    # new_user.parent_id=parentId               
    new_user.status=0                  
    # 保存用户
    new_user.save()
        # Add the user to the 'your_custom_group' group
    your_custom_group = Group.objects.get(name='ebc')
    new_user.groups.set([your_custom_group])

    # 创建 userToken
     # 创建关联的 userToken
    
    current_timestamp = int(timezone.now().timestamp())
    now_userToken = userToken.objects.create(uid=new_user,cTime=current_timestamp)
    
    serializer = CustomUserSerializer(new_user)  # 使用 CustomUserSerializer 对象序列化用户对象
    serialized_data = serializer.data  # 获取序列化后的数据
    return Response(serialized_data)  # 返回序列化后的 JSON 数据
    
    # return JsonResponse({'valid': True, 'message': '用户注册成功'})

    # if t_js :
    #     return JsonResponse(t_js,safe=False)

   
# 检查 卡牌是否足够
@api_view(["POST"])
def isKapai(request):    
    t_username = request.data.get('username')   
    kuangji = int(request.data.get('kuangji'))

     
    now_user = User.objects.filter(username=t_username).first()   
    

    if not now_user:
        return JsonResponse({'valid': False, 'message': '用户不存在'}) 
    
    # if now_user.status==1:
    #     return JsonResponse({'valid': False, 'message': '矿机正在运行中'}) 
    
    if kuangji==2000:
        if now_user.kapaiA>=1:
            now_user.kapaiA=now_user.kapaiA-1
            now_user.status=1          #改变状态 1 不可以在次购买矿机          
            now_user.save()
            ebcJiaSuShouYiJiLu.objects.create(
                    uidB=now_user.id,
                    status=1,  
                    fanHuan=1,
                    # liuShuiId=int(value[4][i]),
                    Layer=0, #0代币 充值
                    Remark='扣除A卡牌1张'        )
            logger.info('扣除A卡牌1张:'+now_user.username )            
            return JsonResponse({'valid': True, 'message': '成功'}) 
        else:
            return JsonResponse({'valid': False, 'message': '卡牌不够'}) 
    if kuangji==4000:
        if now_user.kapaiB>=1:
            now_user.kapaiB=now_user.kapaiB-1
            now_user.status=1          #改变状态 1 不可以在次购买矿机          
            now_user.save()
            ebcJiaSuShouYiJiLu.objects.create(
                uidB=now_user.id,
                status=1,  
                fanHuan=1,
                # liuShuiId=int(value[4][i]),
                Layer=0, #0代币 充值
                Remark='扣除B卡牌1张'        )
            logger.info('扣除B卡牌1张: '+now_user.username )          

            return JsonResponse({'valid': True, 'message': '成功'}) 
        else:
            return JsonResponse({'valid': False, 'message': '卡牌不够'}) 
        
    if kuangji==6000:
        if now_user.kapaiC>=1:
            now_user.kapaiC=now_user.kapaiC-1
            now_user.status=1          #改变状态 1 不可以在次购买矿机          
            now_user.save()
            ebcJiaSuShouYiJiLu.objects.create(
                uidB=now_user.id,
                status=1,  
                fanHuan=1,
                # liuShuiId=int(value[4][i]),
                Layer=0, #0代币 充值
                Remark='扣除C卡牌1张'        )
            logger.info('扣除C卡牌1张:'+now_user.username )       

            return JsonResponse({'valid': True, 'message': '成功'}) 
        else:
            return JsonResponse({'valid': False, 'message': '卡牌不够'}) 
    return JsonResponse({'valid': False, 'message': '参数不正确'}) 

# 修改父节点
@api_view(["POST"])
def setUserParent(request):
    if request.method == 'POST':
        fuid = request.POST.get('fuid') 
        
        t_username = request.data.get('username')  
    
    
        # now_user = User.objects.filter(username=t_username).first()
    
        userid_modify = User.objects.filter(username=t_username).first() 
        # userid_modify = User.objects.get(id=userid) 
        # 修改节点的父节点
        # fuid_node = User.objects.get(id=fuid)      
        try:
            fuid_node = User.objects.get(id=fuid)
        except User.DoesNotExist:
            # 处理用户不存在的情况，可以返回错误信息或者执行其他逻辑
            print("用户不存在")
            # 可以选择返回特定的响应，或者抛出自定义的异常
            # raise CustomException("用户不存在")
            # 或者直接返回错误信息给前端
            return JsonResponse({'valid': False, 'message': '推荐码不存在'}) 

        
        if userid_modify and fuid_node:   
        # sss=fuid_node.get_children()   
            userid_modify.move_to(fuid_node)   
            now_user = User.objects.filter(username=t_username).first()
            return JsonResponse({'valid': True, 'message': '成功'}) 

        # if now_user:
        #     now_user.parent_id=fuid     
        #     now_user.save()       
        #     return JsonResponse({'valid': True, 'message': '成功'}) 
        
        return JsonResponse({'valid': False, 'message': '用户不存在'}) 

        
        
        
        # 在这里执行你的自定义操作，使用 parameter
        # 获取要修改的节点实例
        # userid_modify = User.objects.get(id=userid)

        # # 修改节点的父节点
        # fuid_node = User.objects.get(id=fuid)        
        
        # sss=fuid_node.get_children()  
        
        # userid_modify.move_to(fuid_node)



# 注册用户
@api_view(["POST"])
def webInfoView(request):    
    # t_username = request.data.get('username') 
    
    webid = request.data.get('webid') 

    
    # now_webid = webInfo.objects.get(id=webid)  
    now_webid = webInfo.objects.filter(webid=webid).first()     

    
    
    if now_webid:
        serializer = webInfoSerializer(now_webid)  # 使用 CustomUserSerializer 对象序列化用户对象
        serialized_data = serializer.data  # 获取序列化后的数据
        
        return Response(serialized_data)  # 返回序列化后的 JSON 数据
    


@api_view(["POST"])
def ebcTiXianMatic(request):    
    # return JsonResponse({'valid': True, 'message': '临时暂定'})
    # amount = int(request.data.get('amount') )
    amount = 0
    amount_param = request.data.get('amount')
    if amount_param is not None  and amount_param !='NaN':
        amount = float(amount_param)
    
    tiXianWallter = request.data.get('tixianwallter')     
    if(amount<=0):
        return JsonResponse({'valid': False, 'message': '不能为0'}) 
    
    now_user = User.objects.filter(username=tiXianWallter).first()
    if now_user:
        # if now_user.fanHuan<0 or now_user.fanHuan<Decimal(amount): 
        if now_user.fanHuan<=0  :           
            return JsonResponse({'valid': False, 'message': '返回金额小于0'}) 
       
        # 判断 总共要返还的数量小于 要返还的数量 那么取走剩余。重置用户.
        if now_user.userStakesBfanHuan<amount:
            amount=now_user.userStakesBfanHuan            
        # now_user.fanHuan=now_user.fanHuan-Decimal(amount)
        now_user.fanHuan=0
        now_user.userStakesBfanHuan=now_user.userStakesBfanHuan-amount
        now_user.save()
    
         # 写入记录     
        t_payToken=payToken ()
        # t_payToken.uidA=t_user   #发送方
        t_payToken.uidB=now_user.id  # 接收方
        t_payToken.status=0  # 
        t_payToken.Layer=0        
        t_payToken.amount=amount
        t_payToken.tiXianWallter=tiXianWallter
        t_payToken.Remark='用户提现'    
        t_payToken.save()  
        
        # 扣费
        ebcFenRun.tiXianOksql(t_payToken.amount,t_payToken.tiXianWallter)
        return JsonResponse({'valid': True, 'message': '按照流程操作中途不要退出'})
    
      
    else:
        return JsonResponse({'valid': False, 'message': '用户不存在'})
    

# @api_view(["POST"])
# def showMaticBalances(request):  
      