from django.shortcuts import redirect,reverse,render
from django.http import HttpResponse

from django import forms
from app1 import models
from app1.myFroms import infoFrom

from app1 import viewFunc 
from django.contrib.auth import logout

from rest_framework.decorators import api_view
import json
from django.http import JsonResponse
from  app1.until import tools ,denglu
from app1.tasks import taskQuantify,taskQuantifyPrice,taskQuantifyBuySell
from app1.models import T_task,T_Quantify1,CategoryToken ,T_TokenAddr,T_TokenAddrBak #保存 task id 以后删除
import datetime
from celery.app.control import Control
from moon39.celery   import app

from apiV1.DeFi2 import DeFi2,createWallet
from django.db import transaction
from django.http import HttpResponseRedirect


BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)



def sprots():
    str = '26+23+16+28+11+18+9+17+24+21+27+14+10+56+57+3+8+25+6+5+7+32+29+30+2+43+44+34+39+48+59+47+49+46+45+36+33+40+42+41+37+35+38+63+4+55+60+31+22+0+1+64+20+61+62+51+50+15+53+54+58+19+12+13'
    arr = str.split('+')
    return arr


class Myfrom2(forms.Form):
    user=forms.CharField(label="name",max_length=100)
    sex=forms.CheckboxInput()
    password = forms.CharField(max_length=32, label="密码",widget=forms.PasswordInput())
   
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
def info_user1(request):
    # infoData=myFroms.Myfrom()  
    if request.method=="GET":
        infoData=Myfrom2() 
        models.TcWeb.objects.create(name="dk12")
        return render(request,"info.html",{"form":infoData})
    form=Myfrom2(data=request.POST)
    if form.is_valid():
        # form.save()
        # return redirect('/list')
        return render(request,"info.html",{"form":form})
    
    return render(request,"info.html",{"form":form})

def dashboard1(request):
     user_count =5
     task_count = 6

     userId=request.session.get('_auth_user_id')
 
     context = { 'user_count': user_count, 'task_count': task_count }
     return render(request, 'dashboard.html',context)

def che(request):
    if request.method=="POST":
        check_box_list = request.POST.getlist('check_box_list')
        if check_box_list:
            print(check_box_list)
            return HttpResponse("ok")
        else:
            print("fail")
            return HttpResponse("fail")
    else:
        userId=request.session.get('_auth_user_id')
        a = [1,2,3,userId]
        return render(request,'che.html',{'a':a})

def layout(request):
     user_count =5
     task_count = 6

     userId=request.session.get('_auth_user_id')
 
     context = { 'user_count': user_count, 'task_count': task_count }
     return render(request, 'layout.html',context)

def info(request):
    # infoData=myFroms.Myfrom()
    if request.method=="GET":     
        
        #判断当前访客是否登录
        if not request.user.is_authenticated:            
            return redirect(reverse('logout'))
        userId=request.session.get('_auth_user_id')
        # models.TcSearch.objects.create(paiXu="paiXu2",menOneTwo="2")
        # row_object=models.TcSearch.objects.filter(uid=userId)         
        # 如果不存在新建一个用户查询记录
        # result.count() == 0:
        # if  row_object.exists():
        # if  row_object.count() == 0:  
        #     tcSearch=models.TcSearch()
        #     tcSearch.uid=userId
        #     tcSearch.save()
        # infoData=infoFrom(instance=row_object.first()) 
        # models.TcWeb.objects.create(name="dk12")        
        # return render(request,"index.html",{"form":infoData})
        return render(request,"index.html")
        # return render(request,"info.html",{"form":infoData})
    # post 提交 1.保存 Tcsearch 变量，2.搜索
    if request.method=="POST":
        userId=request.session.get('_auth_user_id')
        row_object=models.TcSearch.objects.filter(uid=userId)   
        form=infoFrom(data=request.POST,instance=row_object.first())
        if form.is_valid():
            form.save()
            # 组合搜索按钮
            params =viewFunc.searchStr(userId)
            # 转成 url 转义
            # result = urlencode(params)
            # # get 出去 得到返回值
            # url = "https://zh.surebet.com/surebets?"
            # url=url+result
            # listUrl=get.getUrlList(url)
            # print(listUrl)            
            # return redirect('/list')
            return render(request,"index.html",{"form":form,"tableInfo":params})
    return render(request,"info.html",{"form":form})


