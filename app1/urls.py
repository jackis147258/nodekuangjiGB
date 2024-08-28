
from django.urls import re_path, path, include
# import app1.views
import traceback
from . import views
from django.views.generic import ListView

urlpatterns = [
    path('layout/',views.layout),    
    path('mycustompage/', views.my_custom_view, name='mycustompage'),  
    path('info/', views.info, name='info'),
    path('htmlInfo/', views.htmlInfo, name='htmlInfo'),
    path('nextPage/', views.nextPage, name='nextPage'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'), # 自动登录 获取 cookie
    path('calculator/ydty0.html', views.ydty0, name='ydty0'),
    path('calculator/ydty1.html', views.ydty1, name='ydty1'),
    path('calculator/ydty2.html', views.ydty2, name='ydty2'),
    path('calculator/ydty3.html', views.ydty3, name='ydty3'),
    path('chat/', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),    
    path('showlog/<str:room_name>/', views.showLog, name='showLog'),     
    path('QuantifyRun/', views.QuantifyRun, name='QuantifyRun'),    
    path('log/', views.log, name='log'),
    path('stopTask/', views.stopTask, name='stopTask'),    
    
    path('add_to_modelb/', views.add_to_modelb, name='add_to_modelb'),
    path('handle_modelb/', views.handle_modelb, name='handle_modelb'),
    
    path('custom_template_view/', views.custom_template_view, name='custom_template_view'),
    
    # path('my-amis-page/', views.MyAmisPageView.as_view(), name='my_amis_page'),


    
]

 