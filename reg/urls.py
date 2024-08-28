from django.urls import path
from . import views


from . import views,viewsEbc,viewReg,viewsNodeKJ
from rest_framework import routers, serializers, viewsets 

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('signup/<int:parent_id>/', views.register, name='signup_with_parent'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    
    path('resend-activation-link/<int:user_id>/', views.resend_activation_link, name='resend_activation_link'),
    
    path('user_hierarchy/', views.user_hierarchy, name='user_hierarchy'),
    
    path('user_detail/', views.user_detail, name='user_detail'),
    # Ebc
    # 获取当天加速
    path('getdayfanhuan/', viewsEbc.getDayFanHuan, name='getdayfanhuan'),
    path('ebctixian/', viewsEbc.ebcTiXian, name='ebcTiXian'),
    path('ebctuandui/', viewsEbc.ebcTuanDui, name='ebcTuanDui'),
    
    path('ebcusertuichu/', viewsEbc.ebcUserTuiChuView, name='ebcUserTuichu'),
    
    path('ebctest/', viewsEbc.ebcTest, name='ebcTest'),
    # 改变父类
    path('changfu/', viewsEbc.changFuLeiview, name='changfu'),
    
    # 注册新用户 返回 用户信息， 创建userToken
    path('reguser/', viewsEbc.regUser, name='reguser'),
    path('iskapai/', viewsEbc.isKapai, name='isKapai'),
    
    path('setuserparent/', viewsEbc.setUserParent, name='setUserParent'),
    path('webinfo/', viewsEbc.webInfoView, name='webinfo'),    
    path('sign-message/', viewReg.sign_message, name='sign_message'),
    path('verify-signature/', viewReg.verify_signature, name='verify_signature'),
    path('ebctixianmatic/', viewsEbc.ebcTiXianMatic, name='ebcTiXianMatic'),
    # 节点矿机
    path('buynodeKJ/', viewsNodeKJ.buynodeKJ, name='buynodeKJ'),

    path('buyRanLiaoBao/', viewsNodeKJ.buyRanLiaoBao, name='buyRanLiaoBao'),

    path('getKJDayFanHuan/', viewsNodeKJ.getKJDayFanHuan, name='getKJDayFanHuan'),
    # 点击提现 首先触发 获取 sig
    path('signature/', viewsNodeKJ.generate_signature, name='signature'),
    path('generate_key/', viewsNodeKJ.generate_key, name='generate_key'),
    path('verify_signature/', viewsNodeKJ.verify_signature, name='verify_signature'),

    path('fanTiXian/', viewsNodeKJ.fanTiXian, name='verify_signature'),

    path('buynodeKJStart/', viewsNodeKJ.buynodeKJStart, name='buynodeKJStart'),




    

     

    


]

router = routers.DefaultRouter()
router.register(r'customuserlistcreateview', viewsEbc.CustomUserListCreateView)

router.register(r'jiasushouyi', viewsEbc.ebcJiaSuShouYiJiLuView)

router.register(r'tokenzhiya', viewsEbc.tokenZhiYaJiShiView)

router.register(r'paytoken', viewsEbc.ebcPayTokenView)

#节点矿机用户质押列表
router.register(r'userkjlist',viewsNodeKJ.userTokenZhiYaJiShiListView)
#节点矿机用户质押列表
# router.register(r'userkjlistStop',viewsNodeKJ.userTokenZhiYaJiShiListView)
# router.register(r'CustomUserListCreateView', viewsEbc.CustomUserListCreateView)
urlpatterns += router.urls