# @api_view(['POST'])
def logout_view(request):    
    logout(request)
    request.session.flush()   
    ret = {"status": 1, 'url': '/tcadmin/'}  
    return redirect('/tcadmin/')
    """实现退出登录逻辑"""
# 自动登录获取 cookie
def login_view(request):
    
    aim_url = {
        'url': 'https://zh.surebet.com/users/sign_in',
        'username': '731772412@qq.com',
        'password': 'dnjsrl0620'
    }
    # 登录
    # driver = login_fr(aim_url['url'], aim_url['username'], aim_url['password'])
    t_cookie2=denglu.login_fr(aim_url['url'], aim_url['username'], aim_url['password'])
    print(t_cookie2)
    # cookie=tools.getLogin("1")
    ret = {"status": '登录', 'url': t_cookie2}
    return HttpResponse(json.dumps(ret))
    
  
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


def add_user(request):
    if request.method == 'POST':
        usid = request.POST.get('usid','')
        name = request.POST.get('name','')
        if usid=='' or name=='':
            return JsonResponse({'code':100101,'msg':'用户id或密码不能为空'})
        if usid=='1' and name=='james':
            return JsonResponse({'code':100200,'msg':'添加成功','data':{'usid':1,'name':'james','age':36}})
        else:
            return JsonResponse({'code':100102,'msg':'添加失败'})

    else:
        return JsonResponse({'code': 100103, 'msg': '请求方法错误'})


# vue 前后分离
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# @api_view(["GET", "POST"])
def htmlInfo(request):  

    if request.method=="POST":
        userId=request.session.get('_auth_user_id')
        # row_object=models.TcSearch.objects.filter(uid=userId)
        get_json = request.body
        # get_json=get_json.decode()         
        params =viewFunc.searchDict(userId,get_json)        
    return JsonResponse({'code':100200,'msg':'添加成功','data':params})    

        
@csrf_exempt
def nextPage(request):
    if request.method=="POST":
        userId=request.session.get('_auth_user_id')
        # row_object=models.TcSearch.objects.filter(uid=userId)
        get_json = request.body
        # get_json=get_json.decode()     
        cursor=request.GET['page'] 
        
        params =viewFunc.searchNext(userId,cursor)  
        
        return JsonResponse({'code':100200,'msg':'添加成功','data':params})   
    
def ydty0(request): 
    return render(request,"calculator/ydty0.html")  
def ydty1(request): 
    return render(request,"calculator/ydty1.html")  
def ydty2(request): 
    return render(request,"calculator/ydty2.html")  
def ydty3(request): 
    return render(request,"calculator/ydty3.html")  


def websocket_view(request):
    return render(request, 'websocket.html')

 

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
    

def showLog(request,room_name):
    return render(request, 'chat/showLog.html', {
         'room_name': room_name
        
    })



import tkinter.messagebox #弹窗库
from tkinter import *
from moon39.celeryAuto  import  DynamicPeriodicTask
from app1.tasks import taskQuantifyPrice

from apiV1.DeFi2 import celeryPrice,celeryBuySell
def QuantifyRun(request):
    params='log'
    acct=request.user
    if acct==None :
        # return JsonResponse({'code':100200,'msg':'请登录','data':params})   
        tkinter.messagebox.showinfo('提示','请登录')
        mainloop()
        return redirect('/admin') 

    if request.method=="GET": 
        acct=request.user 
        QuantifyId = request.GET.get('id','')
        # 自动创建task
        # 执行自动读价格 保存 task 名字 到 redis 
        
        # taskQuantifyPrice(QuantifyId)
        
        # taskQuantifyBuySell(QuantifyId)
        
        # celeryPrice.work(id)
        
        # 获得 时间 
            # sub = CourseModel.objects.get(id=student_id)

        Quantify= T_Quantify1.objects.get(id=QuantifyId)
        
        # task_taskQuantifyPrice = DynamicPeriodicTask.create_task(Quantify.Token_Price_Time,'app1.tasks.taskQuantifyPrice' , [QuantifyId, ])
        
        task_taskQuantifyBuySell = DynamicPeriodicTask.create_task(Quantify.Token_Transaction_Time,'app1.tasks.taskQuantifyBuySell' , [QuantifyId ],Quantify.start_time,Quantify.end_time,Quantify.duration)
        
        # t_taskId=task_taskQuantifyPrice+","+task_taskQuantifyBuySell
        t_taskId=task_taskQuantifyBuySell



        # t_taskId=task_taskQuantifyPrice+"," 

        
        # t_taskId =taskQuantifyPrice.delay(QuantifyId)
        # 
        # DeFi2.work(QuantifyId)
        
        # t_task = taskQuantify.delay(QuantifyId)   
        # t_taskId = t_taskId.id   
       
        # t_taskId = taskQuantify.delay(QuantifyId)        
        t_task=T_task ()
        t_task.taskId=str(t_taskId)
        t_task.QuantifyId=QuantifyId
        t_task.taskRemark='remark'
        t_task.uid=acct
        t_task.save() 
        print('log')
        return redirect('/admin/app1/t_quantify1/')

    # return JsonResponse({'code':100200,'msg':'添加成功','data':params})    


def log(request):
    # data="{'utf8': ['✓'], 'filter[selected][]': ['33714663'], 'filter[current_id]': ['33714663'], 'selector[order]': ['profit'], 'selector[outcomes][]': ['2', '3'], 'selector[min_profit]': ['0.0'], 'selector[settled_in]': ['86400'], 'selector[bookies_settings]': ['67,66,27'], 'selector[exclude_sports_ids_str]': ['26,23,2,13'], 'selector[extra_filters]': ['3']}"
    # # data ='''
    # # {"name": "Bill", "info": {"sex": "male", "age": 29, "birth": "19900506"}}
    # # '''    
    
    # datadict = json.loads(json.dumps(eval(data)))
    # print(datadict)
    # params =viewFunc.searchDict(1,datadict)

    params='log'

    if request.method=="GET":
        # userId=request.session.get('_auth_user_id')
        # # row_object=models.TcSearch.objects.filter(uid=userId)
        # get_json = request.body
        # # get_json=get_json.decode()         
        # params =viewFunc.searchDict(userId,get_json)        
        print('log')
    return JsonResponse({'code':100200,'msg':'添加成功','data':params})    




def stopTask(request):

     
    # time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')                
    # # result = [time1,'出售地址:',self.walletAddress ,f"出售完成: {self.web3.fromWei(tokenToSell, self.TradingTokenDecimal)}  " ,'hash:',self.web3.to_hex(tx_token),]
    # result = [time1,'已关闭:']


    celery_control = Control(app=app)

    id = request.GET.get('id','')
    t_task=T_task.objects.filter(id=id ).order_by('-id').first()
    
    if not t_task==None:
        # 处理 动态 task
        
        # str(t_task.taskId)
        items = str(t_task.taskId).split(',')        
        for item in items:
            # print(item)
            DynamicPeriodicTask.delete_task(item)

        
        
        # 处理静态task 
        # reCelery=celery_control.revoke(str(t_task.taskId), terminate=True)  
        # 修改task状态
        t_task.status=0
        t_task.save()
    # else:
        # result = [time1,'没有找到 taskId'] 
    

    return redirect('/admin/app1/t_task/') 
def my_custom_view(request):    
    
    fields_a = ['TRADE_TOKEN_ADDRESS', 'buyPrice']
    fields_b = ['taskId', 'QuantifyId']
    
     # Get verbose names for fields_a
    model_a = T_Quantify1
    verbose_names_a = {field: model_a._meta.get_field(field).verbose_name for field in fields_a}
    
    # Get verbose names for fields_b
    model_b = T_task
    verbose_names_b = {field: model_b._meta.get_field(field).verbose_name for field in fields_b}


    
    items_a_data = [
        {field: getattr(item, field) for field in fields_a} 
        for item in T_Quantify1.objects.all()
    ]
    
    items_b_data = [
        {field: getattr(item, field) for field in fields_b} 
        for item in T_task.objects.all()
    ]
    print('dk')
    return render(request, 'my_custom_page.html', {
        'items_a_data': items_a_data, 
        'items_b_data': items_b_data, 
        'fields_a': fields_a, 
        'fields_b': fields_b,
        'verbose_names_a': verbose_names_a,
        'verbose_names_b': verbose_names_b,
    })
    
    
    
    
    # fields_a = ['TRADE_TOKEN_ADDRESS', 'buyPrice']
    # fields_b = ['taskId', 'QuantifyId']

    # field_names_a = [T_Quantify1._meta.get_field(field).verbose_name for field in fields_a]
    # field_names_b = [T_task._meta.get_field(field).verbose_name for field in fields_b]

    # return render(request, 'my_custom_page.html', {
    #     'items_a': items_a, 
    #     'items_b': items_b, 
    #     'fields_a': fields_a, 
    #     'fields_b': fields_b,
    #     'field_names_a': field_names_a,
    #     'field_names_b': field_names_b
    # })
    
    
    # fields_a = ['TRADE_TOKEN_ADDRESS', 'buyPrice']  # The fields you want to show for ModelA
    # fields_b = ['taskId', 'QuantifyId']  # The fields you want to show for ModelB
    # return render(request, 'my_custom_page.html', {'items_a': items_a, 'items_b': items_b, 'fields_a': fields_a, 'fields_b': fields_b})


    
    
    # modela_list = T_Quantify1.objects.all()
    # modelb_list = T_Quantify1.objects.all()
    
    # context = {
    #     'modela_list': modela_list,
    #     'modelb_list': modelb_list,
    # }
    # return render(request, 'my_custom_page.html', context)

@csrf_exempt
def add_to_modelb(request):
    model_a_id = request.POST.get('model_a_id')
    # ... Logic to add a new record to ModelB based on ModelA id ...

    return JsonResponse({'status': 'success'})

@csrf_exempt
def handle_modelb(request):
    model_b_id = request.POST.get('model_b_id')
    # ... Logic to handle ModelB record ...

    return JsonResponse({'status': 'success'})

   
def custom_template_view(request):
    # print("dk")
    # return HttpResponseRedirect('/admin/app1/t_tokenaddr/')  # 重定向到列表页面

    if request.method == "POST":
        acct=request.user
            # 从POST请求中获取数据
        category_id = request.POST.get('category') 
        data_text = request.POST.get('data')

        # 分割数据，按行处理
        data_lines = data_text.strip().splitlines()

        # 使用数据库事务来确保所有操作都成功完成
        with transaction.atomic():
            for line in data_lines:
                # 假设每行是一个TOKEN_private
                token_private_data = line.strip()
                
                # 创建新的T_TokenAddr实例
                T_TokenAddr.objects.create(
                    # TOKEN_ADDRESS=
                    # wallList=createWallet.dbWallet(token_private_data),
                    TOKEN_private=createWallet.dbWallet(token_private_data),
                    category_id=category_id,
                    uid=acct
                )
                T_TokenAddrBak.objects.create(
                    # TOKEN_ADDRESS=wallet['address'],
                    TOKEN_private=createWallet.dbWallet(token_private_data),
                    category_id=category_id,
                    uid=acct
                                )
        return HttpResponseRedirect('/admin/app1/t_tokenaddr/')  # 重定向到列表页面

    # 获取分类选项
    # categories = CategoryToken.objects.all()
    categories = CategoryToken.objects.filter(uid=request.user)

    categories= [{'value': cat.id, 'label': cat.name} for cat in categories]

    context = {
        'categories': categories,
        'tips': '导入数据',
        'confirm_button': '确认导入',
        # 'cancel_button': '取消',
        'labelWidth': "100px",
    }
    return render(request, 'your_template_name.html', context)



# from amis_render.views import AmisRenderView
# from django_amis_render.views import AmisRenderView

# class MyAmisPageView(AmisRenderView):
#     # model = MyModel
#     AMIS_CONFIG = {
#     'type': 'page',
#     'title': 'AMIS Page',
#     'body': {
#         'type': 'form',
#         'controls': [
#             {
#                 'type': 'text',
#                 'name': 'name',
#                 'label': 'Name',
#                 'required': True,
#             },
#             {
#                 'type': 'textarea',
#                 'name': 'description',
#                 'label': 'Description',
#             },
#         ],
#     },
#                     }
#     amis_config = AMIS_CONFIG
#     template_name = 'my_amis_page.html'